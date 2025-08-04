#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Configuração do Banco de Dados
Integração com Supabase PostgreSQL e salvamento local
"""

import os
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any

# Tenta importar Supabase, usa fallback se falhar
try:
    from services.supabase_client import supabase_client
    HAS_SUPABASE = True
except ImportError:
    HAS_SUPABASE = False
    supabase_client = None

# Importa fallback
from services.database_fallback import database_fallback
from services.local_file_manager import local_file_manager
import json

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Gerenciador de conexão e operações com Supabase + salvamento local"""
    
    def __init__(self):
        """Inicializa gerenciador com Supabase e arquivos locais"""
        # Tenta usar Supabase, fallback para SQLite
        if HAS_SUPABASE and supabase_client and supabase_client.is_connected():
            self.supabase = supabase_client
            self.use_fallback = False
            logger.info("✅ Database Manager usando Supabase")
        else:
            self.supabase = database_fallback
            self.use_fallback = True
            logger.info("⚠️ Database Manager usando SQLite (fallback)")
            
        self.local_files = local_file_manager
        
        db_type = "SQLite Fallback" if self.use_fallback else "Supabase"
        logger.info(f"✅ Database Manager inicializado com {db_type} + Local Files")
    
    def test_connection(self) -> bool:
        """Testa conexão com o banco"""
        try:
            return self.supabase.test_connection()
        except Exception as e:
            logger.error(f"❌ Erro ao testar conexão: {e}")
            return False
    
    def create_analysis(self, analysis_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Cria nova análise no banco e salva localmente"""
        try:
            # 1. Salva arquivos localmente primeiro
            logger.info("💾 Salvando análise em arquivos locais...")
            local_result = self.local_files.save_analysis_locally(analysis_data)
            
            if not local_result['success']:
                logger.error(f"❌ Falha ao salvar localmente: {local_result.get('error')}")
                return None
            
            # 2. Adiciona caminho dos arquivos locais aos dados
            analysis_data['local_files_path'] = local_result.get('base_directory')
            analysis_data['local_files_info'] = local_result.get('files', [])
            
            # 3. Salva no Supabase
            logger.info("☁️ Salvando análise no Supabase...")
            supabase_result = self.supabase.create_analysis(analysis_data)
            
            if supabase_result:
                # 4. Salva informações dos arquivos no Supabase
                analysis_id = supabase_result['id']
                
                for file_info in local_result.get('files', []):
                    self.supabase.save_analysis_file(analysis_id, {
                        'file_type': file_info['type'],
                        'file_name': file_info['name'],
                        'file_path': file_info['path'],
                        'file_size': file_info['size'],
                        'content_preview': f"Arquivo {file_info['type']} da análise"
                    })
                
                logger.info(f"✅ Análise criada: Supabase ID {analysis_id} + {len(local_result['files'])} arquivos locais")
                
                # Retorna dados combinados
                return {
                    **supabase_result,
                    'local_files': local_result
                }
            else:
                logger.warning("⚠️ Falha no Supabase, mas arquivos locais salvos com sucesso")
                return {
                    'id': local_result['analysis_id'],
                    'local_only': True,
                    'local_files': local_result
                }
                
        except Exception as e:
            logger.error(f"❌ Erro ao criar análise: {str(e)}")
            return None
    
    def update_analysis(self, analysis_id: int, update_data: Dict[str, Any]) -> bool:
        """Atualiza análise existente"""
        return self.supabase.update_analysis(str(analysis_id), update_data)
    
    def get_analysis(self, analysis_id: int) -> Optional[Dict[str, Any]]:
        """Busca análise por ID"""
        return self.supabase.get_analysis(str(analysis_id))
    
    def list_analyses(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        """Lista análises com paginação"""
        return self.supabase.list_analyses(limit, offset)
    
    def delete_analysis(self, analysis_id: int) -> bool:
        """Remove análise do banco"""
        # Remove do Supabase
        supabase_result = self.supabase.delete_analysis(str(analysis_id))
        
        # Remove arquivos locais
        local_result = self.local_files.delete_local_analysis(str(analysis_id))
        
        return supabase_result or local_result
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do banco"""
        # Combina estatísticas do banco e arquivos locais
        try:
            db_stats = self.supabase.get_stats()
        except Exception as e:
            logger.error(f"❌ Erro ao obter stats do banco: {e}")
            db_stats = {'error': str(e), 'total_analyses': 0}
            
        local_analyses = self.local_files.list_local_analyses()
        
        return {
            **db_stats,
            'local_analyses_count': len(local_analyses),
            'local_analyses': local_analyses[:10],  # Últimas 10
            'storage_type': f'hybrid_{"sqlite" if self.use_fallback else "supabase"}_local',
            'fallback_mode': self.use_fallback
        }
    
    def get_analysis_files(self, analysis_id: str) -> List[Dict[str, Any]]:
        """Busca arquivos de uma análise"""
        return self.supabase.get_analysis_files(analysis_id)
    
    def list_local_analyses(self) -> List[Dict[str, Any]]:
        """Lista análises salvas localmente"""
        return self.local_files.list_local_analyses()

# Instância global do gerenciador
db_manager = DatabaseManager()