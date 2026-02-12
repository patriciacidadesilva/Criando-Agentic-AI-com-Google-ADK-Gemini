<div align="center">

<!-- (Opcional) Banner no topo -->
<!-- <img src="assets/header.png" alt="Header" width="100%" /> -->

# 🤖 Criando Agentic AI com Google ADK + Gemini

**Hands-on para criar um agente (C-3PO) com Google ADK rodando localmente e testado via ADK Web Developer UI.**

**Usuário → ADK Web Developer UI → Google ADK → Gemini (gemini-2.0-flash)**

<img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Google%20ADK-Agent%20Development%20Kit-4285F4?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/Gemini-gemini--2.0--flash-000000?style=for-the-badge&logo=googlegemini&logoColor=white" />
<img src="https://img.shields.io/badge/ADK%20Web%20UI-localhost-1f6feb?style=for-the-badge" />

<br/>

<img src="https://img.shields.io/badge/windows-powershell-0C7BD6?style=for-the-badge&logo=powershell&logoColor=white" />
<img src="https://img.shields.io/badge/uv-package%20manager-6f42c1?style=for-the-badge" />
<img src="https://img.shields.io/badge/venv-isolated%20env-2EA44F?style=for-the-badge" />
<img src="https://img.shields.io/badge/status-stable-2EA44F?style=for-the-badge" />

</div>

---

## 🎯 Objetivo (Visão de Produto)
- Criar um **agente raiz** (root agent) com personalidade e instruções fixas
- Configurar **API Key do Gemini** via `.env`
- Subir a **Dev UI do ADK** (`adk web`) para conversar com o agente em localhost
- Estruturar o projeto no VS Code com ambiente virtual e dependências isoladas

---  

## 🧠 Arquitetura (High Level)
**Usuário** → **ADK Web Developer UI** → **Google ADK** → **Gemini** (gemini-2.0-flash)

---

## ✅ Pré-requisitos
- Windows + PowerShell (ou Git Bash)
- Python instalado (recomendado 3.10+)
- VS Code
- Acesso a uma **API Key do Gemini**

---

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

1. **from google.adk.agents import Agent**
* ➡️ Importa a classe base de agente do Google ADK
* 👉 É o “framework” que transforma LLM em agente executável

2. **root_agent = Agent(...)**
* ➡️ Aqui você instancia o agente
* 👉 Pense nisso como “registrar um funcionário digital”

3. **name="c3po"**
* ➡️ Identidade do agente
* 👉 Usado para logs, orquestração e multi-agent no futuro

4. **model="gemini-2.0-flash"**
* ➡️ LLM que o agente usa
* 👉 flash = rápido, barato, ideal para agentes reativos
* 👉 Depois você pode trocar por modelos mais “pensantes”

5. **description="Droid C-3PO do filme Star Wars"**
* ➡️ Metadado descritivo
* 👉 Não guia comportamento, mas ajuda em observabilidade e governança

6. **instruction=...**
* ➡️ Cérebro comportamental do agente
* 👉 Define: * personalidade/ * tom de resposta/ * estilo cognitivo
É o equivalente ao prompt base permanente.

7. **if __name__ == "__main__":**
* ➡️ Padrão Python para execução direta
* 👉 Permite rodar:
python agent.py
* Sem quebrar quando virar módulo maior depois.

8. **print(...)**
* ➡️ Apenas validação operacional
* 👉 Confirma que: * o agente foi instanciado/ * atributos estão corretos

Não é o “chat” ainda — é smoke test.

---

## 🔑 Configurando a API Key (Gemini)
Esta etapa conecta o agente ao Gemini, o LLM subjacente utilizado pelo Google ADK.

### 1️⃣ Criar um projeto no Google Cloud

* Acesse o Google Cloud Console:
➡️ Google Cloud Console
https://console.cloud.google.com/welcome/new

