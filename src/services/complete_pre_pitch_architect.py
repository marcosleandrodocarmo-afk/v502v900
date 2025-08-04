#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Complete Pre-Pitch Architect
Arquiteto Completo do Pré-Pitch Invisível baseado no documento
"""

import time
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class CompletePrePitchArchitect:
    """Arquiteto Completo do Pré-Pitch Invisível - Sinfonia de Tensão Psicológica"""
    
    def __init__(self):
        """Inicializa o arquiteto completo de pré-pitch"""
        self.psychological_phases = self._load_psychological_phases()
        self.format_templates = self._load_format_templates()
        
        logger.info("Complete Pre-Pitch Architect inicializado")
    
    def _load_psychological_phases(self) -> Dict[str, Dict[str, Any]]:
        """Carrega as fases psicológicas do documento"""
        return {
            'quebra': {
                'objetivo': 'Destruir a ilusão confortável',
                'duracao': '3-5 minutos',
                'intensidade': 'Alta',
                'drivers_ideais': ['Diagnóstico Brutal', 'Ferida Exposta'],
                'resultado_esperado': 'Desconforto produtivo',
                'tecnicas': ['Confronto direto', 'Pergunta desconfortável', 'Estatística chocante']
            },
            'exposicao': {
                'objetivo': 'Revelar a ferida real',
                'duracao': '4-6 minutos',
                'intensidade': 'Crescente',
                'drivers_ideais': ['Custo Invisível', 'Ambiente Vampiro'],
                'resultado_esperado': 'Consciência da dor',
                'tecnicas': ['Cálculo de perdas', 'Visualização da dor', 'Comparação cruel']
            },
            'indignacao': {
                'objetivo': 'Criar revolta produtiva',
                'duracao': '3-4 minutos',
                'intensidade': 'Máxima',
                'drivers_ideais': ['Relógio Psicológico', 'Inveja Produtiva'],
                'resultado_esperado': 'Urgência de mudança',
                'tecnicas': ['Urgência temporal', 'Comparação social', 'Consequências futuras']
            },
            'vislumbre': {
                'objetivo': 'Mostrar o possível',
                'duracao': '5-7 minutos',
                'intensidade': 'Esperançosa',
                'drivers_ideais': ['Ambição Expandida', 'Troféu Secreto'],
                'resultado_esperado': 'Desejo amplificado',
                'tecnicas': ['Visualização do sucesso', 'Casos de transformação', 'Possibilidades expandidas']
            },
            'tensao': {
                'objetivo': 'Amplificar o gap',
                'duracao': '2-3 minutos',
                'intensidade': 'Crescente',
                'drivers_ideais': ['Identidade Aprisionada', 'Oportunidade Oculta'],
                'resultado_esperado': 'Tensão máxima',
                'tecnicas': ['Gap atual vs ideal', 'Identidade limitante', 'Oportunidade única']
            },
            'necessidade': {
                'objetivo': 'Tornar a mudança inevitável',
                'duracao': '3-4 minutos',
                'intensidade': 'Definitiva',
                'drivers_ideais': ['Método vs Sorte', 'Mentor Salvador'],
                'resultado_esperado': 'Necessidade de solução',
                'tecnicas': ['Caminho claro', 'Mentor necessário', 'Método vs caos']
            }
        }
    
    def _load_format_templates(self) -> Dict[str, Dict[str, Any]]:
        """Carrega templates por formato do documento"""
        return {
            'webinario': {
                'duracao_total': '15-20 minutos',
                'posicionamento': 'Últimos 20 minutos antes da oferta',
                'foco': 'Urgência e método',
                'velocidade': 'Rápida, dinâmica',
                'adaptacoes': ['Usar chat para engajamento', 'Pausas para perguntas retóricas', 'Slides de apoio visual'],
                'distribuicao_fases': {
                    'quebra': '3 min',
                    'exposicao': '4 min',
                    'indignacao': '3 min',
                    'vislumbre': '5 min',
                    'tensao': '2 min',
                    'necessidade': '3 min'
                }
            },
            'evento_presencial': {
                'duracao_total': '25-35 minutos',
                'posicionamento': 'Distribuído ao longo do evento',
                'foco': 'Transformação profunda',
                'velocidade': 'Construção gradual',
                'adaptacoes': ['Interação direta com audiência', 'Movimentação no palco', 'Provas visuais físicas'],
                'distribuicao_fases': {
                    'quebra': '5 min',
                    'exposicao': '6 min',
                    'indignacao': '4 min',
                    'vislumbre': '7 min',
                    'tensao': '3 min',
                    'necessidade': '4 min'
                }
            },
            'cpl_3_aulas': {
                'duracao_total': '10-15 minutos',
                'posicionamento': 'Final da aula 3',
                'foco': 'Consolidação e decisão',
                'velocidade': 'Crescente',
                'adaptacoes': ['Construção gradual ao longo das aulas', 'Callbacks entre aulas', 'Intensificação na aula 3'],
                'distribuicao_fases': {
                    'quebra': '2 min',
                    'exposicao': '3 min',
                    'indignacao': '2 min',
                    'vislumbre': '4 min',
                    'tensao': '2 min',
                    'necessidade': '2 min'
                }
            },
            'lives_aquecimento': {
                'duracao_total': '5-8 minutos por live',
                'posicionamento': 'Distribuído nas lives',
                'foco': 'Preparação subliminar',
                'velocidade': 'Sutil',
                'adaptacoes': ['Sementes em cada live', 'Preparação subliminar', 'Crescimento de intensidade'],
                'distribuicao_fases': {
                    'quebra': '1 min',
                    'exposicao': '2 min',
                    'vislumbre': '2 min',
                    'necessidade': '1 min'
                }
            }
        }
    
    def generate_complete_pre_pitch_system(
        self, 
        drivers_list: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any],
        format_type: str = 'webinario'
    ) -> Dict[str, Any]:
        """Gera sistema completo de pré-pitch baseado no documento"""
        
        try:
            logger.info(f"🎭 Gerando sistema completo de pré-pitch para {format_type}...")
            
            # Salva dados de entrada
            salvar_etapa("pre_pitch_completo_entrada", {
                "drivers_list": drivers_list,
                "avatar_data": avatar_data,
                "context_data": context_data,
                "format_type": format_type
            }, categoria="pre_pitch")
            
            # ETAPA 1: Análise e Seleção de Drivers
            selected_drivers = self._select_optimal_drivers_for_pre_pitch(drivers_list, avatar_data)
            salvar_etapa("drivers_selecionados_pre_pitch", selected_drivers, categoria="pre_pitch")
            
            # ETAPA 2: Criação do Roteiro Completo
            complete_script = self._create_complete_script(selected_drivers, avatar_data, context_data, format_type)
            salvar_etapa("roteiro_completo_pre_pitch", complete_script, categoria="pre_pitch")
            
            # ETAPA 3: Adaptação por Formato
            format_adaptation = self._adapt_for_format(complete_script, format_type, context_data)
            salvar_etapa("adaptacao_formato", format_adaptation, categoria="pre_pitch")
            
            complete_system = {
                'orquestracao_emocional': {
                    'sequencia_psicologica': self._create_psychological_sequence(selected_drivers, format_type),
                    'escalada_emocional': self._create_emotional_escalation(),
                    'pontos_criticos': self._identify_critical_points(),
                    'transicoes': self._create_phase_transitions()
                },
                'roteiro_completo': complete_script,
                'adaptacao_formato': format_adaptation,
                'variacoes_formato': self._create_all_format_variations(complete_script, context_data),
                'metricas_sucesso': self._create_success_metrics(),
                'templates_prontos': self._create_ready_templates(context_data),
                'elementos_avancados': self._create_advanced_elements(),
                'drivers_utilizados': [d.get('nome', 'Driver') for d in selected_drivers],
                'metadata_completo': {
                    'format_type': format_type,
                    'total_drivers': len(selected_drivers),
                    'duracao_estimada': self.format_templates[format_type]['duracao_total'],
                    'generated_at': time.time(),
                    'sistema_completo': True
                }
            }
            
            # Salva sistema completo
            salvar_etapa("sistema_pre_pitch_completo", complete_system, categoria="pre_pitch")
            
            logger.info("✅ Sistema completo de pré-pitch gerado")
            return complete_system
            
        except Exception as e:
            logger.error(f"❌ Erro no sistema completo de pré-pitch: {e}")
            salvar_erro("sistema_pre_pitch", e, contexto=context_data)
            return self._generate_fallback_complete_system(context_data, format_type)
    
    def _select_optimal_drivers_for_pre_pitch(
        self, 
        drivers_list: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """ETAPA 1: Seleciona 5-7 drivers mais poderosos para pré-pitch"""
        
        # Drivers essenciais para pré-pitch baseado no documento
        essential_drivers = [
            'Diagnóstico Brutal', 'Custo Invisível', 'Ambição Expandida',
            'Relógio Psicológico', 'Método vs Sorte', 'Mentor Salvador', 'Decisão Binária'
        ]
        
        selected = []
        
        # Seleciona drivers essenciais disponíveis
        for driver in drivers_list:
            driver_name = driver.get('nome', '')
            if any(essential in driver_name for essential in essential_drivers):
                selected.append(driver)
        
        # Se não tem drivers suficientes, cria drivers básicos
        if len(selected) < 5:
            selected.extend(self._create_basic_drivers_for_pre_pitch(avatar_data))
        
        return selected[:7]  # Máximo 7 drivers
    
    def _create_complete_script(
        self, 
        selected_drivers: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any],
        format_type: str
    ) -> Dict[str, Any]:
        """ETAPA 2: Cria roteiro completo usando IA"""
        
        try:
            format_info = self.format_templates.get(format_type, self.format_templates['webinario'])
            
            prompt = f"""
