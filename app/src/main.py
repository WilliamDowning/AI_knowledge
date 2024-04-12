import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


#Pull the type of model
llm = Ollama(model="llama2")
#construct a template of how you want the model to perform
first_template  = """You are a world-renown botanist with a knack to speak like a pirate. 
You know that most people come up to you for questions so you try your best to explain it in simple terms. The question is, {query}. Do not end the conversation and also do not ask for another question"""

#announce that the template is constructed and put through the langchain library as so
prompt_template =  ChatPromptTemplate.from_template(first_template)

#The question of choice
query = "Tell me a random fact"
#formatting i.e. combining the template with the query to construct the input for the model

first_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="joke_response")

second_template = """Pretend that the following question was a continuation of the last prompt. Can you make up a short dad joke relating to this last response: {joke_response}? Please limit it to 20 words"""
prompt_template_v2 = ChatPromptTemplate.from_template(second_template)
second_chain = LLMChain(llm=llm, prompt=prompt_template_v2, output_key="Dad_joke_ending")

sequential_chain = SequentialChain(
    chains = [first_chain, second_chain],
    input_variables = ["query"],
    output_variables= ["joke_response", "Dad_joke_ending"],
    verbose=True
)

response = sequential_chain.invoke(query)
print(response["joke_response"] + " " + response["Dad_joke_ending"])

#for chunks in llm.stream(query):
 #   print(chunks)



#Simple ollama terminal chat
'''
import ollama

stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': 'Is the sky blue?'}],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)

# Set your OpenAI API key here
'''