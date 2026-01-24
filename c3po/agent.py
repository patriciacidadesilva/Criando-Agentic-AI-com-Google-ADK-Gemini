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

# Execução simples para teste
if __name__ == "__main__":
    print("🤖 Agente criado com sucesso!")
    print(f"Nome do agente: {root_agent.name}")
    print(f"Modelo utilizado: {root_agent.model}")
    print(f"Descrição: {root_agent.description}")
