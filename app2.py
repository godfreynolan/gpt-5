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
          "text": "You are a helpful assistant"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "As Descartes said I think therefore...."
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
    "effort": "medium",
    "summary": "auto"
  },
  tools=[],
  store=True
)
print(response.output[1].content[0].text)
