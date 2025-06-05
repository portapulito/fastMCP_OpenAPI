import httpx

from fastmcp import FastMCP

API_BASE_URL = "http://localhost:8000"

client = httpx.AsyncClient(base_url=API_BASE_URL)


openapi_spec = httpx.get("http://localhost:8000/openapi.json").json()
    
    
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="AI Agent API",
    all_routes_as_tools=True
)

print("mcp creato con successo")

    



   
if __name__ == "__main__":
    print("Starting MCP...")
    mcp.run()

