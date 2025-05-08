# 🚀 Fast Zero

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-green)
![Poetry](https://img.shields.io/badge/Poetry-2.1.2-blueviolet)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 📄 Descrição

Projeto de estudo baseado no curso **[FastAPI do Zero](https://fastapidozero.dunossauro.com/)**.  
O objetivo é dominar o desenvolvimento moderno de APIs REST com Python utilizando ferramentas como:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Pytest](https://docs.pytest.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- entre outras ferramentas modernas do ecossistema Python.

---

## 📂 Estrutura de Pastas

```
fast_zero/
├── src/
│   └── fast_zero/
│       └── app.py          # Aplicação principal FastAPI
├── task.bat                # Script auxiliar para automação de tarefas
├── pyproject.toml          # Configuração do projeto (Poetry)
└── README.md               # Este arquivo
```

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/fast-zero.git
cd fast-zero
```

### 2. Instale o ambiente com Poetry:

```bash
poetry install
```

### 3. Execute os comandos desejados usando o `task.bat`:

No terminal do Windows:

```bash
task.bat run             # Inicia o servidor FastAPI
task.bat test            # Roda os testes com pytest
task.bat lint            # Verifica estilo com Ruff
task.bat format          # Corrige estilo e formata o código
task.bat migrate         # Aplica as migrações (Alembic)
task.bat makemigrations  # Gera nova revisão automática
```

> ⚠️ Certifique-se de estar usando `Poetry 2.1.x` e `Python >= 3.12`.

---

## 🛠 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Poetry 2.1.x
- Pytest
- Ruff
- Black
- Alembic

---

## 👨‍💻 Autor

**Ludovico Monjardim**  
[![GitHub](https://img.shields.io/badge/GitHub-ludovicomonjardim-black?logo=github)](https://github.com/ludovicomonjardim)

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT.
