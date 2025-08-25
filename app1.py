from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-5",
  messages=[
    {
      "role": "developer",
      "content": [
        {
          "type": "text",
          "text": "You are a helpful assistant"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "As Descartes said I think therefore"
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  verbosity="medium",
  reasoning_effort="medium"
)
