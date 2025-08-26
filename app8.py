from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

resp = client.responses.create(
    model="gpt-5",
    input="Fetch the average order value for last month and return a SQL query only.",
    tools=[
        {
            "name": "sql_runner",
            "type": "custom",
            "description": "Executes raw SQL and returns results."
        }
    ]
)

# The model can emit text that the tool receives directly (raw SQL)
# How your backend receives and executes the model->tool payload depends on your webhook/runtime.
print(resp.output_text)
