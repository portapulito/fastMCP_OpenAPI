import httpx

from fastmcp import FastMCP

API_BASE_URL = "http://localhost:8000"

client = httpx.AsyncClient(base_url=API_BASE_URL)

try:
    response = httpx.get(f"{API_BASE_URL}/openapi.json")
    response.raise_for_status()
    openapi_spec = response.json()
   
    print("openapi_spec scaricata con successo")
    
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="Auto Generated MCP from FastAPI"
    )

    print("mcp creato con successo")

    

except httpx.HTTPError as e:
    print(f"Error fetching OpenAPI spec: {e}")

   
if __name__ == "__main__":
    print("Starting MCP...")
    mcp.run()

