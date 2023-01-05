import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY

def homeDescription(query):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate a detailed house description for : {}".format(query),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


print(response)

query = 'single family houses'
homeDescription(query)