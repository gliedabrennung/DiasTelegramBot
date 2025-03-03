from groq import Groq

async def ai_api(text):
    client = Groq()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model = "gemma2-9b-it",
    )

    return chat_completion.choices[0].message.content