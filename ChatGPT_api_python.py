"""
Esse código usa a API do chatGPT para o seu terminal via Python
By: George Telles
+55 11 93290-7425
"""

# Instrucoes
# instalar openai com "pip install openai"
# criar uma chave "API key" no site da OpenAI
# substituir a sua chave no codigo

import openai

# Initialize the API key
openai.api_key = "xxx"

def gerar_resposta(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", ##
        #model="gpt-3.5-turbo-0301", ## ateh 1 junho 2023
        messages=messages,
        max_tokens=1024,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]

#Mensagem inicial
mensagens = [{"role": "system", "content": "Você é um assistente gente boa."}]

while True:
    # Ask a question
    question = input("Perguntar pro ChatGPT (\"sair\"): ")

    if question == "sair" or question == "":
        print("saindo")
        break
    else:
        mensagens.append({"role": "user", "content": str(question)})

        answer = gerar_resposta(mensagens)
        print("Nóis:", question)
        print("ChatGPT:", answer[0], "\nCusto:\n", answer[1])
        mensagens.append({"role": "assistant", "content": answer[0]})

    debugar = False
    if debugar:
        print("Mensagens", mensagens, type(mensagens))
