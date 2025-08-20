# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 13:17:38 2025

@author: MS GROUP
"""
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.question_gen.openai import OpenAIQuestionGenerator
from llama_index.agent.openai import OpenAIAgent
import openai

# Chargement des documents
documents = SimpleDirectoryReader("docs").load_data()

# Indexation
index = VectorStoreIndex.from_documents(documents)

# Génération de questions
question_gen = OpenAIQuestionGenerator()
questions = question_gen.generate_questions_from_nodes(index.as_node_list())

# Agent ICARE
agent = OpenAIAgent.from_tools([], system_prompt="Tu es un assistant pédagogique ICARE.")
response = agent.chat("Quels sont les points clés du document ?")

print("✅ Questions générées :", questions)
print("✅ Réponse de l'agent :", response)
