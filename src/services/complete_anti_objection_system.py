#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Complete Anti-Objection System
Sistema Completo de Engenharia Psicológica Anti-Objeção baseado no documento
"""

import time
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class CompleteAntiObjectionSystem:
    """Sistema Completo de Engenharia Psicológica Anti-Objeção"""
    
    def __init__(self):
        """Inicializa o sistema completo anti-objeção"""
        self.universal_objections = self._load_3_universal_objections()
        self.hidden_objections = self._load_5_hidden_objections()
        self.neutralization_techniques = self._load_neutralization_techniques()
        
        logger.info("Complete Anti-Objection System inicializado")
    
    def _load_3_universal_objections(self) -> Dict[str, Dict[str, Any]]:
        """Carrega as 3 objeções universais do documento"""
        return {
            'tempo': {
                'objecao': 'Isso não é prioridade para mim',
                'raiz_emocional': 'Medo de mais responsabilidade / Falta de clareza sobre importância',
                'contra_ataque': 'Técnica do Cálculo da Sangria + Consequência Exponencial',
                'drives_mentais': ['CÁLCULO DA SANGRIA', 'CONSEQUÊNCIA EXPONENCIAL'],
                'scripts': [
                    'Cada [período] que você adia resolver [problema], você está perdendo [quantia específica]',
                    'O problema não para de crescer enquanto você está ocupado com outras coisas',
                    'Esta oportunidade existe agora por [razão específica], depois pode não existir mais'
                ]
            },
            'dinheiro': {
                'objecao': 'Minha vida não está tão ruim que precise investir',
                'raiz_emocional': 'Medo de perder dinheiro / Prioridades desalinhadas / Não vê valor',
                'contra_ataque': 'Comparação Cruel + ROI Absurdo + Custo de Oportunidade',
                'drives_mentais': ['COMPARAÇÃO CRUEL', 'ROI ABSURDO'],
                'scripts': [
                    'Você gasta R$X em [coisa supérflua] mas hesita em investir [valor] em algo que muda sua vida',
                    'Se você conseguir apenas [resultado mínimo], já pagou o investimento [X] vezes',
                    'O que você vai perder NÃO fazendo isso é muito maior que o investimento'
                ]
            },
            'confianca': {
                'objecao': 'Me dê uma razão para acreditar (em você/produto/provas/mim mesmo)',
                'raiz_emocional': 'Histórico de fracassos / Medo de mais uma decepção / Baixa autoestima',
                'contra_ataque': 'Autoridade Técnica + Prova Social Qualificada + Garantia Agressiva',
                'drives_mentais': ['AUTORIDADE TÉCNICA INQUESTIONÁVEL', 'PROVA SOCIAL QUALIFICADA'],
                'scripts': [
                    'Eu já [credencial específica] e consegui [resultado específico] usando exatamente isso',
                    'Pessoas exatamente como você conseguiram [resultado] em [tempo] seguindo este método',
                    'Estou tão confiante que assumo todo o risco: [garantia específica]'
                ]
            }
        }
    
    def _load_5_hidden_objections(self) -> Dict[str, Dict[str, Any]]:
        """Carrega as 5 objeções ocultas críticas do documento"""
        return {
            'autossuficiencia': {
                'objecao_oculta': 'Acho que consigo sozinho',
                'perfil_tipico': 'Pessoas com formação superior, experiência na área, ego profissional',
                'raiz_emocional': 'Orgulho / Medo de parecer incompetente',
                'sinais': ['Menções de "tentar sozinho"', 'Resistência a ajuda', 'Linguagem técnica excessiva'],
                'contra_ataque': 'O Expert que Precisou de Expert + Aceleração vs Tentativa',
                'scripts': [
                    'Mesmo sendo [autoridade], precisei de ajuda para [resultado específico]',
                    'A diferença entre tentar sozinho e ter orientação é [comparação temporal/financeira]'
                ]
            },
            'sinal_fraqueza': {
                'objecao_oculta': 'Aceitar ajuda é admitir fracasso',
                'perfil_tipico': 'Homens, líderes, pessoas com imagem a zelar',
                'raiz_emocional': 'Medo de julgamento / Perda de status / Humilhação',
                'sinais': ['Minimização de problemas', '"Está tudo bem"', 'Resistência a expor vulnerabilidade'],
                'contra_ataque': 'Reframe de Inteligência + Histórias de Heróis Vulneráveis',
                'scripts': [
                    'Pessoas inteligentes buscam atalhos. Pessoas burras insistem no caminho difícil',
                    'Os maiores CEOs do mundo têm coaches. Coincidência?'
                ]
            },
            'medo_novo': {
                'objecao_oculta': 'Não tenho pressa / Quando for a hora certa',
                'perfil_tipico': 'Pessoas estagnadas mas "confortáveis", medo do desconhecido',
                'raiz_emocional': 'Ansiedade sobre nova realidade / Zona de conforto',
                'sinais': ['"Quando for a hora certa"', 'Procrastinação disfarçada', 'Conformismo'],
                'contra_ataque': 'Dor da Estagnação + Janela Histórica',
                'scripts': [
                    'A única coisa pior que a dor da mudança é a dor do arrependimento',
                    'Esta oportunidade existe por [contexto específico]. Quem não aproveitar agora...'
                ]
            },
            'prioridades_desequilibradas': {
                'objecao_oculta': 'Não é dinheiro (mas gasta em outras coisas)',
                'perfil_tipico': 'Pessoas que gastam em lazer/consumo mas "não têm dinheiro" para evolução',
                'raiz_emocional': 'Não reconhece educação como prioridade / Vício em gratificação imediata',
                'sinais': ['Menções de gastos em outras áreas', 'Justificativas financeiras contraditórias'],
                'contra_ataque': 'Comparação Cruel + Cálculo de Oportunidade Perdida',
                'scripts': [
                    'R$200/mês em streaming vs R$2000 uma vez para nunca mais passar aperto',
                    'Você investe mais no seu carro que na sua mente'
                ]
            },
            'autoestima_destruida': {
                'objecao_oculta': 'Não confio em mim / Sou eu o problema',
                'perfil_tipico': 'Pessoas com múltiplas tentativas fracassadas, baixa confiança pessoal',
                'raiz_emocional': 'Histórico de fracassos / Medo de mais um fracasso',
                'sinais': ['"Já tentei antes"', 'Histórico de fracassos', 'Vitimização', 'Autodesqualificação'],
                'contra_ataque': 'Casos de Pessoas "Piores" + Diferencial do Método',
                'scripts': [
                    'Se [pessoa pior situação] conseguiu, você também consegue',
                    'O problema não era você, era a falta de método certo'
                ]
            }
        }
    
    def _load_neutralization_techniques(self) -> Dict[str, Dict[str, Any]]:
        """Carrega as 5 técnicas de neutralização do documento"""
        return {
            'concordar_valorizar_apresentar': {
                'estrutura': 'Você tem razão... Por isso criei...',
                'quando_usar': 'Objeções lógicas válidas',
                'exemplo': 'Você tem razão em ser cauteloso com investimentos. Por isso criei uma garantia de 60 dias...'
            },
            'inversao_perspectiva': {
                'estrutura': 'Na verdade é o oposto do que você imagina...',
                'quando_usar': 'Crenças limitantes',
                'exemplo': 'Na verdade, pessoas que mais precisam de ajuda são as que mais resistem a ela...'
            },
            'memorias_reviravolta': {
                'estrutura': 'Lembre de quando você decidiu sem certeza...',
                'quando_usar': 'Medo de decisão',
                'exemplo': 'Lembre quando você decidiu [mudança importante] sem ter certeza absoluta...'
            },
            'confronto_controlado': {
                'estrutura': 'Quantas vezes você perdeu oportunidade por isso?',
                'quando_usar': 'Padrões autodestrutivos',
                'exemplo': 'Quantas vezes você já perdeu oportunidades por "pensar demais"?'
            },
            'nova_crenca': {
                'estrutura': 'Isso é uma crença limitante, vou te mostrar outro ângulo...',
                'quando_usar': 'Crenças arraigadas',
                'exemplo': 'Isso é uma crença limitante. Vou te mostrar como pessoas "sem tempo" criaram tempo...'
            }
        }
    
    def generate_complete_anti_objection_arsenal(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any],
        research_responses: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Gera arsenal completo anti-objeção baseado no documento"""
        
        try:
            logger.info("🛡️ Gerando arsenal completo anti-objeção...")
            
            # Salva dados de entrada
            salvar_etapa("anti_objecao_completa_entrada", {
                "avatar_data": avatar_data,
                "context_data": context_data,
                "research_responses": research_responses
            }, categoria="anti_objecao")
            
            # FASE 1: Análise Psicológica das Respostas
            psychological_analysis = self._execute_psychological_analysis(avatar_data, research_responses)
            salvar_etapa("analise_psicologica", psychological_analysis, categoria="anti_objecao")
            
            # FASE 2: Diagnóstico de Objeções Específicas
            objections_diagnosis = self._execute_objections_diagnosis(psychological_analysis, context_data)
            salvar_etapa("diagnostico_objecoes", objections_diagnosis, categoria="anti_objecao")
            
            # FASE 3: Arsenal de Drives Mentais
            mental_drives_arsenal = self._create_mental_drives_arsenal(objections_diagnosis, context_data)
            salvar_etapa("arsenal_drives", mental_drives_arsenal, categoria="anti_objecao")
            
            # FASE 4: Sistema de Implementação Estratégica
            implementation_system = self._create_strategic_implementation(mental_drives_arsenal, context_data)
            salvar_etapa("implementacao_estrategica", implementation_system, categoria="anti_objecao")
            
            # FASE 5: Arsenal de Emergência
            emergency_arsenal = self._create_emergency_arsenal(context_data)
            salvar_etapa("arsenal_emergencia", emergency_arsenal, categoria="anti_objecao")
            
            complete_arsenal = {
                'resumo_executivo': {
                    'perfil_psicologico_audiencia': psychological_analysis.get('perfil_coletivo', {}),
                    'top_5_objecoes_criticas': objections_diagnosis.get('objecoes_prioritarias', []),
                    'estrategia_geral': 'Neutralização preventiva + Arsenal de emergência',
                    'momentos_criticos': ['Pré-lançamento', 'Durante evento', 'Momento oferta', 'Pós-oferta']
                },
                'analise_psicologica_detalhada': psychological_analysis,
                'diagnostico_objecoes_especificas': objections_diagnosis,
                'arsenal_drives_mentais': mental_drives_arsenal,
                'sistema_implementacao_estrategica': implementation_system,
                'kit_emergencia': emergency_arsenal,
                'objecoes_universais': self._customize_universal_objections(context_data),
                'objecoes_ocultas_criticas': self._customize_hidden_objections(avatar_data),
                'tecnicas_neutralizacao': self.neutralization_techniques,
                'metadata_completo': {
                    'total_objecoes_mapeadas': len(objections_diagnosis.get('objecoes_identificadas', [])),
                    'drives_criados': len(mental_drives_arsenal.get('drives_especificos', [])),
                    'tecnicas_disponeis': len(self.neutralization_techniques),
                    'generated_at': time.time(),
                    'sistema_completo': True
                }
            }
            
            # Salva arsenal completo
            salvar_etapa("arsenal_anti_objecao_completo", complete_arsenal, categoria="anti_objecao")
            
            logger.info("✅ Arsenal completo anti-objeção gerado")
            return complete_arsenal
            
        except Exception as e:
            logger.error(f"❌ Erro no arsenal completo anti-objeção: {e}")
            salvar_erro("arsenal_anti_objecao", e, contexto=context_data)
            return self._generate_fallback_complete_arsenal(context_data)
    
    def _execute_psychological_analysis(
        self, 
        avatar_data: Dict[str, Any], 
        research_responses: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """FASE 1: Análise Psicológica das Respostas"""
        
        try:
            prompt = f"""
Você é o ESPECIALISTA EM PSICOLOGIA DE VENDAS. Execute uma ANÁLISE PSICOLÓGICA PROFUNDA.

AVATAR DATA:
{json.dumps(avatar_data, ensure_ascii=False, indent=2)[:2000]}

RESEARCH RESPONSES:
{json.dumps(research_responses, ensure_ascii=False, indent=2)[:1500] if research_responses else "Não disponível"}

Execute análise psicológica seguindo as fases do documento:

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "mapeamento_emocional_geral": {{
    "temperatura_emocional_dominante": "Fria/Morna/Quente",
    "perfil_psicografico_coletivo": "Descrição do perfil coletivo",
    "nivel_consciencia": "Problema/Solução/Produto",
    "resistencia_geral": "Baixa/Média/Alta"
  }},
  "identificacao_dores_primarias": {{
    "dor_primaria": {{
      "descricao": "Dor principal identificada",
      "intensidade_emocional": "1-10",
      "frequencia": "Quantos % mencionam",
      "personalizacao": "Como cada um vive essa dor",
      "urgencia": "Nível de urgência percebida",
      "historico": "Há quanto tempo sofrem com isso"
    }},
    "dores_secundarias": [
      {{
        "descricao": "Dor secundária 1",
        "intensidade": "1-10",
        "frequencia": "% que menciona"
      }}
    ]
  }},
  "mapeamento_desejos_aspiracoes": {{
    "desejos_explicitos": ["Desejo 1", "Desejo 2"],
    "desejos_implicitos": ["Desejo oculto 1", "Desejo oculto 2"],
    "contradicoes": ["Contradição 1", "Contradição 2"],
    "comparacoes_sociais": ["Com quem se comparam"],
    "visualizacao_sucesso": "Como visualizam o sucesso"
  }},
  "perfil_coletivo": {{
    "arquetipo_dominante": "Tipo psicológico predominante",
    "medos_paralisantes": ["Medo 1", "Medo 2"],
    "motivadores_principais": ["Motivador 1", "Motivador 2"],
    "linguagem_tipica": ["Expressão 1", "Expressão 2"],
    "influenciadores_confianca": ["Fonte 1", "Fonte 2"]
  }}
}}
```
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=2500)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    return json.loads(clean_response)
                except json.JSONDecodeError:
                    logger.warning("JSON inválido na análise psicológica")
            
            return self._create_basic_psychological_analysis(avatar_data)
            
        except Exception as e:
            logger.error(f"Erro na análise psicológica: {e}")
            return self._create_basic_psychological_analysis(avatar_data)
    
    def _execute_objections_diagnosis(
        self, 
        psychological_analysis: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """FASE 2: Diagnóstico de Objeções Específicas"""
        
        try:
            prompt = f"""
Execute DIAGNÓSTICO COMPLETO de objeções baseado na análise psicológica.

ANÁLISE PSICOLÓGICA:
{json.dumps(psychological_analysis, ensure_ascii=False, indent=2)[:2000]}

CONTEXTO:
- Segmento: {context_data.get('segmento', 'Não informado')}
- Produto: {context_data.get('produto', 'Não informado')}
- Preço: R$ {context_data.get('preco', 'Não informado')}

Analise TODAS as objeções universais e ocultas:

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "objecoes_universais_detectadas": {{
    "tempo": {{
      "frases_especificas": ["Frase 1", "Frase 2"],
      "atividades_prioritarias": ["Atividade 1", "Atividade 2"],
      "sinais_procrastinacao": ["Sinal 1", "Sinal 2"],
      "rotina_atual": "Descrição da rotina",
      "tratamento_especifico": {{
        "drives_mentais": ["Drive 1", "Drive 2"],
        "historias_consequencia": ["História 1"],
        "reformulacao": "Como reformular 'tempo' como 'importância'",
        "calculo_custo": "Cálculo específico de custo de oportunidade"
      }}
    }},
    "dinheiro": {{
      "como_se_referem": ["Expressão 1", "Expressão 2"],
      "outras_areas_investimento": ["Área 1", "Área 2"],
      "dificuldade_vs_prioridade": "Análise da relação",
      "justificativas_gastos": ["Justificativa 1"],
      "tratamento_especifico": {{
        "tecnica_piorar_vida": "Como aplicar",
        "comparacoes_investimento": ["Comparação 1"],
        "historias_roi": ["História ROI"],
        "ressignificacao": "Gasto vs investimento vs custo de não agir"
      }}
    }},
    "confianca": {{
      "em_quem_desconfiam": ["Alvo 1", "Alvo 2"],
      "experiencias_negativas": ["Experiência 1"],
      "referencia_autoridades": ["Autoridade 1"],
      "desconfianca_si_mesmos": "Nível de autoconfiança",
      "tratamento_especifico": {{
        "provas_sociais_especificas": ["Prova 1"],
        "garantias_removem_riscos": ["Garantia 1"],
        "autoridade_construida": "Como construir",
        "validacao_preocupacoes": "Como validar medos"
      }}
    }}
  }},
  "objecoes_ocultas_identificadas": {{
    "autossuficiencia": {{
      "sinais_detectados": ["Sinal 1", "Sinal 2"],
      "perfil_tipico_presente": "Sim/Não",
      "raiz_emocional_ativa": "Orgulho/Medo incompetência",
      "contra_ataque_especifico": "Expert que Precisou de Expert customizado"
    }},
    "sinal_fraqueza": {{
      "sinais_detectados": ["Sinal 1"],
      "perfil_tipico_presente": "Sim/Não",
      "contra_ataque_especifico": "Reframe de Inteligência customizado"
    }},
    "medo_novo": {{
      "sinais_detectados": ["Sinal 1"],
      "perfil_tipico_presente": "Sim/Não",
      "contra_ataque_especifico": "Dor da Estagnação customizada"
    }},
    "prioridades_desequilibradas": {{
      "sinais_detectados": ["Sinal 1"],
      "gastos_outras_areas": ["Área 1"],
      "contra_ataque_especifico": "Comparação Cruel customizada"
    }},
    "autoestima_destruida": {{
      "sinais_detectados": ["Sinal 1"],
      "historico_fracassos": ["Fracasso 1"],
      "contra_ataque_especifico": "Casos Pessoas Piores customizado"
    }}
  }},
  "objecoes_prioritarias": [
    "Objeção 1 mais crítica",
    "Objeção 2 mais crítica",
    "Objeção 3 mais crítica",
    "Objeção 4 mais crítica",
    "Objeção 5 mais crítica"
  ],
  "objecoes_identificadas": [
    "Lista completa de todas as objeções identificadas"
  ]
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
                    logger.warning("JSON inválido no diagnóstico de objeções")
            
            return self._create_basic_objections_diagnosis(context_data)
            
        except Exception as e:
            logger.error(f"Erro no diagnóstico de objeções: {e}")
            return self._create_basic_objections_diagnosis(context_data)
    
    def _create_mental_drives_arsenal(
        self, 
        objections_diagnosis: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """FASE 3: Arsenal de Drives Mentais"""
        
        try:
            prompt = f"""
Crie ARSENAL COMPLETO de drives mentais anti-objeção.

DIAGNÓSTICO DE OBJEÇÕES:
{json.dumps(objections_diagnosis, ensure_ascii=False, indent=2)[:2000]}

CONTEXTO:
- Segmento: {context_data.get('segmento', 'Não informado')}
- Produto: {context_data.get('produto', 'Não informado')}

Crie drives específicos para cada categoria:

RETORNE APENAS JSON VÁLIDO:

```json
{{
  "drives_elevacao_prioridade": [
    {{
      "nome": "CÁLCULO DA SANGRIA",
      "objetivo": "Elevar prioridade para objeções de tempo",
      "gatilho": "Mostrar perda contínua por inação",
      "script_template": "Cada [período] sem [ação] = R$ [valor] perdidos",
      "historia_visceral": "História específica de 150+ palavras",
      "comando_acao": "Comando específico de ação",
      "frases_ancoragem": ["Frase 1", "Frase 2", "Frase 3"]
    }}
  ],
  "drives_justificacao_investimento": [
    {{
      "nome": "COMPARAÇÃO CRUEL",
      "objetivo": "Justificar investimento para objeções de dinheiro",
      "gatilho": "Contrastar gastos fúteis com investimento transformador",
      "script_template": "R$X em [futilidade] vs R$Y em [transformação]",
      "historia_visceral": "História específica de comparação",
      "comando_acao": "Redefina suas prioridades financeiras",
      "frases_ancoragem": ["Frase 1", "Frase 2", "Frase 3"]
    }}
  ],
  "drives_construcao_confianca": [
    {{
      "nome": "AUTORIDADE TÉCNICA INQUESTIONÁVEL",
      "objetivo": "Construir confiança para objeções de credibilidade",
      "gatilho": "Demonstrar expertise através de conhecimento profundo",
      "script_template": "Eu já [credencial] e consegui [resultado] usando isso",
      "historia_visceral": "História de autoridade específica",
      "comando_acao": "Confie na experiência comprovada",
      "frases_ancoragem": ["Frase 1", "Frase 2", "Frase 3"]
    }}
  ],
  "drives_objecoes_ocultas": [
    {{
      "nome": "O EXPERT QUE PRECISOU DE EXPERT",
      "objetivo": "Contra autossuficiência",
      "gatilho": "Mostrar que até experts precisam de orientação",
      "script_template": "Mesmo sendo [autoridade], precisei de ajuda para [resultado]",
      "historia_visceral": "História de expert vulnerável",
      "comando_acao": "Seja inteligente, busque orientação",
      "frases_ancoragem": ["Frase 1", "Frase 2", "Frase 3"]
    }}
  ],
  "templates_scripts": {{
    "concordancia_virada": "Você tem razão... Por isso criei...",
    "confronto_controlado": "Quantas vezes você perdeu oportunidade por isso?",
    "historia_visceral": "Era uma vez [personagem] que [situação]...",
    "calculo_brutal": "Vamos fazer as contas: [cálculo específico]"
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
                    logger.warning("JSON inválido no arsenal de drives")
            
            return self._create_basic_drives_arsenal(context_data)
            
        except Exception as e:
            logger.error(f"Erro no arsenal de drives: {e}")
            return self._create_basic_drives_arsenal(context_data)
    
    def _create_strategic_implementation(
        self, 
        drives_arsenal: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """FASE 4: Sistema de Implementação Estratégica"""
        
        return {
            'mapeamento_por_estagio': {
                'pre_lancamento': {
                    'drives_recomendados': ['CÁLCULO DA SANGRIA', 'OPORTUNIDADE OCULTA'],
                    'objetivo': 'Preparação subliminar',
                    'formato': 'Lives de aquecimento',
                    'intensidade': 'Baixa a média'
                },
                'durante_evento': {
                    'drives_recomendados': ['DIAGNÓSTICO BRUTAL', 'COMPARAÇÃO CRUEL'],
                    'objetivo': 'Instalação principal',
                    'formato': 'CPL ou webinar',
                    'intensidade': 'Média a alta'
                },
                'momento_oferta': {
                    'drives_recomendados': ['AUTORIDADE TÉCNICA', 'ROI ABSURDO'],
                    'objetivo': 'Neutralização final',
                    'formato': 'Pitch direto',
                    'intensidade': 'Máxima'
                },
                'pos_oferta': {
                    'drives_recomendados': ['EXPERT QUE PRECISOU', 'DECISÃO BINÁRIA'],
                    'objetivo': 'Eliminar hesitação',
                    'formato': 'Follow-up',
                    'intensidade': 'Focada'
                }
            },
            'personalizacao_por_perfil': self._create_persona_customization(drives_arsenal, context_data),
            'cronograma_implementacao': self._create_implementation_timeline(drives_arsenal),
            'metricas_eficacia': [
                'Taxa de objeções por tipo',
                'Tempo médio de neutralização',
                'Resistência pós-neutralização',
                'Taxa de conversão por drive'
            ]
        }
    
    def _create_persona_customization(self, drives_arsenal: Dict[str, Any], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Cria personalização por perfil"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return [
            {
                'nome_persona': f'O Cético de {segmento}',
                'perfil_psicologico': 'Desconfiado, analítico, precisa de muitas provas',
                'objecoes_primarias': ['confiança', 'autossuficiência'],
                'drives_eficazes': ['AUTORIDADE TÉCNICA', 'PROVA SOCIAL QUALIFICADA'],
                'linguagem_tom_ideal': 'Técnico, baseado em dados, respeitoso',
                'momentos_resistencia': ['Primeira apresentação', 'Momento da oferta']
            },
            {
                'nome_persona': f'O Ocupado de {segmento}',
                'perfil_psicologico': 'Sempre correndo, prioridades desalinhadas',
                'objecoes_primarias': ['tempo', 'prioridades_desequilibradas'],
                'drives_eficazes': ['CÁLCULO DA SANGRIA', 'COMPARAÇÃO CRUEL'],
                'linguagem_tom_ideal': 'Direto, urgente, focado em resultados',
                'momentos_resistencia': ['Início da apresentação', 'Explicações longas']
            },
            {
                'nome_persona': f'O Queimado de {segmento}',
                'perfil_psicologico': 'Já tentou muito, baixa autoestima, vitimização',
                'objecoes_primarias': ['autoestima_destruída', 'confiança'],
                'drives_eficazes': ['CASOS PESSOAS PIORES', 'DIFERENCIAL DO MÉTODO'],
                'linguagem_tom_ideal': 'Empático, encorajador, baseado em casos similares',
                'momentos_resistencia': ['Qualquer promessa', 'Garantias']
            }
        ]
    
    def _create_implementation_timeline(self, drives_arsenal: Dict[str, Any]) -> Dict[str, Any]:
        """Cria timeline de implementação"""
        
        return {
            'semana_1_preparacao': {
                'atividades': ['Mapear objeções específicas da audiência', 'Preparar histórias viscerais', 'Treinar scripts'],
                'drives_foco': ['Preparação de autoridade', 'Coleta de casos'],
                'entregaveis': ['Scripts prontos', 'Histórias testadas']
            },
            'semana_2_aquecimento': {
                'atividades': ['Lives de preparação', 'Instalação de drives básicos', 'Teste de reações'],
                'drives_foco': ['OPORTUNIDADE OCULTA', 'DIAGNÓSTICO SUAVE'],
                'entregaveis': ['Audiência preparada', 'Objeções mapeadas']
            },
            'evento_principal': {
                'atividades': ['Instalação completa de drives', 'Neutralização ativa', 'Monitoramento reações'],
                'drives_foco': ['Todos os drives principais'],
                'entregaveis': ['Objeções neutralizadas', 'Audiência convertida']
            },
            'pos_evento': {
                'atividades': ['Follow-up personalizado', 'Neutralização residual', 'Análise resultados'],
                'drives_foco': ['CORAGEM NECESSÁRIA', 'DECISÃO BINÁRIA'],
                'entregaveis': ['Conversões finalizadas', 'Relatório de eficácia']
            }
        }
    
    def _create_emergency_arsenal(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """FASE 5: Arsenal de Emergência"""
        
        return {
            'objecoes_ultima_hora': {
                'preciso_pensar': {
                    'diagnostico_rapido': 'Medo de decisão ou falta de urgência',
                    'tratamento_imediato': 'RELÓGIO PSICOLÓGICO + CUSTO INVISÍVEL',
                    'script_emergencia': 'Pensar é importante, mas pensar demais paralisa...',
                    'validacao': 'Entendo a necessidade de refletir',
                    'follow_up': 'Prazo específico para decisão'
                },
                'nao_e_momento_certo': {
                    'diagnostico_rapido': 'Zona de conforto ou medo do novo',
                    'tratamento_imediato': 'DOR DA ESTAGNAÇÃO + JANELA HISTÓRICA',
                    'script_emergencia': 'Momento certo é uma ilusão que mantém você parado...',
                    'validacao': 'Compreendo a cautela',
                    'follow_up': 'Mostrar custo de esperar'
                },
                'vou_fazer_depois': {
                    'diagnostico_rapido': 'Procrastinação ou prioridades desalinhadas',
                    'tratamento_imediato': 'CONSEQUÊNCIA EXPONENCIAL + COMPARAÇÃO CRUEL',
                    'script_emergencia': 'Depois é onde os sonhos vão morrer...',
                    'validacao': 'Entendo que tem outras prioridades',
                    'follow_up': 'Cálculo do custo de adiar'
                }
            },
            'kit_primeiros_socorros': {
                'diagnostico_rapido': [
                    'Identificar tipo de objeção em 30 segundos',
                    'Mapear raiz emocional imediatamente',
                    'Selecionar drive apropriado'
                ],
                'tratamento_imediato': [
                    'Aplicar técnica de neutralização',
                    'Usar script de emergência',
                    'Validar preocupação'
                ],
                'validacao': [
                    'Confirmar neutralização',
                    'Verificar estado emocional',
                    'Preparar próximo passo'
                ],
                'follow_up': [
                    'Reforçar neutralização',
                    'Adicionar prova social',
                    'Criar urgência específica'
                ]
            },
            'scripts_emergencia_prontos': [
                'Vamos ser honestos: você vai continuar adiando até quando?',
                'A única diferença entre você e quem já conseguiu é a decisão de agir',
                'Quantas oportunidades você já perdeu por "pensar demais"?',
                'O medo de errar está te impedindo de acertar',
                'Você prefere o arrependimento de ter tentado ou de não ter tentado?',
                'Cada "não" que você diz para evolução é um "sim" para estagnação',
                'O tempo que você está perdendo pensando, outros estão usando para agir',
                'Sua zona de conforto é uma prisão disfarçada de segurança'
            ]
        }
    
    def _customize_universal_objections(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Customiza objeções universais para o contexto"""
        
        segmento = context_data.get('segmento', 'negócios')
        customized = {}
        
        for obj_type, obj_data in self.universal_objections.items():
            customized[obj_type] = obj_data.copy()
            customized[obj_type]['contexto_segmento'] = segmento
            customized[obj_type]['scripts_customizados'] = [
                script.replace('[período]', 'mês')
                      .replace('[problema]', f'situação em {segmento}')
                      .replace('[quantia específica]', 'R$ 10.000 em oportunidades')
                for script in obj_data['scripts']
            ]
        
        return customized
    
    def _customize_hidden_objections(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Customiza objeções ocultas baseado no avatar"""
        
        customized = {}
        personalidade = avatar_data.get('perfil_psicografico', {}).get('personalidade', '').lower()
        
        for obj_type, obj_data in self.hidden_objections.items():
            customized[obj_type] = obj_data.copy()
            
            # Calcula probabilidade baseado no perfil
            if obj_type == 'autossuficiencia' and any(trait in personalidade for trait in ['independente', 'autoconfiante']):
                customized[obj_type]['probabilidade'] = 'Alta'
            elif obj_type == 'sinal_fraqueza' and 'líder' in personalidade:
                customized[obj_type]['probabilidade'] = 'Média'
            else:
                customized[obj_type]['probabilidade'] = 'Baixa'
        
        return customized
    
    def _create_basic_psychological_analysis(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria análise psicológica básica como fallback"""
        
        return {
            'mapeamento_emocional_geral': {
                'temperatura_emocional_dominante': 'Morna',
                'perfil_psicografico_coletivo': 'Profissionais ambiciosos mas sobrecarregados',
                'nivel_consciencia': 'Problema',
                'resistencia_geral': 'Média'
            },
            'identificacao_dores_primarias': {
                'dor_primaria': {
                    'descricao': 'Trabalhar muito sem crescer proporcionalmente',
                    'intensidade_emocional': '8',
                    'frequencia': '85%',
                    'urgencia': 'Alta'
                }
            },
            'perfil_coletivo': {
                'arquetipo_dominante': 'O Escalador Frustrado',
                'medos_paralisantes': ['Fracasso público', 'Estagnação'],
                'motivadores_principais': ['Liberdade', 'Reconhecimento']
            },
            'fallback_mode': True
        }
    
    def _create_basic_objections_diagnosis(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria diagnóstico básico de objeções"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'objecoes_universais_detectadas': {
                'tempo': {
                    'frases_especificas': [f'Não tenho tempo para implementar em {segmento}'],
                    'tratamento_especifico': {
                        'drives_mentais': ['CÁLCULO DA SANGRIA'],
                        'calculo_custo': f'Cada mês sem otimizar {segmento} = R$ 10.000 perdidos'
                    }
                },
                'dinheiro': {
                    'como_se_referem': ['Investimento alto', 'Não cabe no orçamento'],
                    'tratamento_especifico': {
                        'comparacoes_investimento': [f'ROI em {segmento} paga investimento em 3 meses']
                    }
                },
                'confianca': {
                    'em_quem_desconfiam': ['Gurus', 'Promessas mirabolantes'],
                    'tratamento_especifico': {
                        'autoridade_construida': f'Expertise comprovada em {segmento}'
                    }
                }
            },
            'objecoes_prioritarias': [
                f'Não tenho tempo para implementar em {segmento}',
                'Preciso pensar melhor sobre o investimento',
                f'Meu caso em {segmento} é muito específico',
                'Já tentei outras coisas e não funcionaram',
                'Preciso de mais garantias'
            ],
            'fallback_mode': True
        }
    
    def _create_basic_drives_arsenal(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria arsenal básico de drives"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'drives_elevacao_prioridade': [
                {
                    'nome': f'CÁLCULO DA SANGRIA EM {segmento.upper()}',
                    'objetivo': 'Elevar prioridade para objeções de tempo',
                    'script_template': f'Cada mês sem otimizar {segmento} = R$ 10.000 perdidos',
                    'frases_ancoragem': [f'Tempo perdido em {segmento} não volta']
                }
            ],
            'drives_justificacao_investimento': [
                {
                    'nome': f'ROI ABSURDO EM {segmento.upper()}',
                    'objetivo': 'Justificar investimento',
                    'script_template': f'ROI médio em {segmento}: 300-500% em 12 meses',
                    'frases_ancoragem': [f'Investimento em {segmento} se paga sozinho']
                }
            ],
            'fallback_mode': True
        }
    
    def _generate_fallback_complete_arsenal(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera arsenal completo de fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        return {
            'resumo_executivo': {
                'perfil_psicologico_audiencia': f'Profissionais de {segmento} ambiciosos',
                'top_5_objecoes_criticas': [
                    f'Não tenho tempo para {segmento}',
                    'Investimento muito alto',
                    'Preciso de mais garantias',
                    f'Meu caso em {segmento} é específico',
                    'Já tentei outras coisas'
                ],
                'estrategia_geral': 'Neutralização preventiva com drives customizados'
            },
            'objecoes_universais': self._customize_universal_objections(context_data),
            'objecoes_ocultas_criticas': self.hidden_objections,
            'tecnicas_neutralizacao': self.neutralization_techniques,
            'arsenal_emergencia': [
                f'Quantas oportunidades em {segmento} você já perdeu por hesitar?',
                f'Seus concorrentes em {segmento} não estão esperando você se decidir',
                f'O custo de não agir em {segmento} é maior que o investimento'
            ],
            'fallback_mode': True,
            'sistema_completo': True
        }

# Instância global
complete_anti_objection_system = CompleteAntiObjectionSystem()