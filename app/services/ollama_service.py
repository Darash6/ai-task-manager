import requests
from app.core.config import OLLAMA_URL, OLLAMA_MODEL


def gerar_tarefa(texto: str):
    prompt = f"""
Você é um sistema que transforma ideias em tarefas.

Responda EXATAMENTE assim:

TITULO: <titulo curto>
DESCRICAO: <descricao objetiva>

Texto: {texto}
"""

    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()
        resposta = data.get("response", "")

        titulo = "Tarefa automática"
        descricao = resposta

        if "TITULO:" in resposta and "DESCRICAO:" in resposta:
            partes = resposta.split("DESCRICAO:")
            titulo = partes[0].replace("TITULO:", "").strip()
            descricao = partes[1].strip()

        return titulo, descricao

    except Exception as e:
        return "Erro na IA", str(e)