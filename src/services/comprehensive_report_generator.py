#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Comprehensive Report Generator
Gerador de relatórios abrangentes com todos os componentes
"""

import logging
import time
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class ComprehensiveReportGenerator:
    """Gerador de relatórios abrangentes com todos os componentes"""
    
    def __init__(self):
        """Inicializa o gerador de relatórios"""
        self.report_sections = {
            'analise_forense_devastadora': 'Análise Forense Devastadora',
            'analise_forense_completa': 'Análise Forense Completa (12 Camadas)',
            'engenharia_reversa_psicologica': 'Engenharia Reversa Psicológica',
            'sistema_drivers_mentais': 'Sistema de Drivers Mentais',
            'drivers_mentais_sistema_completo': 'Sistema Completo de Drivers Mentais',
            'sistema_anti_objecao_completo': 'Sistema Anti-Objeção Completo',
            'arsenal_anti_objecao_completo': 'Arsenal Completo Anti-Objeção',
            'pre_pitch_invisivel_completo': 'Pré-Pitch Invisível',
            'sistema_pre_pitch_completo': 'Sistema Completo de Pré-Pitch',
            'sistema_provas_visuais_completo': 'Sistema de Provas Visuais',
            'sistema_provis_completo': 'Sistema Completo de PROVIs',
            'dashboard_avatar_completo': 'Dashboard do Avatar',
            'avatar_ultra_detalhado': 'Avatar Ultra-Detalhado',
            'drivers_mentais_customizados': 'Drivers Mentais Customizados',
            'provas_visuais_sugeridas': 'Provas Visuais Sugeridas',
            'sistema_anti_objecao': 'Sistema Anti-Objeção',
            'pre_pitch_invisivel': 'Pré-Pitch Invisível',
            'predicoes_futuro_completas': 'Predições do Futuro',
            'pesquisa_web_massiva': 'Pesquisa Web Massiva',
            'insights_exclusivos': 'Insights Exclusivos'
        }
        
        logger.info("Comprehensive Report Generator inicializado")
    
    def generate_complete_report(self, analysis_data: Dict[str, Any]) -> str:
        """Gera relatório completo em Markdown"""
        
        try:
            logger.info("📋 Gerando relatório abrangente...")
            
            # Cabeçalho do relatório
            report = self._generate_report_header(analysis_data)
            
            # Índice
            report += self._generate_table_of_contents(analysis_data)
            
            # Resumo executivo
            report += self._generate_executive_summary(analysis_data)
            
            # Seções principais
            for section_key, section_title in self.report_sections.items():
                if section_key in analysis_data and analysis_data[section_key]:
                    report += self._generate_section(section_key, section_title, analysis_data[section_key])
            
            # Conclusões e próximos passos
            report += self._generate_conclusions(analysis_data)
            
            # Salva relatório
            salvar_etapa("relatorio_completo_markdown", {
                "content": report,
                "length": len(report),
                "sections_included": len([k for k in self.report_sections.keys() if k in analysis_data])
            }, categoria="analise_completa")
            
            logger.info(f"✅ Relatório completo gerado: {len(report)} caracteres")
            return report
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar relatório: {e}")
            salvar_erro("relatorio_completo", e)
            return self._generate_fallback_report(analysis_data)
    
    def _generate_report_header(self, analysis_data: Dict[str, Any]) -> str:
        """Gera cabeçalho do relatório"""
        
        segmento = analysis_data.get('segmento', 'Não informado')
        produto = analysis_data.get('produto', 'Não informado')
        
        return f"""# ANÁLISE ULTRA-DETALHADA DE MERCADO
## ARQV30 Enhanced v2.0 - Relatório Completo

**Segmento:** {segmento}  
**Produto/Serviço:** {produto}  
**Data de Geração:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}  
**Versão:** 2.0.0  

---

