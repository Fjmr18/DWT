from flask import Flask, request, Response
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed  # Para paralelismo

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

# Função principal para encontrar o caminho até "Philosophy"
def find_philosophy_stream(start_page):
    visited_pages = []
    stack = []
    current_page = start_page

    while current_page.lower() != "philosophy":
        if current_page in visited_pages:
            # Loop encontrado, tenta o próximo link
            if stack:
                previous_page, remaining_links = stack.pop()
                if remaining_links:
                    current_page = remaining_links.pop(0)
                    stack.append((previous_page, remaining_links))
                    continue
            else:
                return [{"error": "Loop encontrado, sem links adicionais", "page": current_page}]

        # Marca a página como visitada
        visited_pages.append(current_page)
        yield {"step": len(visited_pages), "current_page": current_page, "link": f"https://en.wikipedia.org/wiki/{current_page}"}

        # Obter conteúdo da Wikipédia
        response = requests.get(f"https://en.wikipedia.org/wiki/{current_page}")
        if response.status_code != 200:
            return [{"error": "Página não encontrada", "link": f"https://en.wikipedia.org/wiki/{current_page}"}]

        # Extrair todas as hiperligações válidas da página
        soup = BeautifulSoup(response.content, "html.parser")
        links = []
        for p in soup.find_all("p"):
            for link in p.find_all("a", href=True):
                href = link["href"]
                link_title = href.split("/wiki/")[-1]
                if (
                    href.startswith("/wiki/") and
                    ":" not in href and
                    "(disambiguation)" not in link_title.lower() and
                    link_title.lower() != current_page.lower()
                ):
                    links.append(link_title)

        # Caso não haja links válidos
        if not links:
            return [{"error": "Beco sem saída", "link": f"https://en.wikipedia.org/wiki/{current_page}"}]

        # Guarda os links restantes no stack
        stack.append((current_page, links[1:]))
        current_page = links[0]  # Segue o primeiro link por padrão
        time.sleep(0.2)  # Pausa opcional para simular processamento

    # Conclusão: Página Philosophy encontrada
    visited_pages.append("Philosophy")
    return [{"completed": True, "steps": len(visited_pages), "path": visited_pages, "link": "https://en.wikipedia.org/wiki/Philosophy"}]

# Rota para processar múltiplos jogadores em paralelo
@app.route("/find_paths_stream", methods=["POST"])
def find_paths_stream():
    data = request.get_json()
    players = data.get("players", [])

    if not players:
        return Response("Nenhum jogador fornecido", status=400)

    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:  # Define até 5 threads simultâneas
        futures = {
            executor.submit(find_philosophy_stream, player.get("page", "").replace(" ", "_")): player.get("name", f"Jogador {i+1}")
            for i, player in enumerate(players)
        }

        # Coleta os resultados conforme as threads terminam
        for future in as_completed(futures):
            player_name = futures[future]
            try:
                results[player_name] = list(future.result())  # Coleta o caminho do jogador
            except Exception as e:
                results[player_name] = {"error": str(e)}

    return Response(json.dumps(results, indent=4), content_type="application/json")

if __name__ == "__main__":
    app.run(debug=True)
