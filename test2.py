import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
engine="text-davinci-002",
prompt="Write an extremely long, detailed answer to \"How to Cut Corners Using CSS Mask and Clip Path Properties\". Use HTML formatting.",
temperature=0.7,
max_tokens=709,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

print(response.choices[0].text)