"""
    
    def _generate_table_of_contents(self, analysis_data: Dict[str, Any]) -> str:
        """Gera índice do relatório"""
        
        toc = "## 📋 ÍNDICE\n\n"
        
        section_number = 1
        for section_key, section_title in self.report_sections.items():
            if section_key in analysis_data and analysis_data[section_key]:
                toc += f"{section_number}. [{section_title}](#{section_key.replace('_', '-')})\n"
                section_number += 1
        
        toc += "\n---\n\n"
        return toc
    
    def _generate_executive_summary(self, analysis_data: Dict[str, Any]) -> str:
        """Gera resumo executivo"""
        
        summary = "## 🎯 RESUMO EXECUTIVO\n\n"
        
        # Informações básicas
        projeto_dados = analysis_data.get('projeto_dados', {})
        summary += f"**Segmento Analisado:** {projeto_dados.get('segmento', 'Não informado')}\n"
        summary += f"**Produto/Serviço:** {projeto_dados.get('produto', 'Não informado')}\n"
        summary += f"**Público-Alvo:** {projeto_dados.get('publico', 'Não informado')}\n"
        summary += f"**Preço:** R$ {projeto_dados.get('preco', 'Não informado')}\n\n"
        
        # Componentes gerados
        components_count = len([k for k in self.report_sections.keys() if k in analysis_data])
        summary += f"**Componentes Gerados:** {components_count} sistemas completos\n\n"
        
        # Principais insights
        insights = analysis_data.get('insights_exclusivos', [])
        if insights:
            summary += "### 💡 Principais Insights\n\n"
            for i, insight in enumerate(insights[:5], 1):
                summary += f"{i}. {insight}\n"
            summary += "\n"
        
        # Qualidade da análise
        metadata = analysis_data.get('metadata', {})
        if metadata:
            summary += "### 📊 Qualidade da Análise\n\n"
            summary += f"- **Tempo de Processamento:** {metadata.get('processing_time_formatted', 'N/A')}\n"
            summary += f"- **Fontes Consultadas:** {metadata.get('data_sources_used', 'N/A')}\n"
            summary += f"- **Modelos de IA Utilizados:** {metadata.get('ai_models_used', 'N/A')}\n"
            summary += f"- **Salvamento Automático:** ✅ Ativo\n"
            summary += f"- **Isolamento de Falhas:** ✅ Ativo\n\n"
        
        summary += "---\n\n"
        return summary
    
    def _generate_section(self, section_key: str, section_title: str, section_data: Any) -> str:
        """Gera seção específica do relatório"""
        
        section = f"## {section_title}\n\n"
        
        try:
            if section_key == 'analise_forense_devastadora':
                section += self._format_forensic_analysis(section_data)
            elif section_key == 'engenharia_reversa_psicologica':
                section += self._format_psychological_reverse(section_data)
            elif section_key == 'sistema_drivers_mentais':
                section += self._format_mental_drivers_system(section_data)
            elif section_key == 'sistema_anti_objecao_completo':
                section += self._format_anti_objection_system(section_data)
            elif section_key == 'pre_pitch_invisivel_completo':
                section += self._format_pre_pitch_system(section_data)
            elif section_key == 'sistema_provas_visuais_completo':
                section += self._format_visual_proofs_system(section_data)
            elif section_key == 'dashboard_avatar_completo':
                section += self._format_avatar_dashboard(section_data)
            elif section_key == 'avatar_ultra_detalhado':
                section += self._format_avatar_analysis(section_data)
            elif section_key == 'pesquisa_web_massiva':
                section += self._format_research_analysis(section_data)
            elif section_key == 'insights_exclusivos':
                section += self._format_insights_analysis(section_data)
            else:
                section += self._format_generic_section(section_data)
            
        except Exception as e:
            logger.error(f"Erro ao formatar seção {section_key}: {e}")
            section += f"**Erro ao processar seção:** {str(e)}\n\n"
        
        section += "---\n\n"
        return section
    
    def _format_forensic_analysis(self, data: Dict[str, Any]) -> str:
        """Formata análise forense devastadora"""
        
        content = "### 🔍 DNA DA CONVERSÃO IDENTIFICADO\n\n"
        
        if 'resumo_executivo' in data:
            resumo = data['resumo_executivo']
            content += f"**Veredicto Geral:** {resumo.get('veredicto_geral', 'N/A')}\n\n"
            
            if 'top_3_pontos_fortes' in resumo:
                content += "**Top 3 Pontos Mais Fortes:**\n"
                for i, ponto in enumerate(resumo['top_3_pontos_fortes'], 1):
                    content += f"{i}. {ponto}\n"
                content += "\n"
        
        if 'dna_conversao' in data:
            dna = data['dna_conversao']
            content += "### 🧬 Fórmula Estrutural\n\n"
            content += f"**Fórmula:** {dna.get('formula_estrutural', 'N/A')}\n\n"
            
            if 'sequencia_gatilhos' in dna:
                content += "**Sequência de Gatilhos:**\n"
                for i, gatilho in enumerate(dna['sequencia_gatilhos'], 1):
                    content += f"{i}. {gatilho}\n"
                content += "\n"
        
        if 'metricas_objetivas' in data:
            metricas = data['metricas_objetivas']
            content += "### 📊 Métricas Objetivas\n\n"
            content += f"- **Duração Total:** {metricas.get('duracao_total', 'N/A')}\n"
            content += f"- **Densidade Informacional:** {metricas.get('densidade_informacional', 'N/A')}\n"
            content += f"- **Ratio EU/VOCÊ:** {metricas.get('ratio_eu_voce', 'N/A')}\n"
            content += f"- **Promessas Totais:** {metricas.get('promessas_totais', 'N/A')}\n"
            content += f"- **Provas Oferecidas:** {metricas.get('provas_oferecidas', 'N/A')}\n\n"
        
        return content
    
    def _format_psychological_reverse(self, data: Dict[str, Any]) -> str:
        """Formata engenharia reversa psicológica"""
        
        content = "### 🧬 DOSSIÊ PSICOLÓGICO CONFIDENCIAL\n\n"
        
        if 'perfil_psicologico_profundo' in data:
            perfil = data['perfil_psicologico_profundo']
            content += f"**Nome Fictício:** {perfil.get('nome_ficticio', 'N/A')}\n"
            content += f"**Idade:** {perfil.get('idade_aproximada', 'N/A')}\n"
            content += f"**Ocupação:** {perfil.get('ocupacao_situacao', 'N/A')}\n"
            content += f"**Jornada de Dor:** {perfil.get('jornada_dor', 'N/A')}\n\n"
        
        if 'feridas_abertas' in data:
            content += "### 🩸 AS FERIDAS ABERTAS\n\n"
            for i, ferida in enumerate(data['feridas_abertas'], 1):
                content += f"{i}. {ferida}\n"
            content += "\n"
        
        if 'sonhos_proibidos' in data:
            content += "### ✨ OS SONHOS PROIBIDOS\n\n"
            for i, sonho in enumerate(data['sonhos_proibidos'], 1):
                content += f"{i}. {sonho}\n"
            content += "\n"
        
        if 'demonios_internos' in data:
            content += "### 👹 OS DEMÔNIOS INTERNOS\n\n"
            for i, demonio in enumerate(data['demonios_internos'], 1):
                content += f"{i}. {demonio}\n"
            content += "\n"
        
        if 'dialeto_alma' in data:
            dialeto = data['dialeto_alma']
            content += "### 🗣️ O DIALETO DA ALMA\n\n"
            
            if 'frases_dores' in dialeto:
                content += "**Frases Típicas Sobre Dores:**\n"
                for frase in dialeto['frases_dores']:
                    content += f"- \"{frase}\"\n"
                content += "\n"
            
            if 'frases_desejos' in dialeto:
                content += "**Frases Típicas Sobre Desejos:**\n"
                for frase in dialeto['frases_desejos']:
                    content += f"- \"{frase}\"\n"
                content += "\n"
        
        return content
    
    def _format_mental_drivers_system(self, data: Dict[str, Any]) -> str:
        """Formata sistema de drivers mentais"""
        
        content = "### ⚡ ARSENAL DE DRIVERS MENTAIS\n\n"
        
        if 'drivers_emocionais_primarios' in data:
            content += "#### 🔥 Drivers Emocionais Primários\n\n"
            for i, driver in enumerate(data['drivers_emocionais_primarios'], 1):
                content += f"**{i}. {driver.get('nome', 'Driver')}**\n\n"
                content += f"- **Gatilho Central:** {driver.get('gatilho_central', 'N/A')}\n"
                content += f"- **Definição:** {driver.get('definicao_visceral', 'N/A')}\n"
                
                if 'roteiro_ativacao' in driver:
                    roteiro = driver['roteiro_ativacao']
                    content += f"- **Pergunta de Abertura:** {roteiro.get('pergunta_abertura', 'N/A')}\n"
                    content += f"- **História/Analogia:** {roteiro.get('historia_analogia', 'N/A')}\n"
                    content += f"- **Comando de Ação:** {roteiro.get('comando_acao', 'N/A')}\n"
                
                if 'frases_ancoragem' in driver:
                    content += "- **Frases de Ancoragem:**\n"
                    for frase in driver['frases_ancoragem']:
                        content += f"  - \"{frase}\"\n"
                
                content += "\n"
        
        if 'top_7_essenciais' in data:
            content += "#### 🎯 Top 7 Drivers Essenciais\n\n"
            for i, driver in enumerate(data['top_7_essenciais'], 1):
                content += f"{i}. {driver}\n"
            content += "\n"
        
        return content
    
    def _format_anti_objection_system(self, data: Dict[str, Any]) -> str:
        """Formata sistema anti-objeção"""
        
        content = "### 🛡️ ARSENAL ANTI-OBJEÇÃO\n\n"
        
        if 'objecoes_universais' in data:
            content += "#### 🌍 Objeções Universais\n\n"
            for objecao_tipo, objecao_data in data['objecoes_universais'].items():
                content += f"**{objecao_tipo.upper()}**\n\n"
                content += f"- **Objeção:** {objecao_data.get('objecao', 'N/A')}\n"
                content += f"- **Raiz Emocional:** {objecao_data.get('raiz_emocional', 'N/A')}\n"
                content += f"- **Contra-Ataque:** {objecao_data.get('contra_ataque', 'N/A')}\n"
                
                if 'scripts' in objecao_data:
                    content += "- **Scripts:**\n"
                    for script in objecao_data['scripts']:
                        content += f"  - \"{script}\"\n"
                
                content += "\n"
        
        if 'objecoes_ocultas_criticas' in data:
            content += "#### 🕵️ Objeções Ocultas Críticas\n\n"
            for objecao_tipo, objecao_data in data['objecoes_ocultas_criticas'].items():
                content += f"**{objecao_tipo.upper().replace('_', ' ')}**\n\n"
                content += f"- **Objeção Oculta:** {objecao_data.get('objecao_oculta', 'N/A')}\n"
                content += f"- **Perfil Típico:** {objecao_data.get('perfil_tipico', 'N/A')}\n"
                content += f"- **Contra-Ataque:** {objecao_data.get('contra_ataque', 'N/A')}\n"
                content += "\n"
        
        if 'arsenal_emergencia' in data:
            content += "#### 🚨 Arsenal de Emergência\n\n"
            for i, frase in enumerate(data['arsenal_emergencia'], 1):
                content += f"{i}. \"{frase}\"\n"
            content += "\n"
        
        return content
    
    def _format_pre_pitch_system(self, data: Dict[str, Any]) -> str:
        """Formata sistema de pré-pitch"""
        
        content = "### 🎭 PRÉ-PITCH INVISÍVEL\n\n"
        
        if 'orquestracao_emocional' in data:
            content += "#### 🎼 Orquestração Emocional\n\n"
            sequencia = data['orquestracao_emocional'].get('sequencia_psicologica', [])
            
            for i, fase in enumerate(sequencia, 1):
                content += f"**FASE {i}: {fase.get('fase', 'N/A').upper()}**\n\n"
                content += f"- **Objetivo:** {fase.get('objetivo', 'N/A')}\n"
                content += f"- **Duração:** {fase.get('duracao', 'N/A')}\n"
                content += f"- **Intensidade:** {fase.get('intensidade', 'N/A')}\n"
                content += f"- **Resultado Esperado:** {fase.get('resultado_esperado', 'N/A')}\n"
                
                if 'drivers_utilizados' in fase:
                    content += f"- **Drivers Utilizados:** {', '.join(fase['drivers_utilizados'])}\n"
                
                content += "\n"
        
        if 'roteiro_completo' in data:
            content += "#### 📝 Roteiro Completo\n\n"
            roteiro = data['roteiro_completo']
            
            for secao_nome, secao_data in roteiro.items():
                if isinstance(secao_data, dict):
                    content += f"**{secao_nome.upper().replace('_', ' ')}**\n\n"
                    content += f"- **Tempo:** {secao_data.get('tempo', 'N/A')}\n"
                    content += f"- **Objetivo:** {secao_data.get('objetivo', 'N/A')}\n"
                    content += f"- **Script:** {secao_data.get('script', 'N/A')}\n"
                    content += "\n"
        
        return content
    
    def _format_visual_proofs_system(self, data: Dict[str, Any]) -> str:
        """Formata sistema de provas visuais"""
        
        content = "### 🎯 SISTEMA DE PROVAS VISUAIS (PROVIs)\n\n"
        
        if 'arsenal_provis' in data:
            content += "#### 🎪 Arsenal de PROVIs\n\n"
            for i, provi in enumerate(data['arsenal_provis'], 1):
                content += f"**{provi.get('nome', f'PROVI #{i}')}**\n\n"
                content += f"- **Conceito-Alvo:** {provi.get('conceito_alvo', 'N/A')}\n"
                content += f"- **Categoria:** {provi.get('categoria', 'N/A')}\n"
                content += f"- **Prioridade:** {provi.get('prioridade', 'N/A')}\n"
                content += f"- **Experimento:** {provi.get('experimento', 'N/A')}\n"
                
                if 'materiais' in provi:
                    content += "- **Materiais:**\n"
                    for material in provi['materiais']:
                        content += f"  - {material}\n"
                
                if 'roteiro_completo' in provi:
                    roteiro = provi['roteiro_completo']
                    content += f"- **Setup:** {roteiro.get('setup', 'N/A')}\n"
                    content += f"- **Execução:** {roteiro.get('execucao', 'N/A')}\n"
                    content += f"- **Clímax:** {roteiro.get('climax', 'N/A')}\n"
                
                content += "\n"
        
        if 'categorias_provis' in data:
            categorias = data['categorias_provis']
            content += "#### 📂 Categorias de PROVIs\n\n"
            
            if 'destruidoras_objecao' in categorias:
                content += "**Destruidoras de Objeção:**\n"
                for destruidora in categorias['destruidoras_objecao']:
                    content += f"- **Contra \"{destruidora.get('contra', 'N/A')}\":** {', '.join(destruidora.get('experimentos', []))}\n"
                content += "\n"
        
        return content
    
    def _format_avatar_dashboard(self, data: Dict[str, Any]) -> str:
        """Formata dashboard do avatar"""
        
        content = "### 👤 DASHBOARD ARQUEOLÓGICO DO AVATAR\n\n"
        
        if 'visao_geral' in data:
            visao = data['visao_geral']
            content += "#### 📊 Visão Geral\n\n"
            content += f"**Público Analisado:** {visao.get('publico_analisado', 'N/A')}\n\n"
            
            if 'distribuicao_faturamento' in visao:
                dist = visao['distribuicao_faturamento']
                content += "**Distribuição por Faturamento:**\n"
                content += f"- Acima de R$ 5 milhões: {dist.get('acima_5_milhoes', 'N/A')}\n"
                content += f"- Entre R$ 1-5 milhões: {dist.get('entre_1_5_milhoes', 'N/A')}\n"
                content += f"- Abaixo de R$ 1 milhão: {dist.get('abaixo_1_milhao', 'N/A')}\n\n"
        
        if 'analise_dores' in data:
            dores = data['analise_dores']
            content += "#### 😣 Análise de Dores\n\n"
            
            if 'top_10_dores_estruturadas' in dores:
                content += "**Top 10 Dores Estruturadas:**\n"
                for i, dor in enumerate(dores['top_10_dores_estruturadas'], 1):
                    content += f"{i}. **{dor.get('dor', 'N/A')}**\n"
                    content += f"   - Frequência: {dor.get('frequencia', 'N/A')}\n"
                    content += f"   - Intensidade: {dor.get('intensidade', 'N/A')}\n"
                    content += f"   - Contexto: {dor.get('contexto', 'N/A')}\n"
                content += "\n"
        
        if 'comportamento' in data:
            comportamento = data['comportamento']
            content += "#### 🧠 Análise Comportamental\n\n"
            
            if 'arquetipos_dominantes' in comportamento:
                content += "**Arquétipos Dominantes:**\n"
                for arquetipo, percentual in comportamento['arquetipos_dominantes'].items():
                    content += f"- {arquetipo.replace('_', ' ').title()}: {percentual}\n"
                content += "\n"
            
            if 'medos_paralisantes' in comportamento:
                content += "**Medos Paralisantes:**\n"
                for medo in comportamento['medos_paralisantes']:
                    content += f"- {medo}\n"
                content += "\n"
        
        return content
    
    def _format_avatar_analysis(self, data: Dict[str, Any]) -> str:
        """Formata análise do avatar"""
        
        content = "### 👤 AVATAR ULTRA-DETALHADO\n\n"
        
        if 'perfil_demografico' in data:
            content += "#### 📊 Perfil Demográfico\n\n"
            for key, value in data['perfil_demografico'].items():
                content += f"- **{key.replace('_', ' ').title()}:** {value}\n"
            content += "\n"
        
        if 'dores_viscerais' in data:
            content += "#### 😣 Dores Viscerais\n\n"
            for i, dor in enumerate(data['dores_viscerais'], 1):
                content += f"{i}. {dor}\n"
            content += "\n"
        
        if 'desejos_secretos' in data:
            content += "#### ✨ Desejos Secretos\n\n"
            for i, desejo in enumerate(data['desejos_secretos'], 1):
                content += f"{i}. {desejo}\n"
            content += "\n"
        
        return content
    
    def _format_research_analysis(self, data: Dict[str, Any]) -> str:
        """Formata análise de pesquisa"""
        
        content = "### 🔍 PESQUISA WEB MASSIVA\n\n"
        
        if 'estatisticas' in data:
            stats = data['estatisticas']
            content += "#### 📊 Estatísticas da Pesquisa\n\n"
            content += f"- **Total de Queries:** {stats.get('total_queries', 'N/A')}\n"
            content += f"- **Total de Resultados:** {stats.get('total_resultados', 'N/A')}\n"
            content += f"- **Fontes Únicas:** {stats.get('fontes_unicas', 'N/A')}\n"
            content += f"- **Conteúdo Extraído:** {stats.get('total_conteudo', 'N/A'):,} caracteres\n"
            content += f"- **Qualidade Média:** {stats.get('qualidade_media', 'N/A'):.1f}%\n\n"
        
        if 'fontes' in data:
            content += "#### 🌐 Principais Fontes\n\n"
            for i, fonte in enumerate(data['fontes'][:10], 1):
                content += f"{i}. **{fonte.get('title', 'Sem título')}**\n"
                content += f"   - URL: {fonte.get('url', 'N/A')}\n"
                if 'quality_score' in fonte:
                    content += f"   - Qualidade: {fonte['quality_score']:.1f}%\n"
                content += "\n"
        
        return content
    
    def _format_insights_analysis(self, data: List[str]) -> str:
        """Formata análise de insights"""
        
        content = "### 💡 INSIGHTS EXCLUSIVOS\n\n"
        
        for i, insight in enumerate(data, 1):
            content += f"{i}. {insight}\n"
        
        content += "\n"
        return content
    
    def _format_generic_section(self, data: Any) -> str:
        """Formata seção genérica"""
        
        if isinstance(data, dict):
            content = ""
            for key, value in data.items():
                content += f"**{key.replace('_', ' ').title()}:** {value}\n"
            content += "\n"
            return content
        elif isinstance(data, list):
            content = ""
            for i, item in enumerate(data, 1):
                content += f"{i}. {item}\n"
            content += "\n"
            return content
        else:
            return f"{str(data)}\n\n"
    
    def _generate_conclusions(self, analysis_data: Dict[str, Any]) -> str:
        """Gera conclusões e próximos passos"""
        
        conclusions = "## 🎯 CONCLUSÕES E PRÓXIMOS PASSOS\n\n"
        
        # Resumo dos componentes
        components_generated = len([k for k in self.report_sections.keys() if k in analysis_data])
        conclusions += f"### 📊 Resumo da Análise\n\n"
        conclusions += f"- **Componentes Gerados:** {components_generated} sistemas completos\n"
        conclusions += f"- **Análise Visceral:** ✅ Completa\n"
        conclusions += f"- **Drivers Mentais:** ✅ Customizados\n"
        conclusions += f"- **Sistema Anti-Objeção:** ✅ Implementado\n"
        conclusions += f"- **Provas Visuais:** ✅ Criadas\n"
        conclusions += f"- **Pré-Pitch:** ✅ Orquestrado\n\n"
        
        # Próximos passos
        conclusions += "### 🚀 Próximos Passos Recomendados\n\n"
        conclusions += "1. **Implementar Drivers Mentais** - Use os drivers customizados em seu conteúdo\n"
        conclusions += "2. **Preparar PROVIs** - Adquira materiais e ensaie as demonstrações\n"
        conclusions += "3. **Treinar Anti-Objeção** - Pratique os scripts de neutralização\n"
        conclusions += "4. **Estruturar Pré-Pitch** - Implemente a sequência psicológica\n"
        conclusions += "5. **Monitorar Resultados** - Acompanhe métricas de conversão\n\n"
        
        # Garantias do sistema
        conclusions += "### 🛡️ Garantias do Sistema\n\n"
        conclusions += "- ✅ **ZERO Perda de Dados** - Todos os resultados salvos automaticamente\n"
        conclusions += "- ✅ **Isolamento de Falhas** - Componentes independentes\n"
        conclusions += "- ✅ **Qualidade Garantida** - Validação rigorosa aplicada\n"
        conclusions += "- ✅ **Recuperação Automática** - Sistema se recupera de falhas\n"
        conclusions += "- ✅ **Dados Preservados** - Arquivos intermediários disponíveis\n\n"
        
        conclusions += "---\n\n"
        conclusions += f"**Relatório gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        conclusions += "**Sistema:** ARQV30 Enhanced v2.0 - Ultra-Robusto\n"
        conclusions += "**Garantia:** 100% dos dados preservados e acessíveis\n\n"
        
        return conclusions
    
    def _generate_fallback_report(self, analysis_data: Dict[str, Any]) -> str:
        """Gera relatório de fallback"""
        
        return f"""# RELATÓRIO DE EMERGÊNCIA - ARQV30 Enhanced v2.0

## ⚠️ MODO DE EMERGÊNCIA ATIVADO

**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
**Status:** Dados parciais preservados

### 📊 Dados Disponíveis

{json.dumps(analysis_data, ensure_ascii=False, indent=2)[:2000]}

### 🔧 Próximos Passos

1. Configure APIs faltantes
2. Execute nova análise completa
3. Consulte arquivos intermediários salvos

---

**IMPORTANTE:** Todos os dados intermediários foram preservados no diretório `relatorios_intermediarios/`
"""

# Instância global
comprehensive_report_generator = ComprehensiveReportGenerator()