#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Complete Drivers Architect
Arquiteto Completo de Drivers Mentais baseado no documento de integração
"""

import time
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class CompleteDriversArchitect:
    """Arquiteto Completo de Drivers Mentais - Sistema de Ancoragem Psicológica"""
    
    def __init__(self):
        """Inicializa o arquiteto completo de drivers"""
        self.universal_drivers = self._load_19_universal_drivers()
        self.optimization_patterns = self._load_optimization_patterns()
        
        logger.info("Complete Drivers Architect inicializado com 19 drivers universais")
    
    def _load_19_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """Carrega os 19 drivers universais do documento"""
        return {
            # DRIVERS EMOCIONAIS PRIMÁRIOS
            'ferida_exposta': {
                'nome': 'DRIVER DA FERIDA EXPOSTA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Exposição da dor mais profunda',
                'definicao_visceral': 'Revelar a ferida que eles tentam esconder de si mesmos',
                'fase_ideal': 'despertar'
            },
            'trofeu_secreto': {
                'nome': 'DRIVER DO TROFÉU SECRETO',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Desejo oculto de reconhecimento',
                'definicao_visceral': 'Ativar o desejo secreto de ser admirado e invejado',
                'fase_ideal': 'desejo'
            },
            'inveja_produtiva': {
                'nome': 'DRIVER DA INVEJA PRODUTIVA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Comparação social estratégica',
                'definicao_visceral': 'Usar inveja como combustível para ação',
                'fase_ideal': 'desejo'
            },
            'relogio_psicologico': {
                'nome': 'DRIVER DO RELÓGIO PSICOLÓGICO',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Pressão temporal visceral',
                'definicao_visceral': 'Criar urgência que paralisa procrastinação',
                'fase_ideal': 'decisao'
            },
            'identidade_aprisionada': {
                'nome': 'DRIVER DA IDENTIDADE APRISIONADA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Prisão da autoimagem atual',
                'definicao_visceral': 'Mostrar como identidade atual os limita',
                'fase_ideal': 'despertar'
            },
            'custo_invisivel': {
                'nome': 'DRIVER DO CUSTO INVISÍVEL',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Perdas não percebidas',
                'definicao_visceral': 'Revelar o que estão perdendo sem perceber',
                'fase_ideal': 'decisao'
            },
            'ambicao_expandida': {
                'nome': 'DRIVER DA AMBIÇÃO EXPANDIDA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Visão ampliada do possível',
                'definicao_visceral': 'Expandir limites do que acreditam ser possível',
                'fase_ideal': 'desejo'
            },
            'diagnostico_brutal': {
                'nome': 'DRIVER DO DIAGNÓSTICO BRUTAL',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Verdade dolorosa sobre situação atual',
                'definicao_visceral': 'Confrontar com realidade sem filtros',
                'fase_ideal': 'despertar'
            },
            'ambiente_vampiro': {
                'nome': 'DRIVER DO AMBIENTE VAMPIRO',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Influências tóxicas ao redor',
                'definicao_visceral': 'Identificar pessoas/situações que drenam energia',
                'fase_ideal': 'despertar'
            },
            'mentor_salvador': {
                'nome': 'DRIVER DO MENTOR SALVADOR',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Necessidade de orientação',
                'definicao_visceral': 'Posicionar como guia necessário para transformação',
                'fase_ideal': 'direcao'
            },
            'coragem_necessaria': {
                'nome': 'DRIVER DA CORAGEM NECESSÁRIA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Ato de bravura requerido',
                'definicao_visceral': 'Transformar medo em coragem para agir',
                'fase_ideal': 'direcao'
            },
            
            # DRIVERS RACIONAIS COMPLEMENTARES
            'mecanismo_revelado': {
                'nome': 'DRIVER DO MECANISMO REVELADO',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Como funciona por dentro',
                'definicao_visceral': 'Revelar o funcionamento interno do sistema',
                'fase_ideal': 'direcao'
            },
            'prova_matematica': {
                'nome': 'DRIVER DA PROVA MATEMÁTICA',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Números irrefutáveis',
                'definicao_visceral': 'Usar matemática para provar viabilidade',
                'fase_ideal': 'direcao'
            },
            'padrao_oculto': {
                'nome': 'DRIVER DO PADRÃO OCULTO',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Padrão que poucos veem',
                'definicao_visceral': 'Revelar padrão secreto de sucesso',
                'fase_ideal': 'despertar'
            },
            'excecao_possivel': {
                'nome': 'DRIVER DA EXCEÇÃO POSSÍVEL',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Possibilidade de ser diferente',
                'definicao_visceral': 'Mostrar que podem ser exceção à regra',
                'fase_ideal': 'desejo'
            },
            'atalho_etico': {
                'nome': 'DRIVER DO ATALHO ÉTICO',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Caminho mais rápido e correto',
                'definicao_visceral': 'Apresentar atalho que não compromete valores',
                'fase_ideal': 'direcao'
            },
            'decisao_binaria': {
                'nome': 'DRIVER DA DECISÃO BINÁRIA',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Duas opções claras',
                'definicao_visceral': 'Simplificar escolha em duas opções extremas',
                'fase_ideal': 'decisao'
            },
            'oportunidade_oculta': {
                'nome': 'DRIVER DA OPORTUNIDADE OCULTA',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Chance que poucos veem',
                'definicao_visceral': 'Revelar oportunidade escondida à vista de todos',
                'fase_ideal': 'despertar'
            },
            'metodo_vs_sorte': {
                'nome': 'DRIVER DO MÉTODO VS SORTE',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Diferença entre sistema e tentativa',
                'definicao_visceral': 'Contrastar método científico com tentativa aleatória',
                'fase_ideal': 'direcao'
            }
        }
    
    def _load_optimization_patterns(self) -> Dict[str, Any]:
        """Carrega padrões de otimização e sobreposições"""
        return {
            'drivers_complementares': [
                'diagnostico_brutal → ambicao_expandida',
                'ambiente_vampiro → mentor_salvador',
                'oportunidade_oculta → metodo_vs_sorte',
                'ferida_exposta → coragem_necessaria',
                'custo_invisivel → decisao_binaria'
            ],
            'drivers_reforco': [
                'ferida_exposta + diagnostico_brutal',
                'relogio_psicologico + custo_invisivel',
                'coragem_necessaria + decisao_binaria',
                'ambicao_expandida + trofeu_secreto',
                'metodo_vs_sorte + mentor_salvador'
            ],
            'top_7_essenciais': [
                'diagnostico_brutal',
                'ambicao_expandida', 
                'relogio_psicologico',
                'metodo_vs_sorte',
                'decisao_binaria',
                'ambiente_vampiro',
                'coragem_necessaria'
            ],
            'sequenciamento_fases': {
                'fase_1_despertar': ['oportunidade_oculta', 'diagnostico_brutal', 'ferida_exposta'],
                'fase_2_desejo': ['ambicao_expandida', 'trofeu_secreto', 'inveja_produtiva'],
                'fase_3_decisao': ['relogio_psicologico', 'custo_invisivel', 'decisao_binaria'],
                'fase_4_direcao': ['metodo_vs_sorte', 'mentor_salvador', 'coragem_necessaria']
            }
        }
    
    def generate_complete_drivers_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de drivers mentais baseado no documento"""
        
        try:
            logger.info("🧠 Gerando sistema completo de drivers mentais...")
            
            # Salva dados de entrada
            salvar_etapa("drivers_completos_entrada", {
                "avatar_data": avatar_data,
                "context_data": context_data
            }, categoria="drivers_mentais")
            
            # Fase 1: Diagnóstico do Avatar
            avatar_diagnosis = self._diagnose_avatar_for_drivers(avatar_data)
            salvar_etapa("diagnostico_avatar", avatar_diagnosis, categoria="drivers_mentais")
            
            # Fase 2: Seleção de Drivers Base
            selected_drivers = self._select_optimal_drivers(avatar_diagnosis, context_data)
            salvar_etapa("drivers_selecionados", selected_drivers, categoria="drivers_mentais")
            
            # Fase 3: Customização Profunda
            customized_drivers = self._customize_drivers_deeply(selected_drivers, avatar_data, context_data)
            salvar_etapa("drivers_customizados_profundo", customized_drivers, categoria="drivers_mentais")
            
            # Fase 4: Sequenciamento Estratégico
            strategic_sequence = self._create_strategic_sequence(customized_drivers)
            salvar_etapa("sequenciamento_estrategico", strategic_sequence, categoria="drivers_mentais")
            
            # Fase 5: Sistema de Implementação
            implementation_system = self._create_implementation_system(customized_drivers, context_data)
            salvar_etapa("sistema_implementacao", implementation_system, categoria="drivers_mentais")
            
            complete_system = {
                'drivers_emocionais_primarios': [d for d in customized_drivers if d.get('categoria') == 'emocional_primario'],
                'drivers_racionais_complementares': [d for d in customized_drivers if d.get('categoria') == 'racional_complementar'],
                'sequenciamento_estrategico': strategic_sequence,
                'otimizacao_sobreposicoes': {
                    'drivers_complementares': self.optimization_patterns['drivers_complementares'],
                    'drivers_reforco': self.optimization_patterns['drivers_reforco']
                },
                'top_7_essenciais': self.optimization_patterns['top_7_essenciais'],
                'sistema_implementacao': implementation_system,
                'avatar_diagnosis': avatar_diagnosis,
                'metadata_completo': {
                    'total_drivers_criados': len(customized_drivers),
                    'drivers_emocionais': len([d for d in customized_drivers if d.get('categoria') == 'emocional_primario']),
                    'drivers_racionais': len([d for d in customized_drivers if d.get('categoria') == 'racional_complementar']),
                    'generated_at': time.time(),
                    'sistema_completo': True
                }
            }
            
            # Salva sistema completo
            salvar_etapa("sistema_drivers_completo", complete_system, categoria="drivers_mentais")
            
            logger.info(f"✅ Sistema completo de drivers: {len(customized_drivers)} drivers customizados")
            return complete_system
            
        except Exception as e:
            logger.error(f"❌ Erro no sistema completo de drivers: {e}")
            salvar_erro("sistema_drivers_completo", e, contexto=context_data)
            return self._generate_fallback_complete_system(context_data)
    
    def _diagnose_avatar_for_drivers(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Diagnóstico profundo do avatar para seleção de drivers"""
        
        diagnosis = {
            'dores_viscerais_top3': [],
            'desejos_profundos_top3': [],
            'objecoes_resistentes_top3': [],
            'perfil_psicologico': {},
            'drivers_recomendados': []
        }
        
        # Extrai top 3 dores
        dores = avatar_data.get('dores_viscerais', [])
        diagnosis['dores_viscerais_top3'] = dores[:3] if len(dores) >= 3 else dores
        
        # Extrai top 3 desejos
        desejos = avatar_data.get('desejos_secretos', [])
        diagnosis['desejos_profundos_top3'] = desejos[:3] if len(desejos) >= 3 else desejos
        
        # Extrai top 3 objeções
        objecoes = avatar_data.get('objecoes_reais', [])
        diagnosis['objecoes_resistentes_top3'] = objecoes[:3] if len(objecoes) >= 3 else objecoes
        
        # Analisa perfil psicográfico
        perfil_psico = avatar_data.get('perfil_psicografico', {})
        diagnosis['perfil_psicologico'] = {
            'personalidade_dominante': perfil_psico.get('personalidade', ''),
            'valores_principais': perfil_psico.get('valores', ''),
            'medos_profundos': perfil_psico.get('medos_profundos', ''),
            'aspiracoes_secretas': perfil_psico.get('aspiracoes_secretas', '')
        }
        
        # Recomenda drivers baseado no diagnóstico
        diagnosis['drivers_recomendados'] = self._recommend_drivers_from_diagnosis(diagnosis)
        
        return diagnosis
    
    def _recommend_drivers_from_diagnosis(self, diagnosis: Dict[str, Any]) -> List[str]:
        """Recomenda drivers baseado no diagnóstico"""
        
        recommended = []
        
        # Analisa dores para recomendar drivers
        dores_text = ' '.join(diagnosis['dores_viscerais_top3']).lower()
        
        if any(word in dores_text for word in ['tempo', 'ocupado', 'correria']):
            recommended.append('relogio_psicologico')
        
        if any(word in dores_text for word in ['estagnado', 'parado', 'mesmo lugar']):
            recommended.append('diagnostico_brutal')
        
        if any(word in dores_text for word in ['concorrência', 'outros crescendo']):
            recommended.append('inveja_produtiva')
        
        if any(word in dores_text for word in ['potencial', 'desperdiçar']):
            recommended.append('identidade_aprisionada')
        
        # Analisa desejos para recomendar drivers
        desejos_text = ' '.join(diagnosis['desejos_profundos_top3']).lower()
        
        if any(word in desejos_text for word in ['reconhecido', 'autoridade', 'referência']):
            recommended.append('trofeu_secreto')
        
        if any(word in desejos_text for word in ['liberdade', 'passivo', 'automático']):
            recommended.append('ambicao_expandida')
        
        if any(word in desejos_text for word in ['método', 'sistema', 'processo']):
            recommended.append('metodo_vs_sorte')
        
        # Sempre inclui drivers essenciais
        essential_drivers = ['diagnostico_brutal', 'metodo_vs_sorte', 'decisao_binaria']
        for driver in essential_drivers:
            if driver not in recommended:
                recommended.append(driver)
        
        return recommended[:7]  # Top 7 drivers
    
    def _select_optimal_drivers(self, diagnosis: Dict[str, Any], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Seleciona drivers ótimos baseado no diagnóstico"""
        
        recommended_names = diagnosis['drivers_recomendados']
        selected_drivers = []
        
        for driver_name in recommended_names:
            if driver_name in self.universal_drivers:
                driver_data = self.universal_drivers[driver_name].copy()
                driver_data['selected_reason'] = f"Recomendado para {context_data.get('segmento', 'este contexto')}"
                selected_drivers.append(driver_data)
        
        return selected_drivers
    
    def _customize_drivers_deeply(
        self, 
        selected_drivers: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Customização profunda dos drivers usando IA"""
        
        try:
            segmento = context_data.get('segmento', 'negócios')
            
            prompt = f"""
Você é o ARQUITETO DE DRIVERS MENTAIS. Customize profundamente os drivers selecionados.

CONTEXTO:
- Segmento: {segmento}
- Produto: {context_data.get('produto', 'Não informado')}
- Preço: R$ {context_data.get('preco', 'Não informado')}

AVATAR DIAGNOSIS:
{json.dumps(avatar_data, ensure_ascii=False, indent=2)[:2000]}

DRIVERS SELECIONADOS:
{json.dumps(selected_drivers, ensure_ascii=False, indent=2)[:1500]}

Para CADA driver selecionado, crie customização PROFUNDA seguindo EXATAMENTE a estrutura:

RETORNE APENAS JSON VÁLIDO:

```json
[
  {{
    "nome": "DRIVER CUSTOMIZADO ESPECÍFICO",
    "categoria": "emocional_primario ou racional_complementar",
    "gatilho_central": "Emoção ou lógica core específica",
    "definicao_visceral": "1-2 frases que capturam a essência",
    "mecanica_psicologica": "Como funciona no cérebro",
    "momento_instalacao": "Quando plantar durante a jornada",
    "roteiro_ativacao": {{
      "pergunta_abertura": "Pergunta que expõe a ferida específica",
      "historia_analogia": "História específica de 150+ palavras do universo do avatar",
      "metafora_visual": "Metáfora que ancora na memória",
      "comando_acao": "Comando que direciona comportamento específico"
    }},
    "frases_ancoragem": [
      "Frase 1 pronta para usar",
      "Frase 2 pronta para usar",
      "Frase 3 pronta para usar",
      "Frase 4 pronta para usar",
      "Frase 5 pronta para usar"
    ],
    "prova_logica": "Dados/fatos específicos que sustentam",
    "loop_reforco": "Como reativar em momentos posteriores",
    "instalacao_por_formato": {{
      "live_aquecimento": "Como introduzir",
      "cpl_aula1": "Como desenvolver",
      "cpl_aula2": "Como aprofundar",
      "cpl_aula3": "Como cristalizar"
    }}
  }}
]
```
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=4000)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    customized = json.loads(clean_response)
                    if isinstance(customized, list) and len(customized) > 0:
                        logger.info("✅ Drivers customizados profundamente com IA")
                        return customized
                except json.JSONDecodeError:
                    logger.warning("⚠️ JSON inválido na customização profunda")
            
            # Fallback para customização básica
            return self._create_basic_customized_drivers(selected_drivers, context_data)
            
        except Exception as e:
            logger.error(f"❌ Erro na customização profunda: {e}")
            return self._create_basic_customized_drivers(selected_drivers, context_data)
    
    def _create_strategic_sequence(self, customized_drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria sequenciamento estratégico dos drivers"""
        
        # Organiza drivers por fase
        sequence_by_phase = {
            'fase_1_despertar': [],
            'fase_2_desejo': [],
            'fase_3_decisao': [],
            'fase_4_direcao': []
        }
        
        for driver in customized_drivers:
            categoria = driver.get('categoria', 'racional_complementar')
            nome = driver.get('nome', '').lower()
            
            # Mapeia para fases baseado no nome e categoria
            if any(word in nome for word in ['diagnóstico', 'ferida', 'oportunidade']):
                sequence_by_phase['fase_1_despertar'].append(driver)
            elif any(word in nome for word in ['ambição', 'troféu', 'inveja']):
                sequence_by_phase['fase_2_desejo'].append(driver)
            elif any(word in nome for word in ['relógio', 'custo', 'decisão']):
                sequence_by_phase['fase_3_decisao'].append(driver)
            elif any(word in nome for word in ['método', 'mentor', 'coragem']):
                sequence_by_phase['fase_4_direcao'].append(driver)
            else:
                # Default para fase de despertar
                sequence_by_phase['fase_1_despertar'].append(driver)
        
        return {
            'sequencia_por_fase': sequence_by_phase,
            'ordem_psicologica_ideal': [
                'Começar com consciência (Diagnóstico/Oportunidade)',
                'Evoluir para desejo (Ambição/Troféu)',
                'Criar pressão (Urgência/Custo)',
                'Oferecer caminho (Método/Mentor)',
                'Forçar decisão (Coragem/Binária)'
            ],
            'escalada_emocional': 'Crescente até o momento da oferta',
            'intervalos_recomendados': '3-5 minutos entre drivers principais'
        }
    
    def _create_implementation_system(self, customized_drivers: List[Dict[str, Any]], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria sistema de implementação dos drivers"""
        
        return {
            'pre_lancamento': {
                'drivers_recomendados': [d['nome'] for d in customized_drivers[:2]],
                'objetivo': 'Preparação subliminar',
                'formato': 'Lives de aquecimento'
            },
            'durante_evento': {
                'drivers_recomendados': [d['nome'] for d in customized_drivers[2:5]],
                'objetivo': 'Instalação principal',
                'formato': 'CPL ou webinar'
            },
            'momento_oferta': {
                'drivers_recomendados': [d['nome'] for d in customized_drivers[-2:]],
                'objetivo': 'Decisão final',
                'formato': 'Pitch direto'
            },
            'pos_oferta': {
                'drivers_recomendados': ['coragem_necessaria', 'decisao_binaria'],
                'objetivo': 'Neutralizar hesitação',
                'formato': 'Follow-up'
            },
            'cronograma_detalhado': self._create_detailed_timeline(customized_drivers),
            'metricas_eficacia': [
                'Tempo de atenção por driver',
                'Reações emocionais geradas',
                'Perguntas/comentários relacionados',
                'Taxa de conversão pós-ativação'
            ]
        }
    
    def _create_detailed_timeline(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria timeline detalhado de implementação"""
        
        timeline = {}
        
        for i, driver in enumerate(drivers):
            timeline[f"momento_{i+1}"] = {
                'driver': driver.get('nome', f'Driver {i+1}'),
                'timing': f"Minuto {i*5}-{(i+1)*5}",
                'objetivo': driver.get('definicao_visceral', 'Ativação psicológica'),
                'duracao_recomendada': '3-5 minutos',
                'transicao_proxima': f"Conectar com {drivers[i+1].get('nome', 'próximo elemento') if i+1 < len(drivers) else 'oferta'}"
            }
        
        return timeline
    
    def _create_basic_customized_drivers(self, selected_drivers: List[Dict[str, Any]], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Cria drivers customizados básicos como fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        customized = []
        
        for i, driver in enumerate(selected_drivers):
            customized_driver = {
                'nome': f"DRIVER {driver['nome']} PARA {segmento.upper()}",
                'categoria': driver.get('categoria', 'emocional_primario'),
                'gatilho_central': f"{driver.get('gatilho_central', 'Gatilho')} específico para {segmento}",
                'definicao_visceral': f"{driver.get('definicao_visceral', 'Definição')} aplicado ao contexto de {segmento}",
                'roteiro_ativacao': {
                    'pergunta_abertura': f"Como você se sente sobre sua situação atual em {segmento}?",
                    'historia_analogia': f"Imagine um profissional de {segmento} que estava na mesma situação que você...",
                    'metafora_visual': f"É como se {segmento} fosse um oceano e você estivesse nadando sem direção",
                    'comando_acao': f"Pare de nadar em círculos em {segmento} e comece a usar um método comprovado"
                },
                'frases_ancoragem': [
                    f"Cada dia sem otimizar {segmento} é oportunidade perdida",
                    f"Profissionais de {segmento} que agem crescem 10x mais rápido",
                    f"O tempo perdido em {segmento} não volta mais",
                    f"Seus concorrentes em {segmento} não estão esperando",
                    f"Método em {segmento} elimina tentativa e erro"
                ],
                'prova_logica': f"Metodologia específica para {segmento} reduz tempo de resultado em 80%",
                'fallback_mode': True
            }
            customized.append(customized_driver)
        
        return customized
    
    def _generate_fallback_complete_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema completo de fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'drivers_emocionais_primarios': [
                {
                    'nome': f'DRIVER DO DIAGNÓSTICO BRUTAL PARA {segmento.upper()}',
                    'categoria': 'emocional_primario',
                    'gatilho_central': f'Verdade dolorosa sobre situação atual em {segmento}',
                    'definicao_visceral': f'Confrontar com realidade sem filtros sobre {segmento}',
                    'roteiro_ativacao': {
                        'pergunta_abertura': f'Há quanto tempo você está no mesmo nível em {segmento}?',
                        'historia_analogia': f'Conheci um profissional de {segmento} que estava exatamente onde você está...',
                        'comando_acao': f'Pare de se enganar sobre sua situação em {segmento}'
                    },
                    'frases_ancoragem': [
                        f'A verdade sobre {segmento} dói, mas liberta',
                        f'Autoengano em {segmento} é o maior inimigo do crescimento'
                    ]
                }
            ],
            'drivers_racionais_complementares': [
                {
                    'nome': f'DRIVER DO MÉTODO VS SORTE PARA {segmento.upper()}',
                    'categoria': 'racional_complementar',
                    'gatilho_central': f'Diferença entre sistema e tentativa em {segmento}',
                    'definicao_visceral': f'Contrastar método científico com tentativa aleatória em {segmento}',
                    'roteiro_ativacao': {
                        'pergunta_abertura': f'Você está tentando ou aplicando método em {segmento}?',
                        'historia_analogia': f'Dois profissionais de {segmento} começaram juntos...',
                        'comando_acao': f'Pare de tentar e comece a aplicar método em {segmento}'
                    },
                    'frases_ancoragem': [
                        f'Método em {segmento} elimina tentativa e erro',
                        f'Sorte é para quem não tem método em {segmento}'
                    ]
                }
            ],
            'fallback_mode': True,
            'sistema_completo': True
        }

# Instância global
complete_drivers_architect = CompleteDriversArchitect()