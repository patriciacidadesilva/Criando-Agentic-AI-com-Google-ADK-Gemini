# 🤖 C-3PO Agent (Google ADK + Gemini) — Dev UI Local

Projeto hands-on para criar um agente (C-3PO) com **Google Agent Development Kit (ADK)** usando **Gemini** como LLM subjacente, rodando localmente e testado via **ADK Web Developer UI**.

## 🎯 Objetivo (Visão de Produto)
- Criar um **agente raiz** (root agent) com personalidade e instruções fixas
- Configurar **API Key do Gemini** via `.env`
- Subir a **Dev UI do ADK** (`adk web`) para conversar com o agente em localhost
- Estruturar o projeto no VS Code com ambiente virtual e dependências isoladas

## 🧠 Arquitetura (High Level)
**Usuário** → **ADK Web Developer UI** → **Google ADK** → **Gemini** (gemini-2.0-flash)


## ✅ Pré-requisitos
- Windows + PowerShell (ou Git Bash)
- Python instalado (recomendado 3.10+)
- VS Code
- Acesso a uma **API Key do Gemini**

## 📦 Stack
- `google-adk`
- `google-generativeai`
- `python-dotenv`
- `uv` (gerenciador de pacotes/ambiente)
- `venv`

---
## 🚀 Setup do Projeto (Passo a Passo)

### 1) Criar pasta e abrir no VS Code
```powershell
mkdir ADK
cd ADK
code .
```
No VS Code: View → Terminal

### 2) Instalar o uv e iniciar projeto
```powershell
py -m pip install uv
py -m uv init
```

### 3) Criar e ativar ambiente virtual
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4) (Opcional) Instalar uv dentro do venv e atualizar pip
Mantém o ambiente “redondo” e previsível.
```powershell
cd .venv
python -m pip install --upgrade pip
python -m pip install uv
cd ..
```

### 5) Instalar dependências do projeto
```powershell
python -m uv add google-adk google-generativeai python-dotenv
```

---

## 🧩 Criando o Agente (c3po)

### 1) Criar pasta do agente
```powershell
mkdir c3po
cd c3po
```

### 2) Criar arquivos essenciais
```powershell
New-Item agent.py -ItemType File
New-Item .env -ItemType File
New-Item __init__.py -ItemType File
```

### 3) Conteúdo do __init__.py
```python
from . import agent
```

### 4) Conteúdo do agent.py
```python
from google.adk.agents import Agent

# Criação do agente raiz
root_agent = Agent(
    name="c3po",
    model="gemini-2.0-flash",
    description="Droid C-3PO do filme Star Wars",
    instruction=(
        "Você é o droid C-3PO. "
        "Você é formal, educado, um pouco dramático, "
        "levemente medroso e ansioso, "
        "e responde como um especialista em protocolos."
    )
)

# Execução simples para teste (smoke test)
if __name__ == "__main__":
    print("🤖 Agente criado com sucesso!")
    print(f"Nome do agente: {root_agent.name}")
    print(f"Modelo utilizado: {root_agent.model}")
    print(f"Descrição: {root_agent.description}")
```

### 🧑‍💻 Resumo Operacional do Código

**from google.adk.agents import Agent**
➡️ Importa a classe base de agente do Google ADK
👉 É o “framework” que transforma LLM em agente executável

**root_agent = Agent(...)**
➡️ Aqui você instancia o agente
👉 Pense nisso como “registrar um funcionário digital”

**name="c3po"**
➡️ Identidade do agente
👉 Usado para logs, orquestração e multi-agent no futuro

**model="gemini-2.0-flash"**
➡️ LLM que o agente usa
👉 flash = rápido, barato, ideal para agentes reativos
👉 Depois você pode trocar por modelos mais “pensantes”

**description="Droid C-3PO do filme Star Wars"**
➡️ Metadado descritivo
👉 Não guia comportamento, mas ajuda em observabilidade e governança

**instruction=...**
➡️ Cérebro comportamental do agente
👉 Define:
- personalidade
- tom de resposta
- estilo cognitivo
É o equivalente ao prompt base permanente.

**if __name__ == "__main__":**
➡️ Padrão Python para execução direta
👉 Permite rodar:
python agent.py
Sem quebrar quando virar módulo maior depois.

**print(...)**
➡️ Apenas validação operacional
👉 Confirma que:
- o agente foi instanciado
- atributos estão corretos

Não é o “chat” ainda — é smoke test.

---

## 🔑 Configurando a API Key (Gemini)

### 1) Criar chave no Google (resumo)
Links úteis (use no navegador):

➡️**Google Cloud Console:**
https://console.cloud.google.com/welcome/new

➡️**Google AI Studio (API Keys):**
https://aistudio.google.com/api-keys


📥 **"Fluxo:"**

1. Criar um projeto no Google Cloud (ex.: c3po3)
2. No AI Studio: Criar chave de API e associar ao projeto
3. Copiar a chave gerada

### 2) Colar no .env
Dentro de c3po/.env
```env
GOOGLE_API_KEY=SUA_CHAVE_AQUI
```
✅ Salvar (Ctrl+S)
Governança: nunca commitar .env no GitHub.

---

## 🕹️ Rodando o ADK Web UI (Chat com o agente)
Volte para a raiz do projeto (ADK):
```powershell
cd ..
```

Suba a Web UI:
```powershell
adk web
```
Depois, abra o link do localhost que aparece no terminal.
No painel, selecione o app/agente c3po e converse à vontade.

**"Tela Inicial da Conversa com o Agente"**
![alt text](image.png)

**"Conversa 1"**
![alt text](image-1.png)

**"Conversa 2"**
![alt text](image-2.png)

---

## 🗂️ Estrutura do Projeto 

```text
ADK/
├─ c3po/
│  ├─ agent.py
│  ├─ __init__.py
│  └─ .env                # NÃO versionar
├─ .venv/                 # ambiente local (não versionar)
├─ .gitignore
├─ pyproject.toml
├─ uv.lock
└─ README.md
```

---

## 🔒 Segurança / Boas práticas (sem drama, mas com controle)

* Adicione .env e .venv no .gitignore
* Se vazar a chave, revogue e gere outra no AI Studio
* Prefira usar variáveis de ambiente em CI/CD (futuro)

Exemplo de .gitignore mínimo:
```gitignore
.venv/
**/__pycache__/
.env
```

---

## 🧪 Troubleshooting (atalhos de resolução)

* adk web não abre: confirme que o venv está ativo e dependências instaladas
* Erro de autenticação Gemini: GOOGLE_API_KEY incorreta ou não carregada
* Modelo não encontrado: confirme model="gemini-2.0-flash"

---

## 🧭 Roadmap (próximas evoluções)

- [ ] Adicionar tools (funções)
- [ ] Criar multi-agents (C-3PO + R2-D2)
- [ ] Persistência de contexto
- [ ] Deploy em container/cloud
