from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

resp = client.responses.create(
    model="gpt-5",
    tools=[{
        "type": "mcp",
        "server_label": "dmcp",
        "server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",
        "server_url": "https://dmcp-server.deno.dev/sse",
        "require_approval": "never",
        "allowed_tools": ["roll"],
    }],
    input="Roll 2d4+1",
)

print(resp.output_text)
