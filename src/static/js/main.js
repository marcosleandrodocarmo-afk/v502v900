// ARQV30 Enhanced v2.0 - Main JavaScript
// Sistema principal de interface e interação

class ARQVApp {
    constructor() {
        this.sessionId = null;
        this.currentAnalysis = null;
        this.progressInterval = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.checkSystemStatus();
        this.generateSessionId();
    }

    generateSessionId() {
        this.sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        console.log('Session ID gerado:', this.sessionId);
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
        });

        // PDF download button
        const pdfBtn = document.getElementById('downloadPdfBtn');
        if (pdfBtn) {
            pdfBtn.addEventListener('click', () => this.downloadPDF());
        }

        // Save JSON button
        const saveBtn = document.getElementById('saveJsonBtn');
        if (saveBtn) {
            saveBtn.addEventListener('click', () => this.saveAnalysisLocally());
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

            // Add session ID
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

            const result = await response.json();

            if (response.ok) {
                this.handleAnalysisSuccess(result);
            } else {
                this.handleAnalysisError(result);
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
        const progressArea = document.getElementById('progressArea');
        const analysisSection = document.querySelector('.analysis-section');
        
        if (progressArea) progressArea.style.display = 'block';
        if (analysisSection) analysisSection.style.display = 'none';
        
        // Reset progress
        this.updateProgress(0, 'Iniciando análise ultra-detalhada...');
    }

    hideProgress() {
        const progressArea = document.getElementById('progressArea');
        if (progressArea) progressArea.style.display = 'none';
        
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
        }, 3000);
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
            const remainingTime = Math.max(0, (100 - percentage) * 2);
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
        
        // Enable buttons
        this.enableResultButtons();
    }

    handleAnalysisError(error) {
        this.hideProgress();
        
        // Show error
        this.showError(`Erro na análise: ${error.message || 'Erro desconhecido'}`);
        
        // Show form again
        const analysisSection = document.querySelector('.analysis-section');
        if (analysisSection) analysisSection.style.display = 'block';
        
        // If partial data was saved, show recovery option
        if (error.dados_recuperados || error.relatorio_parcial) {
            this.showPartialDataRecovery(error);
        }
    }

    displayResults(analysis) {
        const resultsArea = document.getElementById('resultsArea');
        if (resultsArea) {
            resultsArea.style.display = 'block';
            resultsArea.scrollIntoView({ behavior: 'smooth' });
        }

        // Display basic info
        this.displayBasicInfo(analysis);
        
        // Display components
        this.displayAllComponents(analysis);
    }

    displayBasicInfo(analysis) {
        const basicInfo = `
            <div class="result-section">
                <div class="result-section-header">
                    <i class="fas fa-info-circle"></i>
                    <h4>Informações da Análise</h4>
                </div>
                <div class="result-section-content">
                    <div class="metadata-grid">
                        <div class="metadata-item">
                            <span class="metadata-label">Segmento</span>
                            <span class="metadata-value">${analysis.segmento || 'N/A'}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Produto</span>
                            <span class="metadata-value">${analysis.produto || 'N/A'}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Status</span>
                            <span class="metadata-value">✅ Concluída</span>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const resultsContent = document.querySelector('.results-content');
        if (resultsContent) {
            resultsContent.innerHTML = basicInfo;
        }
    }

    displayAllComponents(analysis) {
        const components = [
            { key: 'avatar_ultra_detalhado', title: 'Avatar Ultra-Detalhado', icon: 'fas fa-user' },
            { key: 'drivers_mentais_customizados', title: 'Drivers Mentais', icon: 'fas fa-brain' },
            { key: 'sistema_anti_objecao', title: 'Sistema Anti-Objeção', icon: 'fas fa-shield-alt' },
            { key: 'pre_pitch_invisivel', title: 'Pré-Pitch Invisível', icon: 'fas fa-theater-masks' },
            { key: 'provas_visuais_sugeridas', title: 'Provas Visuais', icon: 'fas fa-eye' },
            { key: 'insights_exclusivos', title: 'Insights Exclusivos', icon: 'fas fa-lightbulb' },
            { key: 'pesquisa_web_massiva', title: 'Pesquisa Web', icon: 'fas fa-globe' }
        ];

        const resultsContent = document.querySelector('.results-content');
        
        components.forEach(component => {
            if (analysis[component.key]) {
                const section = this.createComponentSection(component, analysis[component.key]);
                if (resultsContent) {
                    resultsContent.appendChild(section);
                }
            }
        });
    }

    createComponentSection(component, data) {
        const section = document.createElement('div');
        section.className = 'result-section';

        const header = document.createElement('div');
        header.className = 'result-section-header';
        header.innerHTML = `
            <i class="${component.icon}"></i>
            <h4>${component.title}</h4>
        `;

        const content = document.createElement('div');
        content.className = 'result-section-content';
        content.innerHTML = this.formatComponentData(data, component.title);

        section.appendChild(header);
        section.appendChild(content);

        return section;
    }

    formatComponentData(data, title) {
        if (!data) return '<p>Dados não disponíveis</p>';

        if (Array.isArray(data)) {
            let html = '<ul class="insight-list">';
            data.forEach(item => {
                html += `<li class="insight-item"><i class="fas fa-chevron-right"></i><span class="insight-text">${item}</span></li>`;
            });
            html += '</ul>';
            return html;
        }

        if (typeof data === 'object') {
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

        return `<p>${data}</p>`;
    }

    enableResultButtons() {
        const pdfBtn = document.getElementById('downloadPdfBtn');
        const saveBtn = document.getElementById('saveJsonBtn');
        
        if (pdfBtn) pdfBtn.style.display = 'inline-flex';
        if (saveBtn) saveBtn.style.display = 'inline-flex';
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

    saveAnalysisLocally() {
        if (!this.currentAnalysis) {
            this.showError('Nenhuma análise disponível para salvar');
            return;
        }

        try {
            const dataStr = JSON.stringify(this.currentAnalysis, null, 2);
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
                <button class="btn-secondary" onclick="app.recoverPartialData('${error.session_id}')">
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

    async checkSystemHealth() {
        try {
            const response = await fetch('/api/health');
            return await response.json();
        } catch (error) {
            console.error('Health check error:', error);
            return { status: 'error' };
        }
    }

    removeFile(fileId) {
        console.log('File removed:', fileId);
    }
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    window.app = new ARQVApp();
    window.analysisManager = window.app; // Compatibility
});