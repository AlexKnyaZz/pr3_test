headache = None
high_temperature = None
muscle_pain = None
cough = None

# ОРВИ, мигрень, Ковид, Туберкулез
diseases_list = [[True, True, True, False],
 [True, False, False, False],
 [False, True, False, True],
 [False, True, True, True]]

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
        diseases_definition()


def diseases_definition_test():
    test_list = [True, False, False, False]
    for i in range(len(diseases_list)):
        print(diseases_list[i])
        print(test_list)
        if diseases_list[i] == test_list:
            print("Судя по симптомам у вас мигрень")


def diseases_definition():
    symptom_list = []
    symptom_list.extend((headache, high_temperature, muscle_pain, cough))
    diseases_number = -1
    for i in range(len(diseases_list)):
        if diseases_list[i] == symptom_list:
            diseases_number = i
            break

    if diseases_number == -1:
        print("По вашим симптомам нельзя точно определить заболевание, требуется дополнительынй осмотр")
    if diseases_number == 0:
        print("Судя по вашим симптомам (головная боль, повышенная температура, боль в мышцах) ваш диагноз - ОРВИ")
    if diseases_number == 1:
        print("Судя по вашим симптомам (головная боль) ваш диагноз - Мигрень")
    if diseases_number == 2:
        print("Судя по вашим симптомам (повышенная температура, кашель) ваш диагноз - Covid19")
    if diseases_number == 3:
        print("Судя по вашим симптомам (повышенная температура, боль в мышцах, кашель) ваш диагноз - Туберкулез")


print("Добро пожаловать в онлайн-ассистент вашего районного Терапевта")
print("В случае, если онлайн-ассистент не помог обнаружить ваше заболевание - настоятельно просим посетить нормального врача")
get_questions(1)