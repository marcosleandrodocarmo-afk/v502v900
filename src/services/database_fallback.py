#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Database Fallback
Sistema de fallback para banco de dados quando PostgreSQL não está disponível
"""

import os
import logging
import sqlite3
import json
from datetime import datetime
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

class DatabaseFallback:
    """Sistema de fallback usando SQLite quando PostgreSQL não está disponível"""
    
    def __init__(self):
        """Inicializa fallback com SQLite"""
        self.db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'arqv30.db')
        self.ensure_database_exists()
        logger.info(f"✅ Database Fallback inicializado: {self.db_path}")
    
    def ensure_database_exists(self):
        """Garante que o banco SQLite existe"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS analyses (
                    id TEXT PRIMARY KEY,
                    segmento TEXT NOT NULL,
                    produto TEXT,
                    publico TEXT,
                    preco REAL,
                    objetivo_receita REAL,
                    orcamento_marketing REAL,
                    prazo_lancamento TEXT,
                    concorrentes TEXT,
                    dados_adicionais TEXT,
                    query_text TEXT,
                    status TEXT DEFAULT 'completed',
                    comprehensive_analysis TEXT,
                    local_files_path TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS analysis_files (
                    id TEXT PRIMARY KEY,
                    analysis_id TEXT,
                    file_type TEXT,
                    file_name TEXT,
                    file_path TEXT,
                    file_size INTEGER DEFAULT 0,
                    content_preview TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (analysis_id) REFERENCES analyses (id)
                )
            ''')
            
            conn.commit()
    
    def test_connection(self) -> bool:
        """Testa conexão com SQLite"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('SELECT 1')
            return True
        except Exception as e:
            logger.error(f"❌ Erro na conexão SQLite: {e}")
            return False
    
    def create_analysis(self, analysis_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Cria nova análise no SQLite"""
        try:
            analysis_id = f"analysis_{int(datetime.now().timestamp())}_{os.urandom(4).hex()}"
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT INTO analyses (
                        id, segmento, produto, publico, preco, objetivo_receita,
                        orcamento_marketing, prazo_lancamento, concorrentes, 
                        dados_adicionais, query_text, status, comprehensive_analysis,
                        local_files_path, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    analysis_id,
                    analysis_data.get('segmento', ''),
                    analysis_data.get('produto', ''),
                    analysis_data.get('publico', ''),
                    analysis_data.get('preco'),
                    analysis_data.get('objetivo_receita'),
                    analysis_data.get('orcamento_marketing'),
                    analysis_data.get('prazo_lancamento', ''),
                    analysis_data.get('concorrentes', ''),
                    analysis_data.get('dados_adicionais', ''),
                    analysis_data.get('query', ''),
                    analysis_data.get('status', 'completed'),
                    json.dumps(analysis_data, ensure_ascii=False),
                    analysis_data.get('local_files_path'),
                    datetime.now().isoformat(),
                    datetime.now().isoformat()
                ))
                
                conn.commit()
            
            logger.info(f"✅ Análise criada no SQLite: {analysis_id}")
            return {'id': analysis_id, **analysis_data}
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar análise no SQLite: {e}")
            return None
    
    def get_analysis(self, analysis_id: str) -> Optional[Dict[str, Any]]:
        """Busca análise por ID"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute('SELECT * FROM analyses WHERE id = ?', (analysis_id,))
                row = cursor.fetchone()
                
                if row:
                    return dict(row)
                return None
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar análise {analysis_id}: {e}")
            return None
    
    def list_analyses(self, limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
        """Lista análises com paginação"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute('''
                    SELECT id, segmento, produto, status, created_at, updated_at, local_files_path
                    FROM analyses 
                    ORDER BY created_at DESC 
                    LIMIT ? OFFSET ?
                ''', (limit, offset))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            logger.error(f"❌ Erro ao listar análises: {e}")
            return []
    
    def update_analysis(self, analysis_id: str, update_data: Dict[str, Any]) -> bool:
        """Atualiza análise existente"""
        try:
            update_data['updated_at'] = datetime.now().isoformat()
            
            # Constrói query de update dinamicamente
            fields = list(update_data.keys())
            placeholders = ', '.join([f'{field} = ?' for field in fields])
            values = list(update_data.values()) + [analysis_id]
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(f'''
                    UPDATE analyses 
                    SET {placeholders}
                    WHERE id = ?
                ''', values)
                
                conn.commit()
            
            logger.info(f"✅ Análise {analysis_id} atualizada no SQLite")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao atualizar análise {analysis_id}: {e}")
            return False
    
    def delete_analysis(self, analysis_id: str) -> bool:
        """Remove análise do banco"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('DELETE FROM analysis_files WHERE analysis_id = ?', (analysis_id,))
                conn.execute('DELETE FROM analyses WHERE id = ?', (analysis_id,))
                conn.commit()
            
            logger.info(f"✅ Análise {analysis_id} removida do SQLite")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao remover análise {analysis_id}: {e}")
            return False
    
    def save_analysis_file(self, analysis_id: str, file_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Salva informações de arquivo de análise"""
        try:
            file_id = f"file_{int(datetime.now().timestamp())}_{os.urandom(4).hex()}"
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT INTO analysis_files (
                        id, analysis_id, file_type, file_name, file_path,
                        file_size, content_preview, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    file_id,
                    analysis_id,
                    file_data.get('file_type'),
                    file_data.get('file_name'),
                    file_data.get('file_path'),
                    file_data.get('file_size', 0),
                    file_data.get('content_preview', ''),
                    datetime.now().isoformat()
                ))
                
                conn.commit()
            
            logger.info(f"✅ Arquivo de análise salvo no SQLite: {file_data.get('file_name')}")
            return {'id': file_id, **file_data}
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar arquivo de análise: {e}")
            return None
    
    def get_analysis_files(self, analysis_id: str) -> List[Dict[str, Any]]:
        """Busca arquivos de uma análise"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute('''
                    SELECT * FROM analysis_files 
                    WHERE analysis_id = ? 
                    ORDER BY created_at DESC
                ''', (analysis_id,))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar arquivos da análise {analysis_id}: {e}")
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do banco"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Total de análises
                cursor = conn.execute('SELECT COUNT(*) FROM analyses')
                total_analyses = cursor.fetchone()[0]
                
                # Análises por status
                cursor = conn.execute('SELECT status, COUNT(*) FROM analyses GROUP BY status')
                status_counts = dict(cursor.fetchall())
                
                # Análises recentes (últimos 7 dias)
                week_ago = (datetime.now().timestamp() - 7*24*60*60)
                cursor = conn.execute('''
                    SELECT COUNT(*) FROM analyses 
                    WHERE datetime(created_at) > datetime(?, 'unixepoch')
                ''', (week_ago,))
                recent_count = cursor.fetchone()[0]
                
                return {
                    'total_analyses': total_analyses,
                    'status_counts': status_counts,
                    'recent_analyses': recent_count,
                    'database_type': 'SQLite (Fallback)',
                    'timestamp': datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"❌ Erro ao obter estatísticas: {e}")
            return {
                'total_analyses': 0,
                'status_counts': {},
                'recent_analyses': 0,
                'database_type': 'SQLite (Fallback)',
                'error': str(e)
            }

# Instância global de fallback
database_fallback = DatabaseFallback()