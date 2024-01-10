import json
from difflib import get_close_matches

def loid_knowledge_base(file_path:str)->dict:
    with open(file_path,'r') as file:
        data:json.load(file)
    return data

def save_knowledge_base(file_path : str , data :dict ):
    with open(file_path,'w')as file:
        json.dump(data,file,indent=2)

def get_answer_for_question(question:str,knowledge_base:dict)->str|None:
    for q in knowledge_base["questions"]:
        if q["question"]==question:
            return q["answer"]

def best_answer(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    # Get all answers and their respective scores
    answers = [(item['answer'], len(item['answer'].split())) for item in data['questions']]

    # Find the answer with the highest score (length)
    best_answer = max(answers, key=lambda x: x[1])[0]

    return best_answer



def chatbot():
    while True:
        knowledge_base:dict = save_knowledge_base('knowledge_base.json')
        user_input : str = input("you : ")
        if user_input.lower() == "quit":
            break
        best_answer
        

