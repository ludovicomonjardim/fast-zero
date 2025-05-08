@echo off
set CMD=%1

if "%CMD%"=="run" goto RUN
if "%CMD%"=="pre_test" goto PRE_TEST
if "%CMD%"=="test" goto TEST
if "%CMD%"=="post_test" goto POST_TEST
if "%CMD%"=="lint" goto LINT
if "%CMD%"=="format" goto FORMAT
if "%CMD%"=="migrate" goto MIGRATE
if "%CMD%"=="makemigrations" goto MAKEMIGRATIONS

goto HELP

:RUN
poetry run fastapi dev src/fast_zero/app.py
goto END

:PRE_TEST
goto LINT

:TEST
poetry run pytest --cov=src/fast_zero -vv --disable-warnings
poetry run coverage html
goto END

:POST_TEST
poetry run coverage html
goto END

:LINT
poetry run ruff check src
poetry run ruff check --diff src
goto END

:FORMAT
poetry run ruff check src --fix
poetry run ruff format src
goto END

:MIGRATE
poetry run alembic upgrade head
goto END

:MAKEMIGRATIONS
poetry run alembic revision --autogenerate -m "nova revisao"
goto END

:HELP
echo.
echo Comando "%CMD%" nao reconhecido.
echo.
echo Comandos disponiveis:
echo   run             - Iniciar servidor FastAPI (modo dev)
echo   test            - Executar testes com pytest
echo   lint            - Rodar ruff (linter)
echo   format          - Corrigir estilo e formatar com black
echo   migrate         - Executar migracoes com alembic
echo   makemigrations  - Criar nova revisao com alembic

:END
