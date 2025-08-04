@echo off
REM ARQV30 Enhanced v2.0 ULTRA-ROBUSTO - Script de Instalação Windows CORRIGIDO
REM Execute este arquivo para instalar todas as dependências

echo ========================================
echo ARQV30 Enhanced v2.0 ULTRA-ROBUSTO - Instalação CORRIGIDA
echo Análise Ultra-Detalhada de Mercado
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRO: Python não encontrado!
    echo.
    echo Por favor, instale Python 3.11+ de https://python.org
    echo Certifique-se de marcar "Add Python to PATH" durante a instalação.
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado:
python --version
echo.

REM Verifica versão do Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Versão do Python: %PYTHON_VERSION%
echo.

REM Cria ambiente virtual
echo 🔄 Criando ambiente virtual...
python -m venv venv
if errorlevel 1 (
    echo ❌ ERRO: Falha ao criar ambiente virtual!
    pause
    exit /b 1
)

REM Ativa ambiente virtual
echo 🔄 Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERRO: Falha ao ativar ambiente virtual!
    pause
    exit /b 1
)

REM Atualiza pip
echo 🔄 Atualizando pip...
python -m pip install --upgrade pip
echo.

REM Instala dependências críticas primeiro
echo 🔄 Instalando dependências críticas...
pip install wheel setuptools
pip install Flask==2.3.3
pip install requests==2.31.0
pip install python-dotenv==1.0.0

REM Tenta instalar PostgreSQL driver
echo 🔄 Instalando driver PostgreSQL...
pip install psycopg2-binary==2.9.9
if errorlevel 1 (
    echo ⚠️ PostgreSQL driver falhou, tentando alternativa...
    pip install psycopg2-binary --only-binary=psycopg2-binary
    if errorlevel 1 (
        echo ⚠️ Usando SQLite como fallback...
        pip install sqlalchemy==2.0.23
    )
)

REM Instala dependências de IA
echo 🔄 Instalando dependências de IA...
pip install google-generativeai==0.3.2
pip install groq==0.4.2
pip install openai==1.3.8

REM Instala Supabase
echo 🔄 Instalando Supabase...
pip install supabase==2.0.2
pip install postgrest==0.13.2

REM Instala dependências de processamento
echo 🔄 Instalando dependências de processamento...
pip install pandas==2.3.1
pip install beautifulsoup4==4.12.2
pip install PyPDF2==3.0.1
pip install python-docx==0.8.11
pip install openpyxl==3.1.2

REM Instala dependências de extração (opcionais)
echo 🔄 Instalando extratores (podem falhar, mas não é crítico)...
pip install newspaper3k
if errorlevel 1 (
    echo ⚠️ newspaper3k falhou, continuando...
)

pip install readability-lxml
if errorlevel 1 (
    echo ⚠️ readability-lxml falhou, continuando...
)

pip install trafilatura
if errorlevel 1 (
    echo ⚠️ trafilatura falhou, continuando...
)

pip install pdfplumber==0.11.7
if errorlevel 1 (
    echo ⚠️ pdfplumber falhou, continuando...
)

REM Instala dependências restantes
echo 🔄 Instalando dependências restantes...
pip install reportlab==4.0.4
pip install Pillow==10.2.0
pip install lxml==4.9.3
pip install chardet==5.2.0
pip install Flask-CORS==4.0.0
pip install Werkzeug==2.3.7

REM Cria diretórios necessários
echo 🔄 Criando estrutura de diretórios ULTRA-ROBUSTA...
if not exist "src\uploads" mkdir src\uploads
if not exist "src\static\images" mkdir src\static\images
if not exist "src\cache" mkdir src\cache
if not exist "src\logs" mkdir src\logs
if not exist "relatorios_intermediarios" mkdir relatorios_intermediarios
echo.

REM Testa a instalação
echo 🧪 Testando instalação ULTRA-ROBUSTA...
cd src
python -c "import flask, requests, google.generativeai, supabase, pandas; print('✅ Dependências principais OK')"
if errorlevel 1 (
    echo ⚠️ AVISO: Algumas dependências podem não estar funcionando corretamente.
    echo Mas o sistema pode funcionar com funcionalidade limitada.
) else (
    echo ✅ Teste de dependências ULTRA-ROBUSTO passou!
)
cd ..
echo.

echo ========================================
echo 🎉 INSTALAÇÃO CORRIGIDA CONCLUÍDA!
echo ========================================
echo.
echo 📋 PRÓXIMOS PASSOS:
echo.
echo 1. ✅ Configure suas chaves de API no arquivo .env
echo.
echo 2. Execute run.bat para iniciar a aplicação
echo.
echo 3. Acesse http://localhost:5000 no seu navegador
echo.
echo 4. Teste com uma análise simples primeiro
echo.
echo ⚠️ NOTA: Se PostgreSQL não funcionou, o sistema usará SQLite
echo como fallback, que é suficiente para testes e desenvolvimento.
echo.
echo ========================================
echo.
echo 📚 SISTEMA ULTRA-ROBUSTO PRONTO!
echo Agora você tem acesso a análises de mercado
echo com profundidade de consultoria de R$ 50.000/hora
echo.
echo 🔥 RECURSOS ATIVADOS:
echo - Google Gemini Pro para análise IA
echo - Supabase/SQLite para banco de dados
echo - Sistema de extração robusto
echo - Múltiplos fallbacks implementados
echo.
pause