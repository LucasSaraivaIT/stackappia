# stackappia

Setup do Ambiente da API (Ambiente Linux)
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate

$ pip freeze > requirements.txt

inserir os pacotes que se deseja instalar e executar

pip install -r requeriments.txt

Editar o arquivo .env e incluir a sua OPEN_API_KEY

cd api

https://8000-lucassaraiva-stackappia-9k7vzcfe0v3.ws-us115.gitpod.io/answer?url=https://dbd.puc-rio.br/TecnicasAvancadasNLP.html&question=Quem é o professor do curso?

#OPENAI_API_KEY=sk-None-HQ2AbxLM3RZkMfmvlyEKT3BlbkFJSz6oUOFDNYgLUCy4AMQv
#SITE_URL=https://mpce.mp.br/institucional/nucleos-de-apoio-2/
#API_URL=https://8000-lucassaraiva-stackappia-9k7vzcfe0v3.ws-us115.gitpod.io/#im

# Decide who can access te API
origins = [
    "http://localhost",
    "http://localhost:8501",
    "https://8501-lucassaraiva-stackappia-9k7vzcfe0v3.ws-us115.gitpod.io", # Substitua pela url da sua aplicacao Streamlit (No gitpod está na aba Ports)
]

#mudanças