Você é o ARQUITETO DO PRÉ-PITCH INVISÍVEL. Crie uma SINFONIA DE TENSÃO PSICOLÓGICA.

CONTEXTO:
- Segmento: {context_data.get('segmento', 'Não informado')}
- Produto: {context_data.get('produto', 'Não informado')}
- Preço: R$ {context_data.get('preco', 'Não informado')}
- Formato: {format_type}
- Duração Total: {format_info['duracao_total']}

DRIVERS SELECIONADOS:
{json.dumps(selected_drivers, ensure_ascii=False, indent=2)[:2000]}

AVATAR:
{json.dumps(avatar_data, ensure_ascii=False, indent=2)[:1500]}

Crie PRÉ-PITCH seguindo EXATAMENTE a estrutura do documento:

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "contexto": {{
    "formato": "{format_type}",
    "duracao": "{format_info['duracao_total']}",
    "momento": "{format_info['posicionamento']}",
    "estado_mental_esperado": "Como chegam mentalmente"
  }},
  "objetivo_especifico": "Transformação mental que queremos ao final",
  "roteiro_completo": {{
    "abertura": {{
      "tempo": "{format_info['distribuicao_fases']['quebra']}",
      "driver": "Nome do driver usado",
      "instalacao": "Como introduzir o driver",
      "narrativa": "História/analogia específica de 150+ palavras",
      "pergunta_ancora": "Pergunta que fica ecoando",
      "objetivo": "Quebrar padrão e despertar consciência",
      "script": "Roteiro detalhado da abertura",
      "frases_chave": ["Frase 1", "Frase 2"],
      "transicao": "Como conectar com próxima fase"
    }},
    "desenvolvimento": {{
      "tempo": "{format_info['distribuicao_fases']['exposicao']} + {format_info['distribuicao_fases']['indignacao']}",
      "drivers": ["Driver 1", "Driver 2"],
      "objetivo": "Amplificar dor e criar indignação",
      "script": "Roteiro detalhado do desenvolvimento",
      "momentos_criticos": ["Momento 1", "Momento 2"],
      "escalada_emocional": "Como aumentar intensidade gradualmente"
    }},
    "vislumbre": {{
      "tempo": "{format_info['distribuicao_fases']['vislumbre']}",
      "driver": "Ambição Expandida ou similar",
      "objetivo": "Mostrar o possível e amplificar desejo",
      "script": "Roteiro detalhado do vislumbre",
      "visualizacao": "Como fazer eles visualizarem o sucesso",
      "casos_transformacao": ["Caso 1", "Caso 2"]
    }},
    "transicao_logica": {{
      "tempo": "1-2 minutos",
      "ponte": "Frase que conecta emoção com lógica",
      "objetivo": "Preparar cérebro racional",
      "script": "Roteiro da transição"
    }},
    "prova_logica": {{
      "tempo": "30% do tempo total",
      "numeros": "Estatísticas/dados irrefutáveis",
      "calculo": "ROI demonstrado passo a passo",
      "cases": "Exemplos com métricas específicas",
      "demonstracao": "Passo a passo visual",
      "objetivo": "Validar decisão emocional com lógica"
    }},
    "fechamento_pre_pitch": {{
      "tempo": "{format_info['distribuicao_fases']['necessidade']}",
      "driver_final": "Urgência/Decisão",
      "transicao": "Como levar ao pitch sem parecer vendedor",
      "estado_final": "Como devem estar mentalmente",
      "ponte_oferta": "Frase de transição para oferta"
    }}
  }},
  "scripts_especificos": {{
    "momentos_cruciais": [
      "Script para momento de maior tensão",
      "Script para revelação principal",
      "Script para transição emocional"
    ],
    "frases_impacto": [
      "Frase que marca abertura",
      "Frase que amplifica dor",
      "Frase que cria urgência"
    ]
  }},
  "elementos_tensao": {{
    "como_manter_engajamento": "Técnicas para manter atenção alta",
    "recursos_quebrar_monotonia": ["Recurso 1", "Recurso 2"],
    "gestao_energia_audiencia": "Como gerenciar energia coletiva"
  }},
  "metricas_sucesso_durante": [
    "Silêncio absoluto durante ativação",
    "Comentários emocionais no chat",
    "Perguntas sobre quando abre inscrições",
    "Concordância física (acenar cabeça)"
  ],
  "metricas_sucesso_apos": [
    "Ansiedade visível para a oferta",
    "Perguntas sobre preço/formato",
    "Comentários 'já quero comprar'",
    "Objeções minimizadas"
  ]
}}
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
                    return json.loads(clean_response)
                except json.JSONDecodeError:
                    logger.warning("JSON inválido no roteiro completo")
            
            return self._create_basic_complete_script(context_data, format_type)
            
        except Exception as e:
            logger.error(f"Erro no roteiro completo: {e}")
            return self._create_basic_complete_script(context_data, format_type)
    
    def _create_psychological_sequence(self, selected_drivers: List[Dict[str, Any]], format_type: str) -> List[Dict[str, Any]]:
        """Cria sequência psicológica QUEBRA → EXPOSIÇÃO → INDIGNAÇÃO → VISLUMBRE → TENSÃO → NECESSIDADE"""
        
        format_info = self.format_templates.get(format_type, self.format_templates['webinario'])
        sequence = []
        
        for phase_name, phase_data in self.psychological_phases.items():
            # Mapeia drivers para cada fase
            phase_drivers = []
            for driver in selected_drivers:
                driver_name = driver.get('nome', '')
                if any(ideal_driver in driver_name for ideal_driver in phase_data['drivers_ideais']):
                    phase_drivers.append(driver['nome'])
            
            if not phase_drivers:
                phase_drivers = [selected_drivers[0]['nome']] if selected_drivers else ['Driver Padrão']
            
            sequence.append({
                'fase': phase_name.upper(),
                'objetivo': phase_data['objetivo'],
                'duracao': format_info['distribuicao_fases'].get(phase_name, phase_data['duracao']),
                'intensidade': phase_data['intensidade'],
                'drivers_utilizados': phase_drivers[:2],  # Máximo 2 drivers por fase
                'resultado_esperado': phase_data['resultado_esperado'],
                'tecnicas': phase_data['tecnicas']
            })
        
        return sequence
    
    def _create_emotional_escalation(self) -> Dict[str, Any]:
        """Cria escalada emocional"""
        
        return {
            'curva_intensidade': [
                {'fase': 'QUEBRA', 'intensidade': 'Alta', 'nivel': 8},
                {'fase': 'EXPOSIÇÃO', 'intensidade': 'Crescente', 'nivel': 7},
                {'fase': 'INDIGNAÇÃO', 'intensidade': 'Máxima', 'nivel': 10},
                {'fase': 'VISLUMBRE', 'intensidade': 'Esperançosa', 'nivel': 6},
                {'fase': 'TENSÃO', 'intensidade': 'Crescente', 'nivel': 9},
                {'fase': 'NECESSIDADE', 'intensidade': 'Definitiva', 'nivel': 8}
            ],
            'pontos_pico': ['INDIGNAÇÃO', 'TENSÃO'],
            'momentos_alivio': ['VISLUMBRE'],
            'crescimento_geral': 'Montanha-russa emocional com picos estratégicos'
        }
    
    def _identify_critical_points(self) -> List[Dict[str, Any]]:
        """Identifica pontos críticos do pré-pitch"""
        
        return [
            {
                'momento': 'Primeira quebra de padrão',
                'fase': 'QUEBRA',
                'risco': 'Perda de audiência se muito agressivo',
                'oportunidade': 'Captura total da atenção',
                'gestao': 'Monitorar reações e ajustar intensidade'
            },
            {
                'momento': 'Pico de indignação',
                'fase': 'INDIGNAÇÃO',
                'risco': 'Resistência se exagerar',
                'oportunidade': 'Máximo impacto emocional',
                'gestao': 'Balancear confronto com empatia'
            },
            {
                'momento': 'Transição para lógica',
                'fase': 'TRANSIÇÃO',
                'risco': 'Perda de momentum emocional',
                'oportunidade': 'Validação racional da decisão',
                'gestao': 'Ponte suave mas firme'
            },
            {
                'momento': 'Fechamento pré-pitch',
                'fase': 'NECESSIDADE',
                'risco': 'Antecipação excessiva da oferta',
                'oportunidade': 'Estado mental ideal para pitch',
                'gestao': 'Criar expectativa sem revelar oferta'
            }
        ]
    
    def _create_phase_transitions(self) -> List[Dict[str, Any]]:
        """Cria transições entre fases"""
        
        return [
            {
                'de': 'QUEBRA',
                'para': 'EXPOSIÇÃO',
                'script': 'Eu sei que isso dói ouvir... Mas sabe o que dói mais?',
                'tempo': '15-30 segundos',
                'tecnica': 'Ponte emocional que aprofunda'
            },
            {
                'de': 'EXPOSIÇÃO',
                'para': 'INDIGNAÇÃO',
                'script': 'E o pior de tudo é que isso não precisa ser assim...',
                'tempo': '15-30 segundos',
                'tecnica': 'Transformar dor em revolta'
            },
            {
                'de': 'INDIGNAÇÃO',
                'para': 'VISLUMBRE',
                'script': 'Mas calma, não vim aqui só para abrir feridas...',
                'tempo': '15-30 segundos',
                'tecnica': 'Alívio e esperança'
            },
            {
                'de': 'VISLUMBRE',
                'para': 'TENSÃO',
                'script': 'Agora você vê a diferença entre onde está e onde poderia estar...',
                'tempo': '15-30 segundos',
                'tecnica': 'Amplificar gap'
            },
            {
                'de': 'TENSÃO',
                'para': 'NECESSIDADE',
                'script': 'A pergunta não é SE você vai mudar, é COMO...',
                'tempo': '15-30 segundos',
                'tecnica': 'Inevitabilidade da mudança'
            },
            {
                'de': 'NECESSIDADE',
                'para': 'LÓGICA',
                'script': 'Eu sei que você está sentindo isso agora... Mas seu cérebro racional está gritando: "Será que funciona mesmo?" Então deixa eu te mostrar os números...',
                'tempo': '30-45 segundos',
                'tecnica': 'Ponte para validação racional'
            }
        ]
    
    def _adapt_for_format(self, complete_script: Dict[str, Any], format_type: str, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """ETAPA 3: Adapta para formato específico"""
        
        format_info = self.format_templates.get(format_type, self.format_templates['webinario'])
        
        return {
            'formato': format_type,
            'duracao_total': format_info['duracao_total'],
            'posicionamento': format_info['posicionamento'],
            'foco_principal': format_info['foco'],
            'velocidade_recomendada': format_info['velocidade'],
            'adaptacoes_especificas': format_info['adaptacoes'],
            'distribuicao_tempo': format_info['distribuicao_fases'],
            'recursos_especificos': self._get_format_specific_resources(format_type),
            'consideracoes_tecnicas': self._get_technical_considerations(format_type)
        }
    
    def _create_all_format_variations(self, base_script: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria variações para todos os formatos"""
        
        variations = {}
        
        for format_name, format_info in self.format_templates.items():
            variations[format_name] = {
                'duracao_total': format_info['duracao_total'],
                'adaptacoes': format_info['adaptacoes'],
                'timing': format_info['posicionamento'],
                'foco': format_info['foco'],
                'velocidade': format_info['velocidade'],
                'script_adaptado': self._adapt_script_for_format(base_script, format_name)
            }
        
        return variations
    
    def _create_success_metrics(self) -> Dict[str, Any]:
        """Cria métricas de sucesso baseadas no documento"""
        
        return {
            'indicadores_durante': [
                'Silêncio absoluto durante ativação',
                'Comentários emocionais no chat',
                'Perguntas sobre quando abre inscrições',
                'Concordância física (acenar cabeça)',
                'Aumento de engajamento',
                'Diminuição de questionamentos'
            ],
            'indicadores_apos': [
                'Ansiedade visível para a oferta',
                'Perguntas sobre preço/formato',
                'Comentários "já quero comprar"',
                'Objeções minimizadas',
                'Pedidos para acelerar oferta',
                'Validação social entre participantes'
            ],
            'sinais_resistencia': [
                'Questionamentos técnicos excessivos',
                'Mudança de assunto',
                'Objeções imediatas',
                'Linguagem corporal fechada',
                'Saída de participantes',
                'Comentários negativos'
            ],
            'metricas_conversao': {
                'engajamento': 'Tempo de atenção por fase',
                'emocional': 'Reações emocionais geradas',
                'comportamental': 'Ações tomadas após ativação',
                'conversao': 'Taxa de conversão pós-pré-pitch'
            }
        }
    
    def _create_ready_templates(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria templates prontos baseados no documento"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'template_1_abertura_padrao': {
                'script': f'Deixa eu te fazer uma pergunta sobre {segmento}... [pergunta específica]',
                'uso': 'Abertura universal',
                'adaptacoes': ['Online', 'Presencial', 'Intimista']
            },
            'template_2_transicao_emocao_logica': {
                'script': 'Eu sei que você está sentindo isso agora... Mas seu cérebro racional precisa de provas...',
                'uso': 'Transição da fase emocional para lógica',
                'adaptacoes': ['Webinar', 'Evento', 'CPL']
            },
            'template_3_fechamento_pre_pitch': {
                'script': f'Agora você tem duas escolhas em {segmento}: continuar como está ou...',
                'uso': 'Fechamento antes do pitch',
                'adaptacoes': ['Todos os formatos']
            }
        }
    
    def _create_advanced_elements(self) -> Dict[str, Any]:
        """Cria elementos avançados do documento"""
        
        return {
            'tecnicas_amplificacao': {
                'contrastes_extremos': 'Usar opostos para amplificar diferenças',
                'provas_sociais_estrategicas': 'Casos específicos no momento certo',
                'urgencia_crescente': 'Escalada temporal progressiva'
            },
            'sinais_sucesso': {
                'durante_pre_pitch': [
                    'Silêncio absoluto durante ativação',
                    'Perguntas no chat sobre próximos passos',
                    'Comentários emocionais',
                    'Concordância física visível'
                ],
                'apos_pre_pitch': [
                    'Ansiedade visível para a oferta',
                    'Perguntas sobre preço/formato',
                    'Comentários "já quero comprar"',
                    'Objeções minimizadas'
                ]
            },
            'gestao_riscos': {
                'intensidade_excessiva': 'Como reduzir se audiência resistir',
                'perda_atencao': 'Como recuperar engajamento',
                'objecoes_imprevistas': 'Como lidar com resistência inesperada'
            }
        }
    
    def _create_basic_drivers_for_pre_pitch(self, avatar_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Cria drivers básicos para pré-pitch"""
        
        return [
            {
                'nome': 'DIAGNÓSTICO BRUTAL BÁSICO',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Verdade dolorosa sobre situação atual',
                'definicao_visceral': 'Confrontar com realidade sem filtros'
            },
            {
                'nome': 'AMBIÇÃO EXPANDIDA BÁSICA',
                'categoria': 'emocional_primario',
                'gatilho_central': 'Visão ampliada do possível',
                'definicao_visceral': 'Expandir limites do que acreditam ser possível'
            },
            {
                'nome': 'MÉTODO VS SORTE BÁSICO',
                'categoria': 'racional_complementar',
                'gatilho_central': 'Diferença entre sistema e tentativa',
                'definicao_visceral': 'Contrastar método científico com tentativa aleatória'
            }
        ]
    
    def _create_basic_complete_script(self, context_data: Dict[str, Any], format_type: str) -> Dict[str, Any]:
        """Cria roteiro básico completo"""
        
        segmento = context_data.get('segmento', 'negócios')
        format_info = self.format_templates.get(format_type, self.format_templates['webinario'])
        
        return {
            'contexto': {
                'formato': format_type,
                'duracao': format_info['duracao_total'],
                'momento': format_info['posicionamento']
            },
            'objetivo_especifico': f'Preparar audiência de {segmento} para aceitar oferta',
            'roteiro_completo': {
                'abertura': {
                    'tempo': '3-5 minutos',
                    'objetivo': 'Quebrar padrão e despertar consciência',
                    'script': f'Deixa eu te fazer uma pergunta sobre {segmento}... Há quanto tempo você está no mesmo nível?',
                    'frases_chave': [f'A verdade sobre {segmento} que ninguém te conta'],
                    'transicao': 'E sabe por que isso acontece?'
                },
                'desenvolvimento': {
                    'tempo': '8-12 minutos',
                    'objetivo': 'Amplificar dor e criar urgência',
                    'script': f'Cada dia que passa sem otimizar {segmento} é dinheiro saindo do seu bolso...',
                    'momentos_criticos': ['Cálculo da perda financeira', 'Comparação com concorrentes']
                },
                'fechamento_pre_pitch': {
                    'tempo': '2-3 minutos',
                    'objetivo': 'Transição perfeita para pitch',
                    'script': f'Agora você tem duas escolhas em {segmento}...',
                    'ponte_oferta': 'Eu vou te mostrar exatamente como sair dessa situação...'
                }
            },
            'fallback_mode': True
        }
    
    def _get_format_specific_resources(self, format_type: str) -> List[str]:
        """Obtém recursos específicos por formato"""
        
        resources_map = {
            'webinario': ['Chat interativo', 'Slides de apoio', 'Polls em tempo real', 'Breakout rooms'],
            'evento_presencial': ['Microfone sem fio', 'Projetor', 'Flipchart', 'Props físicos'],
            'cpl_3_aulas': ['Plataforma de ensino', 'Materiais downloadáveis', 'Fórum de discussão'],
            'lives_aquecimento': ['Streaming estável', 'Moderação de chat', 'Notificações push']
        }
        
        return resources_map.get(format_type, ['Recursos básicos'])
    
    def _get_technical_considerations(self, format_type: str) -> List[str]:
        """Obtém considerações técnicas por formato"""
        
        considerations_map = {
            'webinario': ['Qualidade de áudio', 'Estabilidade de internet', 'Backup de slides'],
            'evento_presencial': ['Acústica do local', 'Iluminação adequada', 'Posicionamento do palco'],
            'cpl_3_aulas': ['Qualidade de gravação', 'Edição profissional', 'Legendas'],
            'lives_aquecimento': ['Horário de pico', 'Notificações antecipadas', 'Gravação para replay']
        }
        
        return considerations_map.get(format_type, ['Considerações básicas'])
    
    def _adapt_script_for_format(self, base_script: Dict[str, Any], format_name: str) -> Dict[str, Any]:
        """Adapta script para formato específico"""
        
        format_info = self.format_templates.get(format_name, self.format_templates['webinario'])
        
        return {
            'duracao_adaptada': format_info['duracao_total'],
            'velocidade': format_info['velocidade'],
            'adaptacoes_aplicadas': format_info['adaptacoes'],
            'script_principal': f"Adaptado para {format_name} com foco em {format_info['foco']}"
        }
    
    def _generate_fallback_complete_system(self, context_data: Dict[str, Any], format_type: str) -> Dict[str, Any]:
        """Gera sistema completo de fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'orquestracao_emocional': {
                'sequencia_psicologica': [
                    {
                        'fase': 'QUEBRA',
                        'objetivo': 'Quebrar padrão',
                        'duracao': '3-5 minutos',
                        'drivers_utilizados': ['Diagnóstico Brutal']
                    },
                    {
                        'fase': 'VISLUMBRE',
                        'objetivo': 'Mostrar possibilidades',
                        'duracao': '5-7 minutos',
                        'drivers_utilizados': ['Ambição Expandida']
                    },
                    {
                        'fase': 'NECESSIDADE',
                        'objetivo': 'Criar necessidade',
                        'duracao': '3-4 minutos',
                        'drivers_utilizados': ['Método vs Sorte']
                    }
                ]
            },
            'roteiro_completo': self._create_basic_complete_script(context_data, format_type),
            'variacoes_formato': self.format_templates,
            'fallback_mode': True,
            'sistema_completo': True
        }

# Instância global
complete_pre_pitch_architect = CompletePrePitchArchitect()