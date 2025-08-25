from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.responses.create(
  model="gpt-5",
  input=[
    {
      "role": "developer",
      "content": [
        {
          "type": "input_text",
          "text": "Use the provided city information to provide a structured trip plan. Be concise and use bullet points to outline a plan for each of the days, explaining why it's interesting"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Help me plan a trip for 10 days in Dublin, Ireland"
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  reasoning={
    "effort": "low",
    "summary": "auto"
  },
  tools=[{ "type": "web_search_preview" }],
  store=True
)
print(response.output[1].content[0].text)
