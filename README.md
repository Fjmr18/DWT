# Drunk Wiki Trail 🍻

1. Descrição

O Drunk Wiki Trail é um jogo onde os jogadores começam com um tema aleatório da Wikipédia e têm que percorrer hiperligações (links) entre artigos até chegarem à página da Filosofia. Cada salto de um artigo para outro é contabilizado como um "salto". O objetivo do jogo é determinar quem consegue chegar à página "Filosofia" com o maior número de saltos. O vencedor é o jogador com mais saltos até alcançar Filosofia.

2. Regras do Jogo
  2.1. Início:
     - Cada jogador começa com um tema inicial da Wikipédia (exemplo: "War", "Logic", etc.).
     - O objetivo de cada jogador é chegar à página da "Filosofia" a partir do seu tema inicial.
  2.2. Percurso:
     - Cada jogador dá um "salto" ao clicar no primeiro link válido da página da Wikipédia que está a visualizar.
     - Um "salto" é contado cada vez que o jogador passa de uma página para outra.
     - O jogo continua até que o jogador chegue à página "Filosofia" ou seja bloqueado em um beco sem saída (sem links válidos para seguir)
  2.3. Loops:
     - Se um jogador entrar em um loop (passando repetidamente pelas mesmas páginas), o jogo tenta retroceder e seguir para o próximo link válido.
  2.4. Vencedor:
      - O vencedor é o jogador que atinge a página Filosofia com o maior número de saltos.
      - O vencedor será identificado com uma 🏆 ao lado do seu nome.

3. Funcionalidades
  - Adicionar Jogadores: Os jogadores podem ser adicionados à lista, cada um com um nome e um tema da Wikipédia.

4. Como Jogar
 4.1. Adicionar Jogadores:
    - Insira o nome do jogador e o tema inicial (um artigo da Wikipédia).
    - Clique em "Adicionar Jogador".
  4.2. Iniciar o Jogo:
    - Quando todos os jogadores estiverem na lista, clique em "Começar Jogo".
    - O sistema irá calcular os saltos e mostrar os resultados de cada jogador.
  4.3. Visualizar Resultados:
    - O vencedor será identificado com a 🏆 e o número de saltos que fez.

5. Tecnologias Usadas
  - Frontend: HTML, JavaScript
  - Backend: Python
    - Bibliotecas:
        -requests: Para fazer requisições HTTP à Wikipédia.
        -BeautifulSoup: Para parsear as páginas da Wikipédia e extrair links.
        -Flask: Para criar o servidor e a API de interação com o frontend.

6. Como executar o Jogo Localmente
   6.1. Pré-requisitos:
        Instalar o Python: Certifique-se de ter o Python 3 instalado no seu sistema.
   6.2. Instalar as dependências:
         Comando no terminal: pip install flask requests beautifulsoup4
   6.3. Executar o servidor Flask:
         Navegue até o diretório onde o app.py está localizado (backend).
         Execute o comando: python app.py
   6.4. Abrir o Frontend:
         Abra o arquivo index.html no seu navegador.
         Poderá interagir com o jogo e jogar localmente.


7. Agradecimentos
   Ao Senhoro Andre Albuquerque e ao Senhor David Gil por me incentivarem a ser um alcoólatra <3

9. Licença
    Este projeto é licenciado sob a MIT License.

