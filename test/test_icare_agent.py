# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 12:27:56 2025

@author: MS GROUP
"""

# scripts/test_icare_agent.py
from llama_index.core import SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.question_gen.openai import OpenAIQuestionGenerator

docs = SimpleDirectoryReader("data").load_data()
llm = OpenAI(model="gpt-4")
qgen = OpenAIQuestionGenerator(llm=llm)

questions = qgen.generate(docs)
for i, q in enumerate(questions, 1):
    print(f"❓ Q{i}: {q}")
