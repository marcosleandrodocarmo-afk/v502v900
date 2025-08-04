#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Visceral Analysis Engine
Motor de análise visceral baseado no documento de integração
"""

import logging
import time
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class VisceralAnalysisEngine:
    """Motor de análise visceral com todos os componentes do documento"""
    
    def __init__(self):
        """Inicializa o motor de análise visceral"""
        self.agents = {
            'arquelogo_persuasao': {
                'name': 'ARQUEÓLOGO MESTRE DA PERSUASÃO',
                'mission': 'Escavar cada segundo, palavra e pausa para encontrar o DNA COMPLETO da conversão',
                'tools': ['Python', 'Análise cirúrgica', 'Mapeamento psicológico']
            },
            'mestre_persuasao_visceral': {
                'name': 'MESTRE DA PERSUASÃO VISCERAL',
                'mission': 'Engenharia Reversa Psicológica Profunda',
                'language': 'Direta, brutalmente honesta, carregada de tensão psicológica'
            },
            'arquiteto_pre_pitch': {
                'name': 'ARQUITETO DO PRÉ-PITCH INVISÍVEL',
                'mission': 'Orquestrar SINFONIA DE TENSÃO PSICOLÓGICA',
                'specialty': 'Sequências de instalação psicológica'
            },
            'diretor_experiencias': {
                'name': 'DIRETOR SUPREMO DE EXPERIÊNCIAS TRANSFORMADORAS',
                'mission': 'Transformar conceitos abstratos em experiências físicas inesquecíveis',
                'focus': 'PROVIs (Provas Visuais Instantâneas)'
            },
            'arquiteto_drivers': {
                'name': 'ARQUITETO DE DRIVERS MENTAIS',
                'mission': 'Criar gatilhos psicológicos como âncoras emocionais e racionais',
                'specialty': 'Sistema de ancoragem psicológica'
            }
        }
        
        logger.info("Visceral Analysis Engine inicializado com 5 agentes especializados")
    
    def generate_complete_visceral_analysis(
        self, 
        data: Dict[str, Any],
        session_id: str = None
    ) -> Dict[str, Any]:
        """Gera análise visceral completa com todos os componentes"""
        
        try:
            logger.info("🧠 Iniciando análise visceral completa...")
            
            # Salva início da análise
            salvar_etapa("analise_visceral_iniciada", {
                "data": data,
                "agents": list(self.agents.keys()),
                "timestamp": time.time()
            }, categoria="analise_completa")
            
            # Executa cada componente
            visceral_analysis = {}
            
            # 1. Análise Forense Devastadora (Arqueólogo)
            logger.info("🔍 Executando análise forense devastadora...")
            forensic_analysis = self._execute_forensic_analysis(data)
            if forensic_analysis:
                visceral_analysis['analise_forense_devastadora'] = forensic_analysis
                salvar_etapa("analise_forense", forensic_analysis, categoria="analise_completa")
            
            # 2. Engenharia Reversa Psicológica (Mestre Persuasão)
            logger.info("🧬 Executando engenharia reversa psicológica...")
            psychological_reverse = self._execute_psychological_reverse_engineering(data)
            if psychological_reverse:
                visceral_analysis['engenharia_reversa_psicologica'] = psychological_reverse
                salvar_etapa("engenharia_reversa", psychological_reverse, categoria="analise_completa")
            
            # 3. Sistema de Drivers Mentais (Arquiteto Drivers)
            logger.info("⚡ Executando sistema de drivers mentais...")
            mental_drivers_system = self._execute_mental_drivers_system(data)
            if mental_drivers_system:
                visceral_analysis['sistema_drivers_mentais'] = mental_drivers_system
                salvar_etapa("drivers_mentais", mental_drivers_system, categoria="drivers_mentais")
            
            # 4. Sistema Anti-Objeção (Especialista Psicologia)
            logger.info("🛡️ Executando sistema anti-objeção...")
            anti_objection_system = self._execute_anti_objection_system(data)
            if anti_objection_system:
                visceral_analysis['sistema_anti_objecao_completo'] = anti_objection_system
                salvar_etapa("anti_objecao_completo", anti_objection_system, categoria="anti_objecao")
            
            # 5. Pré-Pitch Invisível (Arquiteto Pré-Pitch)
            logger.info("🎭 Executando pré-pitch invisível...")
            pre_pitch_invisible = self._execute_pre_pitch_invisible(data, mental_drivers_system)
            if pre_pitch_invisible:
                visceral_analysis['pre_pitch_invisivel_completo'] = pre_pitch_invisible
                salvar_etapa("pre_pitch_completo", pre_pitch_invisible, categoria="pre_pitch")
            
            # 6. Sistema de Provas Visuais (Diretor Experiências)
            logger.info("🎯 Executando sistema de provas visuais...")
            visual_proofs_system = self._execute_visual_proofs_system(data)
            if visual_proofs_system:
                visceral_analysis['sistema_provas_visuais_completo'] = visual_proofs_system
                salvar_etapa("provas_visuais_completo", visual_proofs_system, categoria="provas_visuais")
            
            # 7. Dashboard do Avatar (Análise Profunda)
            logger.info("👤 Executando dashboard do avatar...")
            avatar_dashboard = self._execute_avatar_dashboard(data)
            if avatar_dashboard:
                visceral_analysis['dashboard_avatar_completo'] = avatar_dashboard
                salvar_etapa("avatar_dashboard", avatar_dashboard, categoria="avatar")
            
            # 8. Sistema Completo de Provas Visuais Instantâneas
            logger.info("🎯 Executando sistema completo de PROVIs...")
            provis_system = self._execute_complete_provis_system(data, ai_analysis)
            if provis_system:
                visceral_analysis['sistema_provis_completo'] = provis_system
                salvar_etapa("provis_sistema_completo", provis_system, categoria="provas_visuais")
            
            # 9. Análise Forense Devastadora Completa
            logger.info("🔍 Executando análise forense devastadora...")
            forensic_complete = self._execute_complete_forensic_analysis(data)
            if forensic_complete:
                visceral_analysis['analise_forense_completa'] = forensic_complete
                salvar_etapa("analise_forense_completa", forensic_complete, categoria="analise_completa")
            
            # Consolida análise final
            visceral_analysis['metadata_visceral'] = {
                'generated_at': datetime.now().isoformat(),
                'agents_used': list(self.agents.keys()),
                'components_generated': len(visceral_analysis),
                'analysis_type': 'visceral_complete',
                'quality_level': 'premium_visceral'
            }
            
            # Salva análise completa
            salvar_etapa("analise_visceral_completa", visceral_analysis, categoria="analise_completa")
            
            logger.info(f"✅ Análise visceral completa: {len(visceral_analysis)} componentes gerados")
            return visceral_analysis
            
        except Exception as e:
            logger.error(f"❌ Erro na análise visceral: {str(e)}")
            salvar_erro("analise_visceral", e, contexto=data)
            return self._generate_fallback_visceral_analysis(data)
    
    def _execute_forensic_analysis(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa análise forense devastadora"""
        
        try:
            prompt = f"""
Você é o ARQUEÓLOGO MESTRE DA PERSUASÃO. Sua missão é escavar cada elemento psicológico para encontrar o DNA COMPLETO da conversão.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Público: {data.get('publico', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}

Execute uma ANÁLISE FORENSE DEVASTADORA seguindo as 12 CAMADAS PROFUNDAS:

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "resumo_executivo": {{
    "veredicto_geral": "Análise de 1-10",
    "top_3_pontos_fortes": ["Ponto 1", "Ponto 2", "Ponto 3"],
    "estrategia_principal": "Estratégia identificada"
  }},
  "cronometragem_detalhada": {{
    "abertura_0_3min": "Análise da abertura",
    "educacao_conteudo": "Análise do desenvolvimento",
    "transicao_venda": "Análise da transição",
    "apresentacao_oferta": "Análise da oferta",
    "fechamento_cta": "Análise do fechamento"
  }},
  "dna_conversao": {{
    "formula_estrutural": "Fórmula extraída",
    "sequencia_gatilhos": ["Gatilho 1", "Gatilho 2", "Gatilho 3"],
    "padroes_linguagem": ["Padrão 1", "Padrão 2"],
    "timing_otimo": "Timing ideal de cada elemento"
  }},
  "metricas_objetivas": {{
    "duracao_total": "X minutos",
    "densidade_informacional": "X informações/minuto",
    "ratio_eu_voce": "X% vs X%",
    "promessas_totais": 0,
    "provas_oferecidas": 0,
    "ratio_promessa_prova": "1:X"
  }},
  "analise_quantitativa": {{
    "credibilidade_score": 85,
    "logica_vs_emocao": {{"logicos": 40, "emocionais": 60}},
    "gatilhos_cialdini": {{
      "reciprocidade": 3,
      "compromisso": 2,
      "prova_social": 5,
      "afinidade": 4,
      "autoridade": 6,
      "escassez": 2
    }},
    "intensidade_emocional": {{
      "medo": 7,
      "desejo": 8,
      "urgencia": 6,
      "aspiracao": 9
    }}
  }},
  "premissas_estabelecidas": [
    "Premissa 1 - Como estabelece",
    "Premissa 2 - Como estabelece",
    "Premissa 3 - Como estabelece"
  ],
  "sequencia_logica": {{
    "gaps_logicos": ["Gap 1", "Gap 2"],
    "silogismo_principal": "Se A, então B, então C",
    "falacias_utilizadas": ["Falácia 1", "Falácia 2"]
  }}
}}
```
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=3000)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    return json.loads(clean_response)
                except json.JSONDecodeError:
                    logger.warning("JSON inválido na análise forense")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro na análise forense: {e}")
            return None
    
    def _execute_psychological_reverse_engineering(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa engenharia reversa psicológica profunda"""
        
        try:
            prompt = f"""
Você é o MESTRE DA PERSUASÃO VISCERAL. Sua linguagem é direta, brutalmente honesta, carregada de tensão psicológica.

Realize uma ENGENHARIA REVERSA PSICOLÓGICA PROFUNDA para:

SEGMENTO: {data.get('segmento', 'Não informado')}
PRODUTO: {data.get('produto', 'Não informado')}
PÚBLICO: {data.get('publico', 'Não informado')}

Crie um DOSSIÊ CONFIDENCIAL que permita "LER A MENTE" dos leads.

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "perfil_psicologico_profundo": {{
    "nome_ficticio": "Nome representativo",
    "idade_aproximada": "Faixa etária",
    "ocupacao_situacao": "Situação de vida",
    "jornada_dor": "Resumo da jornada de dor"
  }},
  "feridas_abertas": [
    "No fundo, ele(a) teme desesperadamente...",
    "A dor mais profunda é...",
    "O que mais o(a) envergonha é...",
    "O medo secreto que nunca admite é...",
    "A ferida que nunca cicatrizou é..."
  ],
  "sonhos_proibidos": [
    "Mais do que tudo, ele(a) anseia por...",
    "O desejo secreto que nunca confessa é...",
    "O que realmente quer é...",
    "O sonho impossível é...",
    "A fantasia oculta é..."
  ],
  "demonios_internos": [
    "O pensamento que o(a) congela é...",
    "O medo paralisante é...",
    "O terror noturno é...",
    "A ansiedade constante é...",
    "O pânico secreto é..."
  ],
  "correntes_cotidiano": [
    "No dia a dia, luta constantemente com...",
    "As pequenas coisas que o(a) tiram do sério são...",
    "A frustração diária é...",
    "O que mais o(a) irrita é...",
    "A rotina que o(a) sufoca é..."
  ],
  "dialeto_alma": {{
    "frases_dores": ["Frase típica sobre dor 1", "Frase típica sobre dor 2"],
    "frases_desejos": ["Frase típica sobre desejo 1", "Frase típica sobre desejo 2"],
    "metaforas_comuns": ["Metáfora 1", "Metáfora 2"],
    "influenciadores_confianca": ["Fonte 1", "Fonte 2"],
    "fontes_desprezadas": ["Fonte desprezada 1", "Fonte desprezada 2"]
  }},
  "muralhas_desconfianca": [
    "Já tentei de tudo, nada funciona",
    "Meu caso é muito específico",
    "Não tenho tempo para implementar",
    "Preciso de mais garantias"
  ],
  "visoes_paraiso_inferno": {{
    "dia_perfeito": "Narrativa do dia perfeito pós-transformação",
    "pesadelo_recorrente": "Narrativa do pesadelo sem a solução"
  }},
  "como_usar_dossie": {{
    "angulos_copy_poderoso": ["Ângulo 1", "Ângulo 2"],
    "tipos_conteudo_atrativo": ["Tipo 1", "Tipo 2"],
    "tom_voz_ideal": "Tom recomendado",
    "gatilhos_emocionais": ["Gatilho 1", "Gatilho 2"]
  }},
  "segmentacao_psicologica": [
    {{
      "nome_segmento": "Segmento 1",
      "caracteristicas": ["Característica 1", "Característica 2"],
      "abordagem_especifica": "Como abordar este segmento"
    }}
  ]
}}
```
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=3500)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    return json.loads(clean_response)
                except json.JSONDecodeError:
                    logger.warning("JSON inválido na engenharia reversa")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro na engenharia reversa: {e}")
            return None
    
    def _execute_mental_drivers_system(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa sistema completo de drivers mentais"""
        
        try:
            prompt = f"""
Você é o ARQUITETO DE DRIVERS MENTAIS. Crie gatilhos psicológicos que funcionam como âncoras emocionais e racionais.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}
- Público: {data.get('publico', 'Não informado')}

Crie um ARSENAL COMPLETO de drivers mentais customizados baseado nos 19 DRIVERS UNIVERSAIS.

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "drivers_emocionais_primarios": [
    {{
      "nome": "DRIVER DA FERIDA EXPOSTA",
      "gatilho_central": "Emoção ou lógica core",
      "definicao_visceral": "1-2 frases que capturam a essência",
      "mecanica_psicologica": "Como funciona no cérebro",
      "momento_instalacao": "Quando plantar durante a jornada",
      "roteiro_ativacao": {{
        "pergunta_abertura": "Pergunta que expõe a ferida",
        "historia_analogia": "História que ilustra o conceito",
        "metafora_visual": "Metáfora que ancora na memória",
        "comando_acao": "Comando que direciona comportamento"
      }},
      "frases_ancoragem": [
        "Frase 1 pronta para usar",
        "Frase 2 pronta para usar",
        "Frase 3 pronta para usar"
      ],
      "prova_logica": "Dados/fatos que sustentam",
      "loop_reforco": "Como reativar em momentos posteriores"
    }}
  ],
  "drivers_racionais_complementares": [
    {{
      "nome": "DRIVER DO MÉTODO VS SORTE",
      "gatilho_central": "Diferença entre método e tentativa",
      "definicao_visceral": "Parar de tentar e começar a aplicar método",
      "roteiro_ativacao": {{
        "pergunta_abertura": "Você está tentando ou aplicando método?",
        "historia_analogia": "História específica de método vs tentativa",
        "metafora_visual": "Metáfora visual poderosa",
        "comando_acao": "Comando específico de ação"
      }},
      "frases_ancoragem": [
        "Método elimina tentativa e erro",
        "Profissionais com método crescem 10x mais rápido",
        "Sorte é para quem não tem método"
      ],
      "prova_logica": "Metodologia reduz tempo de resultado em 80%"
    }}
  ],
  "sequenciamento_estrategico": {{
    "fase_1_despertar": ["Driver 1", "Driver 2"],
    "fase_2_desejo": ["Driver 3", "Driver 4"],
    "fase_3_decisao": ["Driver 5", "Driver 6"],
    "fase_4_direcao": ["Driver 7"]
  }},
  "otimizacao_sobreposicoes": {{
    "drivers_complementares": [
      "Diagnóstico Brutal → Ambição Expandida",
      "Ambiente Vampiro → Mentor Salvador"
    ],
    "drivers_reforco": [
      "Ferida Exposta + Diagnóstico Brutal",
      "Relógio Psicológico + Custo Invisível"
    ]
  }},
  "top_7_essenciais": [
    "Diagnóstico Brutal",
    "Ambição Expandida", 
    "Relógio Psicológico",
    "Método vs Sorte",
    "Decisão Binária",
    "Ambiente Vampiro",
    "Coragem Necessária"
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
                    logger.warning("JSON inválido no sistema de drivers")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no sistema de drivers: {e}")
            return None
    
    def _execute_anti_objection_system(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa sistema completo anti-objeção"""
        
        try:
            prompt = f"""
Você é o ESPECIALISTA EM PSICOLOGIA DE VENDAS. Crie um ARSENAL PSICOLÓGICO completo para neutralizar TODAS as objeções.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}

Crie um sistema baseado nas 3 OBJEÇÕES UNIVERSAIS e 5 OBJEÇÕES OCULTAS CRÍTICAS.

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "objecoes_universais": {{
    "tempo": {{
      "objecao": "Isso não é prioridade para mim",
      "raiz_emocional": "Medo de mais responsabilidade",
      "contra_ataque": "Técnica do Cálculo da Sangria",
      "scripts": [
        "Cada mês que você adia, você perde X",
        "O problema cresce enquanto você está ocupado",
        "Esta oportunidade existe agora por razão específica"
      ],
      "drives_mentais": ["CÁLCULO DA SANGRIA", "CONSEQUÊNCIA EXPONENCIAL"]
    }},
    "dinheiro": {{
      "objecao": "Minha vida não está tão ruim que precise investir",
      "raiz_emocional": "Medo de perder dinheiro",
      "contra_ataque": "Comparação Cruel + ROI Absurdo",
      "scripts": [
        "Você gasta R$X em coisa supérflua mas hesita em investir",
        "Se conseguir apenas resultado mínimo, já pagou o investimento",
        "O que vai perder NÃO fazendo é maior que o investimento"
      ],
      "drives_mentais": ["COMPARAÇÃO CRUEL", "ROI ABSURDO"]
    }},
    "confianca": {{
      "objecao": "Me dê uma razão para acreditar",
      "raiz_emocional": "Histórico de fracassos",
      "contra_ataque": "Autoridade Técnica + Prova Social + Garantia",
      "scripts": [
        "Eu já consegui resultado específico usando exatamente isso",
        "Pessoas como você conseguiram resultado em tempo",
        "Estou tão confiante que assumo todo o risco"
      ],
      "drives_mentais": ["AUTORIDADE TÉCNICA", "PROVA SOCIAL QUALIFICADA"]
    }}
  }},
  "objecoes_ocultas_criticas": {{
    "autossuficiencia": {{
      "objecao_oculta": "Acho que consigo sozinho",
      "perfil_tipico": "Pessoas com formação superior, ego profissional",
      "raiz_emocional": "Orgulho / Medo de parecer incompetente",
      "sinais": ["Menções de tentar sozinho", "Resistência a ajuda"],
      "contra_ataque": "O Expert que Precisou de Expert",
      "scripts": [
        "Mesmo sendo autoridade, precisei de ajuda para resultado",
        "Diferença entre tentar sozinho e ter orientação é temporal"
      ]
    }},
    "sinal_fraqueza": {{
      "objecao_oculta": "Aceitar ajuda é admitir fracasso",
      "perfil_tipico": "Homens, líderes, pessoas com imagem a zelar",
      "raiz_emocional": "Medo de julgamento / Perda de status",
      "contra_ataque": "Reframe de Inteligência + Heróis Vulneráveis",
      "scripts": [
        "Pessoas inteligentes buscam atalhos",
        "Os maiores CEOs do mundo têm coaches"
      ]
    }},
    "medo_novo": {{
      "objecao_oculta": "Quando for a hora certa",
      "perfil_tipico": "Pessoas estagnadas mas confortáveis",
      "raiz_emocional": "Ansiedade sobre nova realidade",
      "contra_ataque": "Dor da Estagnação + Janela Histórica",
      "scripts": [
        "Única coisa pior que dor da mudança é dor do arrependimento",
        "Esta oportunidade existe por contexto específico"
      ]
    }}
  }},
  "tecnicas_neutralizacao": {{
    "concordar_valorizar_apresentar": {{
      "estrutura": "Você tem razão... Por isso criei...",
      "quando_usar": "Objeções lógicas válidas",
      "exemplo": "Você tem razão em ser cauteloso. Por isso criei garantia de 60 dias"
    }},
    "inversao_perspectiva": {{
      "estrutura": "Na verdade é o oposto do que você imagina...",
      "quando_usar": "Crenças limitantes",
      "exemplo": "Na verdade, pessoas que mais precisam de ajuda são as que mais resistem"
    }}
  }},
  "arsenal_emergencia": [
    "Vamos ser honestos: você vai continuar adiando até quando?",
    "A única diferença entre você e quem conseguiu é a decisão de agir",
    "Quantas oportunidades você já perdeu por pensar demais?",
    "O medo de errar está te impedindo de acertar",
    "Cada 'não' para evolução é um 'sim' para estagnação"
  ],
  "sistema_implementacao": {{
    "pre_lancamento": ["Driver 1", "Driver 2"],
    "durante_evento": ["Driver 3", "Driver 4"],
    "momento_oferta": ["Driver 5", "Driver 6"],
    "pos_oferta": ["Driver 7", "Driver 8"]
  }}
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
                    logger.warning("JSON inválido no sistema anti-objeção")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no sistema anti-objeção: {e}")
            return None
    
    def _execute_pre_pitch_invisible(self, data: Dict[str, Any], drivers_system: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Executa pré-pitch invisível completo"""
        
        try:
            drivers_info = ""
            if drivers_system:
                drivers_info = f"DRIVERS DISPONÍVEIS: {json.dumps(drivers_system, ensure_ascii=False)[:1000]}"
            
            prompt = f"""
Você é o ARQUITETO DO PRÉ-PITCH INVISÍVEL. Crie uma SINFONIA DE TENSÃO PSICOLÓGICA.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}

{drivers_info}

Crie um PRÉ-PITCH que prepare o terreno mental para que a venda seja apenas uma formalidade.

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "orquestracao_emocional": {{
    "sequencia_psicologica": [
      {{
        "fase": "QUEBRA",
        "objetivo": "Destruir a ilusão confortável",
        "duracao": "3-5 minutos",
        "intensidade": "Alta",
        "drivers_utilizados": ["Diagnóstico Brutal"],
        "resultado_esperado": "Desconforto produtivo",
        "tecnicas": ["Confronto direto", "Pergunta desconfortável"]
      }},
      {{
        "fase": "EXPOSIÇÃO",
        "objetivo": "Revelar a ferida real",
        "duracao": "4-6 minutos",
        "intensidade": "Crescente",
        "drivers_utilizados": ["Custo Invisível"],
        "resultado_esperado": "Consciência da dor",
        "tecnicas": ["Cálculo de perdas", "Visualização da dor"]
      }},
      {{
        "fase": "VISLUMBRE",
        "objetivo": "Mostrar o possível",
        "duracao": "5-7 minutos",
        "intensidade": "Esperançosa",
        "drivers_utilizados": ["Ambição Expandida"],
        "resultado_esperado": "Desejo amplificado",
        "tecnicas": ["Visualização do sucesso", "Casos de transformação"]
      }},
      {{
        "fase": "NECESSIDADE",
        "objetivo": "Tornar a mudança inevitável",
        "duracao": "3-4 minutos",
        "intensidade": "Definitiva",
        "drivers_utilizados": ["Método vs Sorte"],
        "resultado_esperado": "Necessidade de solução",
        "tecnicas": ["Caminho claro", "Mentor necessário"]
      }}
    ]
  }},
  "roteiro_completo": {{
    "abertura": {{
      "tempo": "3-5 minutos",
      "objetivo": "Quebrar padrão e despertar consciência",
      "script": "Roteiro detalhado da abertura",
      "frases_chave": ["Frase 1", "Frase 2"],
      "transicao": "Como conectar com próxima fase"
    }},
    "desenvolvimento": {{
      "tempo": "8-12 minutos",
      "objetivo": "Amplificar dor e desejo",
      "script": "Roteiro detalhado do desenvolvimento",
      "momentos_criticos": ["Momento 1", "Momento 2"],
      "escalada_emocional": "Como aumentar intensidade"
    }},
    "pre_climax": {{
      "tempo": "3-4 minutos",
      "objetivo": "Criar tensão máxima",
      "script": "Roteiro detalhado do pré-clímax",
      "ponto_virada": "Momento exato da virada",
      "preparacao_pitch": "Como preparar para oferta"
    }},
    "fechamento": {{
      "tempo": "2-3 minutos",
      "objetivo": "Transição perfeita para pitch",
      "script": "Roteiro detalhado do fechamento",
      "ponte_oferta": "Frase de transição para oferta",
      "estado_mental_ideal": "Como devem estar mentalmente"
    }}
  }},
  "variacoes_formato": {{
    "webinario": {{
      "duracao_total": "15-20 minutos",
      "adaptacoes": ["Usar chat para engajamento", "Pausas para perguntas"],
      "timing": "Últimos 20 minutos antes da oferta"
    }},
    "evento_presencial": {{
      "duracao_total": "25-35 minutos",
      "adaptacoes": ["Interação direta", "Movimentação no palco"],
      "timing": "Distribuído ao longo do evento"
    }},
    "cpl_3_aulas": {{
      "duracao_total": "10-15 minutos",
      "adaptacoes": ["Construção gradual", "Callbacks entre aulas"],
      "timing": "Final da aula 3"
    }}
  }},
  "metricas_sucesso": {{
    "indicadores_durante": [
      "Silêncio absoluto durante ativação",
      "Comentários emocionais no chat",
      "Perguntas sobre quando abre inscrições"
    ],
    "indicadores_apos": [
      "Ansiedade visível para a oferta",
      "Perguntas sobre preço/formato",
      "Comentários 'já quero comprar'"
    ]
  }}
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
                    logger.warning("JSON inválido no pré-pitch")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no pré-pitch: {e}")
            return None
    
    def _execute_visual_proofs_system(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa sistema completo de provas visuais"""
        
        try:
            prompt = f"""
Você é o DIRETOR SUPREMO DE EXPERIÊNCIAS TRANSFORMADORAS. Transforme conceitos abstratos em experiências físicas inesquecíveis.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}

Crie um ARSENAL COMPLETO de PROVIs (Provas Visuais Instantâneas).

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "arsenal_provis": [
    {{
      "nome": "PROVI #1: NOME IMPACTANTE",
      "conceito_alvo": "O que precisa ser instalado/destruído",
      "categoria": "Urgência/Crença/Objeção/Transformação",
      "prioridade": "Crítica/Alta/Média",
      "momento_ideal": "Quando executar no evento",
      "objetivo_psicologico": "Mudança mental específica",
      "experimento": "Descrição da demonstração física",
      "analogia_perfeita": "Assim como experimento → Você aplicação",
      "roteiro_completo": {{
        "setup": "Frase de introdução + preparação física",
        "execucao": "Passo 1, 2, 3 da demonstração",
        "climax": "Momento exato do AHA!",
        "bridge": "Conexão direta com a vida deles"
      }},
      "materiais": [
        "Item 1: especificação exata",
        "Item 2: onde conseguir",
        "Item 3: substitutos possíveis"
      ],
      "variacoes": {{
        "online": "Adaptação para câmera",
        "grande_publico": "Versão amplificada",
        "intimista": "Versão simplificada"
      }},
      "gestao_riscos": {{
        "pode_falhar_se": ["Situação 1", "Situação 2"],
        "plano_b": "Alternativa pronta",
        "transformar_erro": "Como usar falha a favor"
      }},
      "frases_impacto": {{
        "durante": "Frase que aumenta tensão",
        "revelacao": "Frase no momento aha",
        "ancoragem": "Frase que fica na memória"
      }}
    }}
  ],
  "categorias_provis": {{
    "destruidoras_objecao": [
      {{
        "contra": "Não tenho tempo",
        "experimentos": ["Ampulheta com dinheiro", "Celular com 47 apps"]
      }},
      {{
        "contra": "Não tenho dinheiro", 
        "experimentos": ["Calculadora de gastos invisíveis", "Cofrinho furado"]
      }},
      {{
        "contra": "Já tentei antes",
        "experimentos": ["GPS vs mapa rasgado", "Chave certa vs molho"]
      }}
    ],
    "criadoras_urgencia": [
      "Ampulheta", "Trem partindo", "Porta se fechando", "Maré subindo"
    ],
    "instaladoras_crenca": [
      "Lagarta → Borboleta", "Semente → Árvore", "Carvão → Diamante"
    ],
    "provas_metodo": [
      "Quebra-cabeça", "Ingredientes vs receita", "Orquestra com/sem maestro"
    ]
  }},
  "plano_execucao": {{
    "sequencia_otimizada": [
      "PROVI 1: Abertura impactante",
      "PROVI 2: Desenvolvimento da dor",
      "PROVI 3: Amplificação do desejo",
      "PROVI 4: Prova do método",
      "PROVI 5: Urgência final"
    ],
    "timeline_detalhado": "Cronograma de execução",
    "narrativa_conectora": "Como cada PROVI prepara o próximo",
    "metricas_sucesso": ["Reação da audiência", "Engajamento", "Conversão"]
  }},
  "kit_preparacao": {{
    "lista_materiais": ["Material 1", "Material 2", "Material 3"],
    "checklist_preparacao": ["Item 1", "Item 2", "Item 3"],
    "ensaio_recomendado": "Como ensaiar antes do evento",
    "troubleshooting": "Soluções para problemas comuns"
  }}
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
                    logger.warning("JSON inválido no sistema de provas visuais")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no sistema de provas visuais: {e}")
            return None
    
    def _execute_avatar_dashboard(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Executa dashboard completo do avatar"""
        
        try:
            prompt = f"""
Crie um DASHBOARD ARQUEOLÓGICO DO AVATAR completo baseado na análise de perfil empresarial.

CONTEXTO:
- Segmento: {data.get('segmento', 'Não informado')}
- Produto: {data.get('produto', 'Não informado')}
- Público: {data.get('publico', 'Não informado')}
- Preço: R$ {data.get('preco', 'Não informado')}

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "visao_geral": {{
    "publico_analisado": "Perfil do público",
    "distribuicao_faturamento": {{
      "acima_5_milhoes": "64%",
      "entre_1_5_milhoes": "32%", 
      "abaixo_1_milhao": "20%"
    }},
    "principais_desafios": [
      "87% presos no nível operacional",
      "92% faturamento entre R$ 1-10 milhões",
      "100% problemas com gestão de pessoas"
    ]
  }},
  "analise_dores": {{
    "top_10_dores_estruturadas": [
      {{
        "dor": "Desenvolvimento de Liderança e Gestão de Pessoas",
        "frequencia": "95%",
        "intensidade": "Alta",
        "contexto": "Dificuldade em liderar equipes"
      }},
      {{
        "dor": "Construção de Cultura Organizacional Forte",
        "frequencia": "87%",
        "intensidade": "Alta",
        "contexto": "Falta de valores claros"
      }},
      {{
        "dor": "Fortalecimento da Operação e Processos",
        "frequencia": "92%",
        "intensidade": "Muito Alta",
        "contexto": "Processos desorganizados"
      }}
    ],
    "convergencia_descobertas": {{
      "convergencia": "Gestão de Pessoas",
      "descoberta_relevante": "Cultura Organizacional",
      "gap_identificado": "Gestão Financeira"
    }}
  }},
  "desejos_motivacoes": {{
    "sonhos_profundos": [
      {{
        "desejo": "Ausência Produtiva",
        "descricao": "Negócio funcionar sem presença constante",
        "intensidade": "Muito Alta"
      }},
      {{
        "desejo": "Máquina Empresarial Perfeita",
        "descricao": "Sistemas automatizados e eficientes",
        "intensidade": "Alta"
      }},
      {{
        "desejo": "Multiplicação Acelerada",
        "descricao": "Crescimento exponencial rápido",
        "intensidade": "Alta"
      }}
    ],
    "desejos_expressos": [
      "Escalar o negócio",
      "Criar máquina de vendas",
      "Equipe trabalhando para a empresa",
      "Romper barreira de faturamento"
    ]
  }},
  "comportamento": {{
    "arquetipos_dominantes": {{
      "tecnico_aprisionado": "30%",
      "escalador_frustrado": "40%",
      "visionario_sufocado": "30%"
    }},
    "medos_paralisantes": [
      "Terror da Irrelevância",
      "Pânico da Dependência Eterna",
      "Medo da Traição",
      "Pavor do Modelo Errado"
    ],
    "objecoes_reais": [
      "Já tentei de tudo, nada funciona",
      "Meu negócio é muito específico",
      "Não tenho tempo para implementar"
    ]
  }},
  "insights_ocultos": {{
    "gatilhos_emocionais": ["Liberdade", "Controle", "Legado", "Velocidade"],
    "abordagens_impacto": [
      "Honestidade brutal",
      "Casos reais",
      "Métodos práticos",
      "Quick Wins"
    ]
  }},
  "arsenal_tatico": {{
    "estruturacao_mentoria": [
      {{
        "modulo": "Libertação do Operacional",
        "objetivo": "Sair do dia a dia operacional",
        "duracao": "30 dias"
      }},
      {{
        "modulo": "Máquina de Vendas Previsível",
        "objetivo": "Sistema de vendas automatizado",
        "duracao": "45 dias"
      }},
      {{
        "modulo": "Processos que Escalam",
        "objetivo": "Operação escalável",
        "duracao": "60 dias"
      }}
    ],
    "formatos_entrega": [
      "Lives semanais",
      "Templates prontos",
      "Simulações e role-playing",
      "Táticas rápidas de implementação"
    ]
  }},
  "linguagem_recomendada": {{
    "substituicoes": {{
      "processo_comercial": "máquina de vendas",
      "crescer_gradualmente": "romper barreiras",
      "delegar_tarefas": "time autônomo",
      "work_life_balance": "liberdade"
    }},
    "tom_ideal": "Direto, confrontador, orientado a resultados",
    "palavras_poder": ["Liberdade", "Máquina", "Sistema", "Automático", "Escalável"]
  }}
}}
```
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=3500)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    return json.loads(clean_response)
                except json.JSONDecodeError:
                    logger.warning("JSON inválido no dashboard do avatar")
            
            return None
            
        except Exception as e:
            logger.error(f"Erro no dashboard do avatar: {e}")
            return None
    
    def _generate_fallback_visceral_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera análise visceral de fallback"""
        
        segmento = data.get('segmento', 'negócios')
        
        return {
            'analise_forense_devastadora': {
                'resumo_executivo': {
                    'veredicto_geral': f'Análise de {segmento} com potencial alto',
                    'top_3_pontos_fortes': [
                        f'Mercado de {segmento} em crescimento',
                        'Demanda por soluções especializadas',
                        'Oportunidade de diferenciação'
                    ],
                    'estrategia_principal': f'Posicionamento premium em {segmento}'
                }
            },
            'engenharia_reversa_psicologica': {
                'perfil_psicologico_profundo': {
                    'nome_ficticio': f'Profissional {segmento} Brasileiro',
                    'idade_aproximada': '30-45 anos',
                    'ocupacao_situacao': f'Empreendedor em {segmento}',
                    'jornada_dor': f'Luta para crescer em {segmento}'
                },
                'feridas_abertas': [
                    f'Trabalhar muito em {segmento} sem crescer proporcionalmente',
                    'Sentir-se sempre atrás da concorrência',
                    'Ver outros crescendo mais rápido',
                    'Não conseguir se desconectar do trabalho'
                ]
            },
            'fallback_mode': True,
            'recommendation': 'Configure APIs para análise visceral completa'
        }

# Instância global
visceral_analysis_engine = VisceralAnalysisEngine()