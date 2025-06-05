# FastMCP OpenAPI

Un sistema completo per trasformare automaticamente endpoint FastAPI in strumenti MCP (Model Context Protocol) utilizzando OpenAPI, con integrazione per agenti Google.

## 📋 Panoramica

Questo progetto permette di:
- Creare rapidamente endpoint FastAPI
- Convertire automaticamente gli endpoint in strumenti MCP tramite OpenAPI
- Collegare gli strumenti ad agenti Google tramite SDK

## 🏗️ Architettura

Il progetto è composto da tre componenti principali:

### 1. **API Server** (`my_api.py`)
Server FastAPI con endpoint personalizzati che espongono le funzionalità desiderate.

### 2. **MCP Server** (`mcp_server.py`)
Server MCP che:
- Legge automaticamente la specifica OpenAPI dal server FastAPI
- Converte gli endpoint in strumenti MCP utilizzabili
- Gestisce le chiamate agli strumenti e le inoltra agli endpoint

### 3. **Agente Google** (`agent/agent.py`)
Integrazione con SDK Google per collegare gli strumenti MCP agli agenti AI. Utilizza le API key configurate nel file `.env`.

## 🚀 Installazione

1. **Clona il repository:**
```bash
git clone https://github.com/portapulito/fastMCP_OpenAPI.git
cd fastMCP_OpenAPI
```

2. **Crea ambiente virtuale:**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Installa le dipendenze:**
```bash
uv sync
```

4. **Configura le variabili d'ambiente:**
Crea un file `.env` nella root del progetto:
```bash
# .env
GOOGLE_API_KEY=la_tua_api_key_google_qui
```

> ⚠️ **Importante**: Assicurati di avere una API key Google valida per l'integrazione con l'agente.

## 🛠️ Utilizzo

### Avvio del Server FastAPI
```bash
uvicorn file:app --reload
```

### Avvio del Server MCP
```bash
python mcp_server.py
```

### Integrazione con Agente Google
```bash
python -m agent.agent
```

L'agente Google si collega automaticamente agli strumenti MCP esposti dal server utilizzando l'API key configurata.

## 📁 Struttura del Progetto

```
fastMCP_OpenAPI/
├── my_api.py              # Server FastAPI con endpoint
├── mcp_server.py         # Server MCP con conversione OpenAPI
├── agent/
│   ├── __init__.py      # Inizializzazione modulo agente
│   └── agent.py         # Agente Google con integrazione MCP
├── pyproject.toml        # Configurazione dipendenze
├── uv.lock              # Lock file dipendenze
├── .python-version       # Versione Python
├── .env                 # Variabili d'ambiente (da creare)
└── README.md            # Questo file
```

## 🔧 Configurazione

### FastAPI Server
Modifica `file.py` per aggiungere i tuoi endpoint personalizzati:

```python
@app.get("/my-endpoint")
async def my_function():
    return {"message": "Il tuo endpoint personalizzato"}
```

### MCP Server
Il server MCP legge automaticamente la specifica OpenAPI e crea gli strumenti corrispondenti. Non richiede configurazione manuale.

## 🌟 Caratteristiche

- **Conversione Automatica**: Gli endpoint FastAPI diventano automaticamente strumenti MCP
- **Integrazione OpenAPI**: Utilizza le specifiche OpenAPI per la mappatura automatica
- **Agente Google**: Integrazione diretta con SDK Google
- **Scalabile**: Facile aggiungere nuovi endpoint e strumenti
- **Type Safety**: Mantiene la tipizzazione attraverso tutta la pipeline

## 🤝 Contributi

I contributi sono benvenuti! Per contribuire:

1. Fai fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Committa le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Pusha sul branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## 📞 Supporto

Per domande, problemi o suggerimenti, apri una issue su GitHub.

---

**Creato con ❤️ per semplificare l'integrazione tra FastAPI, MCP e agenti Google**
