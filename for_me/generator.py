import eseries
import random

footprints = ["SO-2", "SOT-23", "DIP-8"]
components = ["резистора", "предохранителя", "диода", "светодиода", "варикапа"]

def create_task_1(res1, res2, vol, cap, i):
    

    task_1 = [f"Выполнить виртуальное моделирование делителя напряжения в программном обеспечении MultiSim. Результатом моделирования продемонстрировать график с указанием Uвх. и Uвых. в режиме анализа переходных процессов. Применить курсоры. Исходные данные: R1 = {res1} Ом; R2  = {res2} Ом; Uвх. = {vol} В;", f"Выполнить виртуальное моделирование делителя напряжения в программном обеспечении KiCAD. Результатом моделирования продемонстрировать график с указанием Uвх. и Uвых. в режиме анализа переходных процессов. Применить курсоры. Исходные данные: R1 = {res1} Ом; R2  = {res2} Ом; Uвх. = {vol} В;", f"Выполнить виртуальное моделирование RC-цепи в программном обеспечении MultiSim. Результатом моделирования продемонстрировать график с указанием постоянной времени τ. На графике должно быть порядка 6τ. Исходные данные: R = {res1} Ом; C = {cap} нФ; U = {vol} В;", f"Выполнить виртуальное моделирование RC-цепи в программном обеспечении KiCAD. Результатом моделирования продемонстрировать график с указанием постоянной времени τ. На графике должно быть порядка 6τ. Исходные данные: R = {res1} Ом; C = {cap} нФ; U = {vol} В;"]
    
    return task_1[i]

def create_task_2(fp, comp, i):
    task_2 = [f"Создать УГО {comp} в программном обеспечении Altium Designer в соответствии с требованиями ЕСКД.",
              f"Создать посадочное место {fp} в программном обеспечении Altium Designer на основе информации из технической документации (Datasheet).",
              f"Настроить правила проектирования в программном обеспечении Altium Designer в соответствии с Приложением №1."]
    return task_2[i]

def send_1():
    res1 = eseries.find_nearest(eseries.E12, random.randint(0, 100000))
    res2 = eseries.find_nearest(eseries.E12, random.randint(0, 100000))
    vol = random.randint(5, 30)
    cap = eseries.find_nearest(eseries.E12, random.randint(0, 100))
    i = random.randint(0, 3)
    task1 = create_task_1(res1, res2, vol, cap, i)
    return task1

def send_2():
    fp = footprints[random.randint(0, 2)]
    comp = components[random.randint(0, 4)]
    i = random.randint(0, 2)
    task2 = create_task_2(fp, comp, i)
    return task2
    
for j in range(30):
    print(f"Билет №{j+1}")
    print("1.", send_1(), "\n")
    print("2.", send_2(), "\n")
    