# open AI library
from openai import OpenAI

# Enviroment Variables libraries
import os
from dotenv import load_dotenv

# load enviroment variables from the .env file
load_dotenv()

client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)
    
models = client.models.list()

print(models)