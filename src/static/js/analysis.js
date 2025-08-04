// ARQV30 Enhanced v2.0 - Analysis JavaScript
// Sistema completo de análise com todos os componentes do documento

class AnalysisManager {
    constructor() {
        this.currentAnalysis = null;
        this.sessionId = null;
        this.progressInterval = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.checkSystemStatus();
    }

    setupEventListeners() {
        // Form submission
        const form = document.getElementById('analysisForm');
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        }

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                this.startAnalysis();
            }
            if (e.ctrlKey && e.key === 's') {
                e.preventDefault();
                if (this.currentAnalysis) {
                    this.saveAnalysisLocally(this.currentAnalysis);
                }
            }
        });

        // PDF download button
        const pdfBtn = document.getElementById('downloadPdfBtn');
        if (pdfBtn) {
            pdfBtn.addEventListener('click', () => this.downloadPDF());
        }
    }

    async handleFormSubmit(e) {
        e.preventDefault();
        await this.startAnalysis();
    }

    async startAnalysis() {
        try {
            // Collect form data
            const formData = this.collectFormData();
            
            if (!formData.segmento) {
                this.showError('Segmento é obrigatório');
                return;
            }

            // Generate session ID
            this.sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
            formData.session_id = this.sessionId;

            // Show progress
            this.showProgress();
            this.startProgressTracking();

            // Start analysis
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                const result = await response.json();
                this.handleAnalysisSuccess(result);
            } else {
                const error = await response.json();
                this.handleAnalysisError(error);
            }

        } catch (error) {
            console.error('Analysis error:', error);
            this.handleAnalysisError({ message: error.message });
        }
    }

    collectFormData() {
        const form = document.getElementById('analysisForm');
        const formData = new FormData(form);
        const data = {};

        // Convert FormData to object
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }

        // Add uploaded files
        if (window.uploadManager) {
            data.uploaded_files = window.uploadManager.getUploadedFiles();
        }

        return data;
    }

    showProgress() {
        document.getElementById('progressArea').style.display = 'block';
        document.querySelector('.analysis-section').style.display = 'none';
        
        // Reset progress
        this.updateProgress(0, 'Iniciando análise ultra-detalhada...');
    }

    hideProgress() {
        document.getElementById('progressArea').style.display = 'none';
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
    }

    startProgressTracking() {
        let step = 0;
        const steps = [
            '🔍 Coletando dados do formulário',
            '📊 Processando anexos inteligentes', 
            '🌐 Realizando pesquisa profunda massiva',
            '🧠 Analisando com múltiplas IAs',
            '👤 Criando avatar arqueológico completo',
            '🧠 Gerando drivers mentais customizados',
            '🎭 Desenvolvendo provas visuais instantâneas',
            '🛡️ Construindo sistema anti-objeção',
            '🎯 Arquitetando pré-pitch invisível',
            '⚔️ Mapeando concorrência profunda',
            '📈 Calculando métricas e projeções',
            '🔮 Predizendo futuro do mercado',
            '✨ Consolidando insights exclusivos'
        ];

        this.progressInterval = setInterval(() => {
            if (step < steps.length) {
                this.updateProgress((step / steps.length) * 100, steps[step]);
                step++;
            }
        }, 3000); // Update every 3 seconds
    }

    updateProgress(percentage, message) {
        const progressFill = document.querySelector('.progress-fill');
        const currentStep = document.getElementById('currentStep');
        const stepCounter = document.getElementById('stepCounter');

        if (progressFill) {
            progressFill.style.width = percentage + '%';
        }

        if (currentStep) {
            currentStep.textContent = message;
        }

        if (stepCounter) {
            const currentStepNum = Math.floor((percentage / 100) * 13);
            stepCounter.textContent = `${currentStepNum}/13`;
        }

        // Update estimated time
        const estimatedTime = document.getElementById('estimatedTime');
        if (estimatedTime && percentage > 0) {
            const remainingTime = Math.max(0, (100 - percentage) * 2); // Rough estimate
            const minutes = Math.floor(remainingTime / 60);
            const seconds = Math.floor(remainingTime % 60);
            estimatedTime.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        }
    }

    handleAnalysisSuccess(result) {
        this.hideProgress();
        this.currentAnalysis = result;
        
        // Show results
        this.displayResults(result);
        
        // Show success message
        this.showSuccess('Análise ultra-detalhada concluída com sucesso!');
        
        // Enable PDF download if quality is sufficient
        this.checkPDFEligibility(result);
    }

    handleAnalysisError(error) {
        this.hideProgress();
        
        // Show error
        this.showError(`Erro na análise: ${error.message || 'Erro desconhecido'}`);
        
        // Show form again
        document.querySelector('.analysis-section').style.display = 'block';
        
        // If partial data was saved, show recovery option
        if (error.dados_recuperados || error.relatorio_parcial) {
            this.showPartialDataRecovery(error);
        }
    }

    displayResults(analysis) {
        const resultsArea = document.getElementById('resultsArea');
        resultsArea.style.display = 'block';
        
        // Clear previous results
        this.clearPreviousResults();
        
        // Display each component
        this.displayComponent('avatarResults', 'Avatar Ultra-Detalhado', analysis.avatar_ultra_detalhado, 'fas fa-user');
        
        // Sistema Completo de Drivers
        this.displayComponent('driversResults', 'Sistema Completo de Drivers Mentais', 
            analysis.drivers_mentais_sistema_completo || analysis.drivers_mentais_customizados, 'fas fa-brain');
        
        // Arsenal Completo Anti-Objeção
        this.displayComponent('antiObjectionResults', 'Arsenal Completo Anti-Objeção', 
            analysis.arsenal_anti_objecao_completo || analysis.sistema_anti_objecao, 'fas fa-shield-alt');
        
        // Sistema Completo de Pré-Pitch
        this.displayComponent('prePitchResults', 'Sistema Completo de Pré-Pitch', 
            analysis.sistema_pre_pitch_completo || analysis.pre_pitch_invisivel, 'fas fa-theater-masks');
        
        // Sistema Completo de PROVIs
        this.displayComponent('visualProofsResults', 'Sistema Completo de PROVIs', 
            analysis.sistema_provis_completo || analysis.provas_visuais_sugeridas, 'fas fa-eye');
        
        // Análise Forense Completa
        this.displayComponent('forensicResults', 'Análise Forense Completa (12 Camadas)', 
            analysis.analise_forense_completa || analysis.analise_forense_devastadora, 'fas fa-search');
        
        // Dashboard do Avatar
        this.displayComponent('avatarDashboardResults', 'Dashboard Arqueológico do Avatar', 
            analysis.dashboard_avatar_completo, 'fas fa-chart-pie');
        
        // Engenharia Reversa Psicológica
        this.displayComponent('psychologyResults', 'Engenharia Reversa Psicológica', 
            analysis.engenharia_reversa_psicologica, 'fas fa-brain');
        
        // Existing components
        this.displayComponent('competitionResults', 'Análise de Concorrência', analysis.analise_concorrencia_detalhada, 'fas fa-chess');
        this.displayComponent('positioningResults', 'Escopo e Posicionamento', analysis.escopo, 'fas fa-bullseye');
        this.displayComponent('keywordsResults', 'Estratégia de Palavras-Chave', analysis.estrategia_palavras_chave, 'fas fa-key');
        this.displayComponent('metricsResults', 'Métricas de Performance', analysis.metricas_performance_detalhadas, 'fas fa-chart-line');
        this.displayComponent('actionPlanResults', 'Plano de Ação', analysis.plano_acao_detalhado, 'fas fa-tasks');
        this.displayComponent('futureResults', 'Predições do Futuro', analysis.predicoes_futuro_completas, 'fas fa-crystal-ball');
        this.displayComponent('insightsResults', 'Insights Exclusivos', analysis.insights_exclusivos, 'fas fa-lightbulb');
        this.displayComponent('researchResults', 'Pesquisa Web Massiva', analysis.pesquisa_web_massiva, 'fas fa-globe');
        this.displayComponent('metadataResults', 'Metadados da Análise', analysis.metadata, 'fas fa-info-circle');
        
        // Display completeness report
        this.displayCompletenessReport(analysis.completude_documento);
        
        // Scroll to results
        resultsArea.scrollIntoView({ behavior: 'smooth' });
    }

    displayComponent(containerId, title, data, icon) {
        const container = document.getElementById(containerId);
        if (!container || !data) return;

        const section = this.createResultSection(title, data, icon);
        container.innerHTML = '';
        container.appendChild(section);
    }

    createResultSection(title, data, icon) {
        const section = document.createElement('div');
        section.className = 'result-section';

        const header = document.createElement('div');
        header.className = 'result-section-header';
        header.innerHTML = `
            <i class="${icon}"></i>
            <h4>${title}</h4>
        `;

        const content = document.createElement('div');
        content.className = 'result-section-content';
        content.innerHTML = this.formatComponentData(data, title);

        section.appendChild(header);
        section.appendChild(content);

        return section;
    }

    formatComponentData(data, title) {
        if (!data) return '<p>Dados não disponíveis</p>';

        let html = '';

        // Format based on component type
        if (title.includes('Avatar')) {
            html = this.formatAvatarData(data);
        } else if (title.includes('Drivers')) {
            html = this.formatDriversData(data);
        } else if (title.includes('Anti-Objeção')) {
            html = this.formatAntiObjectionData(data);
        } else if (title.includes('Pré-Pitch')) {
            html = this.formatPrePitchData(data);
        } else if (title.includes('PROVIs')) {
            html = this.formatProvisData(data);
        } else if (title.includes('Forense')) {
            html = this.formatForensicData(data);
        } else if (title.includes('Dashboard')) {
            html = this.formatDashboardData(data);
        } else if (title.includes('Psicológica')) {
            html = this.formatPsychologyData(data);
        } else if (title.includes('Insights')) {
            html = this.formatInsightsData(data);
        } else if (title.includes('Pesquisa')) {
            html = this.formatResearchData(data);
        } else {
            html = this.formatGenericData(data);
        }

        return html;
    }

    formatDriversData(data) {
        let html = '';

        if (data.drivers_emocionais_primarios) {
            html += '<h5><i class="fas fa-fire"></i> Drivers Emocionais Primários</h5>';
            html += '<div class="drivers-grid">';
            
            data.drivers_emocionais_primarios.forEach(driver => {
                html += `
                    <div class="driver-card">
                        <h4>${driver.nome || 'Driver Emocional'}</h4>
                        <div class="driver-content">
                            <p><strong>Gatilho Central:</strong> ${driver.gatilho_central || 'N/A'}</p>
                            <p><strong>Definição:</strong> ${driver.definicao_visceral || 'N/A'}</p>
                            
                            ${driver.roteiro_ativacao ? `
                                <div class="driver-script">
                                    <h6><i class="fas fa-play"></i> Roteiro de Ativação</h6>
                                    <p><strong>Pergunta:</strong> ${driver.roteiro_ativacao.pergunta_abertura || 'N/A'}</p>
                                    <p><strong>História:</strong> ${driver.roteiro_ativacao.historia_analogia || 'N/A'}</p>
                                    <p><strong>Comando:</strong> ${driver.roteiro_ativacao.comando_acao || 'N/A'}</p>
                                </div>
                            ` : ''}
                            
                            ${driver.frases_ancoragem ? `
                                <div class="anchor-phrases">
                                    <h6><i class="fas fa-anchor"></i> Frases de Ancoragem</h6>
                                    <ul>
                                        ${driver.frases_ancoragem.map(frase => `<li>"${frase}"</li>`).join('')}
                                    </ul>
                                </div>
                            ` : ''}
                        </div>
                    </div>
                `;
            });
            
            html += '</div>';
        }

        if (data.top_7_essenciais) {
            html += '<h5><i class="fas fa-star"></i> Top 7 Drivers Essenciais</h5>';
            html += '<div class="keyword-tags">';
            data.top_7_essenciais.forEach(driver => {
                html += `<span class="keyword-tag">${driver}</span>`;
            });
            html += '</div>';
        }

        return html;
    }

    formatAntiObjectionData(data) {
        let html = '';

        if (data.resumo_executivo) {
            html += '<h5><i class="fas fa-clipboard"></i> Resumo Executivo</h5>';
            if (data.resumo_executivo.top_5_objecoes_criticas) {
                html += '<h6>Top 5 Objeções Críticas:</h6>';
                html += '<ul class="insight-list">';
                data.resumo_executivo.top_5_objecoes_criticas.forEach(objecao => {
                    html += `<li class="insight-item"><i class="fas fa-exclamation-triangle"></i><span class="insight-text">${objecao}</span></li>`;
                });
                html += '</ul>';
            }
        }

        if (data.objecoes_universais) {
            html += '<h5><i class="fas fa-globe"></i> Objeções Universais</h5>';
            
            Object.entries(data.objecoes_universais).forEach(([tipo, dados]) => {
                html += `
                    <div class="info-card">
                        <strong>${tipo.toUpperCase()}</strong>
                        <span><strong>Objeção:</strong> ${dados.objecao || 'N/A'}</span>
                        <span><strong>Contra-ataque:</strong> ${dados.contra_ataque || 'N/A'}</span>
                        ${dados.scripts ? `
                            <ul>
                                ${dados.scripts.map(script => `<li>"${script}"</li>`).join('')}
                            </ul>
                        ` : ''}
                    </div>
                `;
            });
        }

        if (data.arsenal_emergencia) {
            html += '<h5><i class="fas fa-first-aid"></i> Arsenal de Emergência</h5>';
            html += '<ul class="insight-list">';
            data.arsenal_emergencia.forEach(frase => {
                html += `<li class="insight-item"><i class="fas fa-quote-left"></i><span class="insight-text">"${frase}"</span></li>`;
            });
            html += '</ul>';
        }

        return html;
    }

    formatPrePitchData(data) {
        let html = '';

        if (data.orquestracao_emocional && data.orquestracao_emocional.sequencia_psicologica) {
            html += '<h5><i class="fas fa-music"></i> Orquestração Emocional</h5>';
            html += '<div class="action-timeline">';
            
            data.orquestracao_emocional.sequencia_psicologica.forEach((fase, index) => {
                html += `
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div class="timeline-content">
                            <div class="timeline-title">
                                FASE ${index + 1}: ${fase.fase || 'FASE'}
                                <span class="timeline-duration">${fase.duracao || 'N/A'}</span>
                            </div>
                            <p><strong>Objetivo:</strong> ${fase.objetivo || 'N/A'}</p>
                            <p><strong>Intensidade:</strong> ${fase.intensidade || 'N/A'}</p>
                            <p><strong>Resultado Esperado:</strong> ${fase.resultado_esperado || 'N/A'}</p>
                            ${fase.drivers_utilizados ? `
                                <p><strong>Drivers:</strong> ${fase.drivers_utilizados.join(', ')}</p>
                            ` : ''}
                        </div>
                    </div>
                `;
            });
            
            html += '</div>';
        }

        if (data.roteiro_completo) {
            html += '<h5><i class="fas fa-script"></i> Roteiro Completo</h5>';
            
            Object.entries(data.roteiro_completo).forEach(([secao, dados]) => {
                if (typeof dados === 'object' && dados !== null) {
                    html += `
                        <div class="info-card">
                            <strong>${secao.replace('_', ' ').toUpperCase()}</strong>
                            <span><strong>Tempo:</strong> ${dados.tempo || 'N/A'}</span>
                            <span><strong>Objetivo:</strong> ${dados.objetivo || 'N/A'}</span>
                            <span><strong>Script:</strong> ${dados.script || 'N/A'}</span>
                        </div>
                    `;
                }
            });
        }

        return html;
    }

    formatProvisData(data) {
        let html = '';

        if (data.arsenal_provis) {
            html += '<h5><i class="fas fa-magic"></i> Arsenal de PROVIs</h5>';
            
            data.arsenal_provis.forEach((provi, index) => {
                html += `
                    <div class="info-card">
                        <strong>${provi.nome || `PROVI #${index + 1}`}</strong>
                        <span><strong>Conceito-Alvo:</strong> ${provi.conceito_alvo || 'N/A'}</span>
                        <span><strong>Categoria:</strong> ${provi.categoria || 'N/A'}</span>
                        <span><strong>Prioridade:</strong> ${provi.prioridade || 'N/A'}</span>
                        <span><strong>Experimento:</strong> ${provi.experimento || 'N/A'}</span>
                        
                        ${provi.materiais ? `
                            <span><strong>Materiais:</strong></span>
                            <ul>
                                ${provi.materiais.map(material => `<li>${material}</li>`).join('')}
                            </ul>
                        ` : ''}
                    </div>
                `;
            });
        }

        if (data.categorias_provis) {
            html += '<h5><i class="fas fa-folder"></i> Categorias de PROVIs</h5>';
            
            if (data.categorias_provis.destruidoras_objecao) {
                html += '<h6>Destruidoras de Objeção:</h6>';
                data.categorias_provis.destruidoras_objecao.forEach(destruidora => {
                    html += `
                        <div class="info-card">
                            <strong>Contra: "${destruidora.contra}"</strong>
                            <span>Experimentos: ${destruidora.experimentos.join(', ')}</span>
                        </div>
                    `;
                });
            }
        }

        return html;
    }

    formatForensicData(data) {
        let html = '';

        if (data.resumo_executivo) {
            html += '<h5><i class="fas fa-gavel"></i> Resumo Executivo</h5>';
            html += `
                <div class="info-card">
                    <strong>Veredicto Geral</strong>
                    <span>${data.resumo_executivo.veredicto_geral || 'N/A'}</span>
                </div>
            `;
            
            if (data.resumo_executivo.top_3_pontos_fortes) {
                html += '<h6>Top 3 Pontos Mais Fortes:</h6>';
                html += '<ul class="insight-list">';
                data.resumo_executivo.top_3_pontos_fortes.forEach(ponto => {
                    html += `<li class="insight-item"><i class="fas fa-star"></i><span class="insight-text">${ponto}</span></li>`;
                });
                html += '</ul>';
            }
        }

        if (data.dna_conversao) {
            html += '<h5><i class="fas fa-dna"></i> DNA da Conversão</h5>';
            html += `
                <div class="info-card">
                    <strong>Fórmula Estrutural</strong>
                    <span>${data.dna_conversao.formula_estrutural || 'N/A'}</span>
                </div>
            `;
            
            if (data.dna_conversao.sequencia_gatilhos) {
                html += '<h6>Sequência de Gatilhos:</h6>';
                html += '<ul class="insight-list">';
                data.dna_conversao.sequencia_gatilhos.forEach(gatilho => {
                    html += `<li class="insight-item"><i class="fas fa-bolt"></i><span class="insight-text">${gatilho}</span></li>`;
                });
                html += '</ul>';
            }
        }

        if (data.metricas_objetivas) {
            html += '<h5><i class="fas fa-ruler"></i> Métricas Objetivas</h5>';
            html += '<div class="metadata-grid">';
            
            Object.entries(data.metricas_objetivas).forEach(([key, value]) => {
                html += `
                    <div class="metadata-item">
                        <span class="metadata-label">${key.replace('_', ' ')}</span>
                        <span class="metadata-value">${value}</span>
                    </div>
                `;
            });
            
            html += '</div>';
        }

        return html;
    }

    formatDashboardData(data) {
        let html = '';

        if (data.visao_geral) {
            html += '<h5><i class="fas fa-chart-pie"></i> Visão Geral</h5>';
            html += `
                <div class="info-card">
                    <strong>Público Analisado</strong>
                    <span>${data.visao_geral.publico_analisado || 'N/A'}</span>
                </div>
            `;
            
            if (data.visao_geral.distribuicao_faturamento) {
                html += '<h6>Distribuição por Faturamento:</h6>';
                html += '<div class="metadata-grid">';
                
                Object.entries(data.visao_geral.distribuicao_faturamento).forEach(([faixa, percentual]) => {
                    html += `
                        <div class="metadata-item">
                            <span class="metadata-label">${faixa.replace('_', ' ')}</span>
                            <span class="metadata-value">${percentual}</span>
                        </div>
                    `;
                });
                
                html += '</div>';
            }
        }

        if (data.analise_dores && data.analise_dores.top_10_dores_estruturadas) {
            html += '<h5><i class="fas fa-heartbeat"></i> Top 10 Dores Estruturadas</h5>';
            html += '<ul class="insight-list">';
            
            data.analise_dores.top_10_dores_estruturadas.forEach((dor, index) => {
                html += `
                    <li class="insight-item">
                        <i class="fas fa-exclamation-circle"></i>
                        <div class="insight-text">
                            <strong>${index + 1}. ${dor.dor || 'Dor'}</strong><br>
                            <small>Frequência: ${dor.frequencia || 'N/A'} | Intensidade: ${dor.intensidade || 'N/A'}</small><br>
                            <em>${dor.contexto || 'N/A'}</em>
                        </div>
                    </li>
                `;
            });
            
            html += '</ul>';
        }

        return html;
    }

    formatPsychologyData(data) {
        let html = '';

        if (data.perfil_psicologico_profundo) {
            html += '<h5><i class="fas fa-user-secret"></i> Perfil Psicológico Profundo</h5>';
            const perfil = data.perfil_psicologico_profundo;
            
            html += `
                <div class="avatar-grid">
                    <div class="avatar-card">
                        <h5><i class="fas fa-id-card"></i> Identificação</h5>
                        <div class="avatar-item">
                            <span class="avatar-label">Nome Fictício</span>
                            <span class="avatar-value">${perfil.nome_ficticio || 'N/A'}</span>
                        </div>
                        <div class="avatar-item">
                            <span class="avatar-label">Idade</span>
                            <span class="avatar-value">${perfil.idade_aproximada || 'N/A'}</span>
                        </div>
                        <div class="avatar-item">
                            <span class="avatar-label">Ocupação</span>
                            <span class="avatar-value">${perfil.ocupacao_situacao || 'N/A'}</span>
                        </div>
                    </div>
                </div>
            `;
        }

        if (data.feridas_abertas) {
            html += '<h5><i class="fas fa-heart-broken"></i> As Feridas Abertas</h5>';
            html += '<ul class="insight-list">';
            data.feridas_abertas.forEach(ferida => {
                html += `<li class="insight-item"><i class="fas fa-bandage"></i><span class="insight-text">${ferida}</span></li>`;
            });
            html += '</ul>';
        }

        if (data.sonhos_proibidos) {
            html += '<h5><i class="fas fa-star"></i> Os Sonhos Proibidos</h5>';
            html += '<ul class="insight-list">';
            data.sonhos_proibidos.forEach(sonho => {
                html += `<li class="insight-item"><i class="fas fa-magic"></i><span class="insight-text">${sonho}</span></li>`;
            });
            html += '</ul>';
        }

        if (data.dialeto_alma) {
            html += '<h5><i class="fas fa-comments"></i> O Dialeto da Alma</h5>';
            
            if (data.dialeto_alma.frases_dores) {
                html += '<h6>Frases Típicas Sobre Dores:</h6>';
                html += '<ul class="insight-list">';
                data.dialeto_alma.frases_dores.forEach(frase => {
                    html += `<li class="insight-item"><i class="fas fa-quote-left"></i><span class="insight-text">"${frase}"</span></li>`;
                });
                html += '</ul>';
            }
        }

        return html;
    }

    formatAvatarData(data) {
        let html = '';

        if (data.perfil_demografico) {
            html += '<h5><i class="fas fa-chart-bar"></i> Perfil Demográfico</h5>';
            html += '<div class="avatar-grid">';
            html += '<div class="avatar-card">';
            html += '<h5><i class="fas fa-users"></i> Demografia</h5>';
            
            Object.entries(data.perfil_demografico).forEach(([key, value]) => {
                html += `
                    <div class="avatar-item">
                        <span class="avatar-label">${key.replace('_', ' ')}</span>
                        <span class="avatar-value">${value}</span>
                    </div>
                `;
            });
            
            html += '</div></div>';
        }

        if (data.dores_viscerais) {
            html += '<h5><i class="fas fa-heart-broken"></i> Dores Viscerais</h5>';
            html += '<ul class="insight-list">';
            data.dores_viscerais.forEach(dor => {
                html += `<li class="insight-item"><i class="fas fa-exclamation-triangle"></i><span class="insight-text">${dor}</span></li>`;
            });
            html += '</ul>';
        }

        if (data.desejos_secretos) {
            html += '<h5><i class="fas fa-star"></i> Desejos Secretos</h5>';
            html += '<ul class="insight-list">';
            data.desejos_secretos.forEach(desejo => {
                html += `<li class="insight-item"><i class="fas fa-heart"></i><span class="insight-text">${desejo}</span></li>`;
            });
            html += '</ul>';
        }

        return html;
    }

    formatInsightsData(data) {
        if (!Array.isArray(data)) return '<p>Formato de insights inválido</p>';

        let html = '<div class="insights-showcase">';
        
        data.forEach((insight, index) => {
            html += `
                <div class="insight-card">
                    <div class="insight-number">${index + 1}</div>
                    <div class="insight-content">${insight}</div>
                </div>
            `;
        });
        
        html += '</div>';
        return html;
    }

    formatResearchData(data) {
        let html = '';

        if (data.estatisticas) {
            html += '<h5><i class="fas fa-chart-line"></i> Estatísticas da Pesquisa</h5>';
            html += '<div class="stats-grid">';
            
            Object.entries(data.estatisticas).forEach(([key, value]) => {
                html += `
                    <div class="stat-item">
                        <span class="stat-label">${key.replace('_', ' ')}</span>
                        <span class="stat-value">${typeof value === 'number' ? value.toLocaleString() : value}</span>
                    </div>
                `;
            });
            
            html += '</div>';
        }

        if (data.fontes) {
            html += '<h5><i class="fas fa-link"></i> Principais Fontes</h5>';
            html += '<div class="results-list">';
            
            data.fontes.slice(0, 10).forEach(fonte => {
                html += `
                    <div class="result-item">
                        <h5>${fonte.title || 'Sem título'}</h5>
                        <div class="result-url">${fonte.url || 'N/A'}</div>
                        ${fonte.quality_score ? `<div class="result-source">Qualidade: ${fonte.quality_score.toFixed(1)}%</div>` : ''}
                    </div>
                `;
            });
            
            html += '</div>';
        }

        return html;
    }

    formatGenericData(data) {
        if (typeof data === 'string') {
            return `<p>${data}</p>`;
        }

        if (Array.isArray(data)) {
            let html = '<ul class="insight-list">';
            data.forEach(item => {
                html += `<li class="insight-item"><i class="fas fa-chevron-right"></i><span class="insight-text">${item}</span></li>`;
            });
            html += '</ul>';
            return html;
        }

        if (typeof data === 'object' && data !== null) {
            let html = '<div class="metadata-grid">';
            
            Object.entries(data).forEach(([key, value]) => {
                if (typeof value === 'object') {
                    html += `
                        <div class="info-card">
                            <strong>${key.replace('_', ' ')}</strong>
                            <span>${JSON.stringify(value, null, 2)}</span>
                        </div>
                    `;
                } else {
                    html += `
                        <div class="metadata-item">
                            <span class="metadata-label">${key.replace('_', ' ')}</span>
                            <span class="metadata-value">${value}</span>
                        </div>
                    `;
                }
            });
            
            html += '</div>';
            return html;
        }

        return `<p>${JSON.stringify(data, null, 2)}</p>`;
    }

    displayCompletenessReport(completeness) {
        if (!completeness) return;

        const container = document.getElementById('completenessResults') || this.createCompletenessContainer();
        
        const html = `
            <div class="result-section">
                <div class="result-section-header">
                    <i class="fas fa-check-circle"></i>
                    <h4>Relatório de Completude do Documento</h4>
                </div>
                <div class="result-section-content">
                    <div class="data-quality-indicator">
                        <span class="quality-label">Taxa de Completude:</span>
                        <span class="quality-value ${completeness.todos_componentes_incluidos ? 'real-data' : 'simulated-data'}">
                            ${completeness.taxa_completude.toFixed(1)}%
                        </span>
                    </div>
                    
                    <div class="metadata-grid">
                        <div class="metadata-item">
                            <span class="metadata-label">Componentes Requeridos</span>
                            <span class="metadata-value">${completeness.componentes_requeridos}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Componentes Presentes</span>
                            <span class="metadata-value">${completeness.componentes_presentes}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Status</span>
                            <span class="metadata-value">${completeness.todos_componentes_incluidos ? '✅ COMPLETO' : '⚠️ PARCIAL'}</span>
                        </div>
                    </div>
                    
                    ${completeness.componentes_ausentes.length > 0 ? `
                        <h6>Componentes Ausentes:</h6>
                        <ul class="insight-list">
                            ${completeness.componentes_ausentes.map(comp => 
                                `<li class="insight-item"><i class="fas fa-exclamation-triangle"></i><span class="insight-text">${comp}</span></li>`
                            ).join('')}
                        </ul>
                    ` : ''}
                </div>
            </div>
        `;
        
        container.innerHTML = html;
    }

    createCompletenessContainer() {
        const container = document.createElement('div');
        container.id = 'completenessResults';
        container.className = 'result-container';
        
        const resultsContent = document.querySelector('.results-content');
        if (resultsContent) {
            resultsContent.insertBefore(container, resultsContent.firstChild);
        }
        
        return container;
    }

    clearPreviousResults() {
        const containers = document.querySelectorAll('.result-container');
        containers.forEach(container => {
            container.innerHTML = '';
        });
    }

    checkPDFEligibility(analysis) {
        // Check if analysis has sufficient quality for PDF
        const hasAvatar = analysis.avatar_ultra_detalhado;
        const hasInsights = analysis.insights_exclusivos && analysis.insights_exclusivos.length >= 3;
        const hasDrivers = analysis.drivers_mentais_sistema_completo || analysis.drivers_mentais_customizados;
        
        const pdfBtn = document.getElementById('downloadPdfBtn');
        if (pdfBtn) {
            if (hasAvatar && hasInsights) {
                pdfBtn.style.display = 'inline-flex';
            } else {
                pdfBtn.style.display = 'none';
            }
        }
    }

    async downloadPDF() {
        if (!this.currentAnalysis) {
            this.showError('Nenhuma análise disponível para download');
            return;
        }

        try {
            const response = await fetch('/api/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.currentAnalysis)
            });

            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `analise_mercado_${new Date().toISOString().slice(0, 10)}.pdf`;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(a);
                
                this.showSuccess('PDF baixado com sucesso!');
            } else {
                const error = await response.json();
                this.showError(`Erro ao gerar PDF: ${error.message}`);
            }
        } catch (error) {
            console.error('PDF download error:', error);
            this.showError('Erro ao baixar PDF');
        }
    }

    saveAnalysisLocally(analysis) {
        try {
            const dataStr = JSON.stringify(analysis, null, 2);
            const dataBlob = new Blob([dataStr], { type: 'application/json' });
            const url = URL.createObjectURL(dataBlob);
            
            const a = document.createElement('a');
            a.href = url;
            a.download = `analise_completa_${new Date().toISOString().slice(0, 10)}.json`;
            document.body.appendChild(a);
            a.click();
            
            URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            this.showSuccess('Análise salva localmente!');
        } catch (error) {
            console.error('Save error:', error);
            this.showError('Erro ao salvar análise');
        }
    }

    showPartialDataRecovery(error) {
        const recoveryHtml = `
            <div class="info-card" style="margin-top: 20px; border-left: 4px solid #ffd700;">
                <strong><i class="fas fa-exclamation-triangle"></i> Dados Parciais Disponíveis</strong>
                <span>Alguns dados foram salvos automaticamente e podem ser recuperados.</span>
                <button class="btn-secondary" onclick="analysisManager.recoverPartialData('${error.session_id}')">
                    <i class="fas fa-download"></i> Recuperar Dados Parciais
                </button>
            </div>
        `;
        
        const resultsArea = document.getElementById('resultsArea');
        if (resultsArea) {
            resultsArea.innerHTML = recoveryHtml;
            resultsArea.style.display = 'block';
        }
    }

    async recoverPartialData(sessionId) {
        try {
            const response = await fetch(`/api/get_analysis_files/${sessionId}`);
            if (response.ok) {
                const data = await response.json();
                this.showSuccess('Dados parciais recuperados!');
                console.log('Dados recuperados:', data);
            }
        } catch (error) {
            this.showError('Erro ao recuperar dados parciais');
        }
    }

    // Test functions
    async testExtraction() {
        try {
            const response = await fetch('/api/test_extraction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: 'https://g1.globo.com/tecnologia/' })
            });
            
            const result = await response.json();
            console.log('Teste de extração:', result);
            this.showSuccess(`Extração testada: ${result.success ? 'Sucesso' : 'Falha'}`);
        } catch (error) {
            this.showError('Erro no teste de extração');
        }
    }

    async testSearch() {
        try {
            const response = await fetch('/api/test_search', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: 'mercado digital Brasil 2024' })
            });
            
            const result = await response.json();
            console.log('Teste de busca:', result);
            this.showSuccess(`Busca testada: ${result.results_count} resultados`);
        } catch (error) {
            this.showError('Erro no teste de busca');
        }
    }

    async showExtractorStats() {
        try {
            const response = await fetch('/api/extractor_stats');
            const result = await response.json();
            console.log('Estatísticas dos extratores:', result);
            
            let statsHtml = '<h4>📊 Estatísticas dos Extratores</h4>';
            if (result.stats) {
                Object.entries(result.stats).forEach(([extractor, stats]) => {
                    if (extractor !== 'global') {
                        statsHtml += `
                            <div class="info-card">
                                <strong>${extractor}</strong>
                                <span>Disponível: ${stats.available ? '✅' : '❌'}</span>
                                <span>Sucessos: ${stats.success || 0}</span>
                                <span>Falhas: ${stats.failed || 0}</span>
                                <span>Taxa de Sucesso: ${stats.success_rate || 0}%</span>
                            </div>
                        `;
                    }
                });
            }
            
            this.showModal('Estatísticas dos Extratores', statsHtml);
        } catch (error) {
            this.showError('Erro ao obter estatísticas');
        }
    }

    async resetExtractors() {
        try {
            const response = await fetch('/api/reset_extractors', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({})
            });
            
            const result = await response.json();
            this.showSuccess('Extratores resetados com sucesso!');
        } catch (error) {
            this.showError('Erro ao resetar extratores');
        }
    }

    async checkSystemStatus() {
        try {
            const response = await fetch('/api/status');
            const status = await response.json();
            
            this.updateStatusIndicator(status.status);
            this.updateAPIStatus(status.systems);
            this.updateExtractorStatus();
            
        } catch (error) {
            console.error('Status check error:', error);
            this.updateStatusIndicator('error');
        }
    }

    updateStatusIndicator(status) {
        const indicator = document.getElementById('statusIndicator');
        const statusText = document.getElementById('statusText');
        
        if (indicator && statusText) {
            indicator.className = `status-indicator ${status}`;
            
            const statusMessages = {
                'healthy': 'Sistema Online',
                'degraded': 'Funcionalidade Limitada',
                'error': 'Sistema Offline'
            };
            
            statusText.textContent = statusMessages[status] || 'Status Desconhecido';
        }
    }

    updateAPIStatus(systems) {
        const apiStatus = document.getElementById('apiStatus');
        if (apiStatus && systems) {
            const aiCount = systems.ai_providers ? systems.ai_providers.available_count : 0;
            const searchCount = systems.search_providers ? systems.search_providers.available_count : 0;
            
            apiStatus.innerHTML = `
                <i class="fas fa-cog"></i>
                <span>APIs: ${aiCount} IA + ${searchCount} Busca</span>
            `;
        }
    }

    updateExtractorStatus() {
        const extractorStatus = document.getElementById('extractorStatus');
        if (extractorStatus) {
            fetch('/api/extractor_stats')
                .then(response => response.json())
                .then(result => {
                    if (result.stats && result.stats.global) {
                        const successRate = result.stats.global.success_rate || 0;
                        extractorStatus.innerHTML = `
                            <i class="fas fa-download"></i>
                            <span>Extratores: ${successRate.toFixed(1)}% sucesso</span>
                        `;
                    }
                })
                .catch(() => {
                    extractorStatus.innerHTML = `
                        <i class="fas fa-exclamation-triangle"></i>
                        <span>Extratores: Status desconhecido</span>
                    `;
                });
        }
    }

    showSuccess(message) {
        this.showAlert(message, 'success');
    }

    showError(message) {
        this.showAlert(message, 'error');
    }

    showAlert(message, type) {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
            ${message}
        `;
        
        document.body.appendChild(alert);
        
        setTimeout(() => {
            alert.remove();
        }, 5000);
    }

    showModal(title, content) {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        `;
        
        modal.innerHTML = `
            <div style="
                background: var(--bg-elevated);
                border-radius: var(--radius-xl);
                padding: var(--spacing-8);
                max-width: 800px;
                max-height: 80vh;
                overflow-y: auto;
                width: 90%;
            ">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--spacing-6);">
                    <h3>${title}</h3>
                    <button onclick="this.closest('.modal').remove()" style="
                        background: none;
                        border: none;
                        color: var(--text-secondary);
                        font-size: var(--font-size-xl);
                        cursor: pointer;
                    ">×</button>
                </div>
                <div>${content}</div>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        // Close on background click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }
}

// Initialize analysis manager
document.addEventListener('DOMContentLoaded', () => {
    window.analysisManager = new AnalysisManager();
});

// Global app object for compatibility
window.app = {
    sessionId: null,
    
    showError: (message) => {
        if (window.analysisManager) {
            window.analysisManager.showError(message);
        } else {
            console.error(message);
        }
    },
    
    showSuccess: (message) => {
        if (window.analysisManager) {
            window.analysisManager.showSuccess(message);
        } else {
            console.log(message);
        }
    },
    
    removeFile: (fileId) => {
        // File removal handled by upload manager
        console.log('File removed:', fileId);
    },
    
    checkSystemHealth: async () => {
        try {
            const response = await fetch('/api/health');
            return await response.json();
        } catch (error) {
            console.error('Health check error:', error);
            return { status: 'error' };
        }
    }
};