**No console:**
1.  Clique em Selecionar projeto → Novo projeto
2.  Defina o nome do projeto (exemplo):
```nginx
c3po3
```
3. Clique em Criar
> 💡 O projeto é necessário para vincular a API Key e aplicar governança básica.

### 2️⃣ Criar a API Key do Gemini no Google AI Studio

* Acesse o Google AI Studio:
➡️ Google AI Studio — API Keys
https://aistudio.google.com/api-keys

**No AI Studio:**

1. Clique em Criar chave de API
2. Em Escolher um projeto, selecione o projeto criado (ex.: c3po3)
3. Clique em Importar / Criar chave
> A API Key será gerada automaticamente.

### 3️⃣ Copiar a API Key

Após a criação:
* Copie a chave exibida pelo AI Studio
* Guarde em local seguro
> ⚠️ Essa chave dá acesso direto ao Gemini.

### 4️⃣ Configurar a chave no projeto (.env)

Dentro do projeto, abra o arquivo:
```text
c3po/.env
```

Adicione:
```env
GOOGLE_API_KEY=SUA_CHAVE_AQUI
```
> Salve o arquivo (Ctrl + S).

--- 

### 🔒 Governança e Segurança

* ❌ Nunca versionar o arquivo .env
* 🔁 Se a chave vazar, revogue e gere outra no AI Studio
* 🚀 Em produção, prefira variáveis de ambiente ou secret managers

---

## 🕹️ Rodando o ADK Web UI (Chat com o agente)
Nesta etapa, você inicia a interface web do Google ADK para conversar com o agente C-3PO criado anteriormente.

### 1️⃣ Voltar para a raiz do projeto

Certifique-se de estar na pasta raiz do projeto (ADK):
```powershell
cd ..
```
> 💡 Esse passo é importante: o comando adk web deve ser executado na raiz do projeto, não dentro da pasta do agente (c3po).

### 2️⃣ Subir o ADK Web Developer UI

Execute o comando:
```powershell
adk web
```

Se tudo estiver correto, o terminal exibirá mensagens semelhantes a:
```powershell
ADK Web Server started
For local testing, access at http://127.0.0.1:8000
```

### 3️⃣ Acessar a interface no navegador

**No terminal:**
1. Segure Ctrl
2. Clique no link http://127.0.0.1:8000
3. Isso abrirá automaticamente o ADK Web Developer UI no navegador.

### 4️⃣ Conversar com o agente C-3PO

**Na interface web:**
1. Selecione o app/agente c3po
2. Digite uma mensagem no chat
3. Interaja livremente com o agente

A partir desse ponto, você já está conversando com um agente de IA em execução local, utilizando:
- Google ADK (Agent Runtime)
- Gemini como LLM subjacente
- Interface web para observabilidade e testes



> **"Tela Inicial da Conversa com o Agente"**
![alt text](image.png)

> **"Conversa 1"**
![alt text](image-1.png)

> **"Conversa 2"**
![alt text](image-2.png)

---

## 🧠 Observações importantes

- Para encerrar o servidor, volte ao terminal e pressione Ctrl + C
- Qualquer alteração no código do agente exige reiniciar o adk web

> A UI permite acompanhar sessions, events e traces, facilitando debug e evolução do agente

---

## 🗂️ Estrutura do Projeto 

```text
Criando-Agentic-AI-com-Google-ADK-Gemini/
├─ c3po/
│  ├─ .adk/               # artefatos internos do Google ADK
│  ├─ agent.py            # definição do agente raiz (C-3PO)
│  └─ __init__.py
├─ .gitignore
├─ .python-version        # versão do Python usada no projeto
├─ main.py                # ponto de entrada auxiliar (opcional)
├─ pyproject.toml         # configuração do projeto Python
├─ uv.lock                # lockfile de dependências
├─ README.md
├─ image.png              # prints da ADK Web UI
├─ image-1.png
└─ image-2.png
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
