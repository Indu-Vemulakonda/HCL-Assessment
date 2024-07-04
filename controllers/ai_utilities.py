import openai
from config import *

openai.api_key = OPEN_AI_API_KEY  # retrieve secured API key

messages = []


# Function to set system content
def set_system_content(system_content):
    global messages
    messages.append({"role": "system", "content": system_content})


# Function to delete system content and make it generic
def delete_system_content():
    global messages
    messages = []  # reset messages to empty


# Function to generate Open AI system response
def get_system_response(usr_message, model="gpt-3.5-turbo", system_content=None):
    global messages
    messages.append({"role": "user", "content": usr_message})
    system_response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return system_response.choices[0].message["content"]  # return generated response
