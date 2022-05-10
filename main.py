import requests
import random
from ls8class import Question


response = requests.get('https://jsonkeeper.com/b/YOJ2')
dict_q = response.json()

def read_question():
    list_questions = []
    for key in dict_q:
        list_questions.append(Question(
            text=key,
            answer=dict_q[key]['answers'],
            difficulty=dict_q[key]['difficulty'],
            author=dict_q[key]['author'],
            theme=dict_q[key]['theme'],
        ))
        random.shuffle(list_questions)
    return list_questions


questions = read_question()

for question in questions:
    print(question.build_question())
    user_answer = input("Введите ваш ответ:")
    question.user_answer = user_answer
    question.is_asked = True
    if user_answer == "stop":
        break
    if question.is_correct():
        print(f"Ответ верный, получено {question.score}")
        question.answer = True
    else:
        print(f"Ответ неверный. Верный ответ - {(', ').join(question.answer)}")
        question.answer = False


def statistics(questions):
    stats = {
        "answer": 0,
        "total": 0,
        "total_score": 0
        }
    for question in questions:
        if question.is_asked == True:
            stats["total"] += 1
            if question.answer == True:
                stats["right_answer"] += 1
                stats["total_score"] += question.score_q
    return stats

stats = statistics(questions)

print(f"Вот и всё! Отвечено {stats['answer']} вопроса из {stats['total']}. Вы набрали {stats['total_score']}" )



