headache = None
high_temperature = None
muscle_pain = None
cough = None

def get_questions_test():
    global headache
    print("Вы чувствуете головную боль? (1 - да, 2 - нет)")
    answer = int(input())
    if answer == 1:
        headache = True
    else:
        headache = False


def get_questions(question_number):
    global headache
    global high_temperature
    global muscle_pain
    global cough
    if question_number == 1:
        print("Вы чувствуете головную боль? (1 - да, 2 - нет)")
        answer = int(input())
        if answer == 1:
            headache = True
        else:
            headache = False
        get_questions(question_number + 1)
    if question_number == 2:
        print("У вас высокая температура? (1 - да, 2 - нет)")
        answer = int(input())
        if answer == 1:
            high_temperature = True
        else:
            high_temperature = False
        get_questions(question_number + 1)
    if question_number == 3:
        print("Вы чувствуете боль в мышцах? (1 - да, 2 - нет)")
        answer = int(input())
        if answer == 1:
            muscle_pain = True
        else:
            muscle_pain = False
        get_questions(question_number + 1)
    if question_number == 4:
        print("У вас есть кашель? (1 - да, 2 - нет)")
        answer = int(input())
        if answer == 1:
            cough = True
        else:
            cough = False


get_questions(1)
print(headache)
print(high_temperature)
print(muscle_pain)
print(cough)