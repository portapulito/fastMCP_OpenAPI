# mcp_agent/agent.py
from pathlib import Path
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

current_dir = Path(__file__).parent
project_root = current_dir.parent
python_exe = project_root / ".venv" / "Scripts" / "python.exe"
mcp_server_file = project_root / "server.py"  # Il tuo MCP da OpenAPI

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='openapi_assistant',
    instruction='''Sei un assistente che usa un'API generata automaticamente da OpenAPI.
    
    Hai accesso a questi tools:
    - add_note: Aggiunge note
    - list_notes: Lista le note
    - calculate: Fa calcoli matematici
    
    Tutti i tools sono stati generati automaticamente dalla specifica OpenAPI.
    ''',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command=str(python_exe),
                args=[str(mcp_server_file)],
                cwd=str(project_root)
            ),
        )
    ],
)