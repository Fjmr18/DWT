let players = []; // Lista de jogadores

// Adiciona um jogador à lista
function addPlayer() {
    const playerName = document.getElementById("playerName").value.trim();
    const wikiTopic = document.getElementById("wikiTopic").value.trim();
    const playersList = document.getElementById("playersList");

    if (playerName && wikiTopic) {
        players.push({ name: playerName, page: wikiTopic, steps: 0 });
        renderPlayerList();
        document.getElementById("playerName").value = "";
        document.getElementById("wikiTopic").value = "";
    } else {
        alert("Por favor, insira o nome do jogador e o tema da Wikipédia.");
    }
}

// Atualiza a lista de jogadores no HTML
function renderPlayerList(winner = null) {
    const playersList = document.getElementById("playersList");
    playersList.innerHTML = "";
    players.forEach(player => {
        playersList.innerHTML += `
            <li>
                ${player.name}: ${player.page} (${player.steps} saltos) 
                ${winner === player.name ? "🏆" : ""}
            </li>
        `;
    });
}

// Inicia o jogo para todos os jogadores
function startGame() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<p>A percorrer páginas... ⏳</p>";

    fetch("http://127.0.0.1:5000/find_paths_stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ players: players })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = ""; // Limpa a mensagem inicial
        let maxSteps = 0;
        let winner = "";

        // Processa os resultados
        players = players.map(player => {
            const path = data[player.name];
            let playerSteps = 0;

            resultDiv.innerHTML += `<h3>${player.name}</h3>`;
            path.forEach(step => {
                if (step.error) {
                    resultDiv.innerHTML += `<p>❌ Erro: ${step.error}</p>`;
                } else {
                    playerSteps = step.step || playerSteps; // Atualiza com o último valor de "step"
                    resultDiv.innerHTML += `
                        <p>🔗 Salto ${step.step}: 
                            <a href="${step.link}" target="_blank">${step.current_page}</a>
                        </p>`;
                }
            });

            // Verifica o maior número de saltos
            if (playerSteps > maxSteps) {
                maxSteps = playerSteps;
                winner = player.name;
            }

            return { ...player, steps: playerSteps };
        });

        // Atualiza a lista com os saltos e coroa o vencedor
        renderPlayerList(winner);

        // Mostra o vencedor
        resultDiv.innerHTML += `<h2>🏆 Vencedor: ${winner} com ${maxSteps} saltos!</h2>`;
    })
    .catch(error => {
        console.error("Erro no fetch:", error.message);
        resultDiv.innerHTML = "Erro ao conectar ao servidor.";
    });
}
