import random
import time

import numpy as np
import matplotlib.pyplot as plt
import pylab

def addWeight(weight_, c_, vec_, max_w_, sorted_r_):  # добавление веса, если вес не максимальный
    indices = [i for i in range(len(vec_)) if vec_[i] == 0]
    indices = random.sample(indices, len(indices))

    for index in indices:
        if weight_ == max_w_:
            return [vec_, weight_, c_]
        if weight_ + sorted_r_[index][0] > max_w_:
            continue
        weight_ += sorted_r_[index][0]
        vec_[index] = 1
        c_ += sorted_r_[index][1]

    return [vec_, weight_, c_]


def makeChild(cross_point, parent1, parent2):
    child = np.zeros(len_r)
    weight = 0
    c = 0
    # Определение гена для потомка на основе родительских генов
    for l in range(cross_point):
        child[l] = parent1[0][l]  # первая часть копируется полностью
        if child[l] == 1:
            weight += sorted_r[l][0]
            c += sorted_r[l][1]
    for l in range(cross_point, len_r):  # вторую часть редактируем при необходимости
        if parent2[0][l] == 1:
            if weight + sorted_r[l][0] > max_w:  # копируем только то, что входит
                continue
            else:
                child[l] = parent2[0][l]
                weight += sorted_r[l][0]
                c += sorted_r[l][1]

    # Добавление случайной мутации (корректируем, если вышли за пределы)
    if random.random() < mutation:
        index = random.randint(0, len_r - 1)  # Выбор случайного гена
        if child[index] == 0 and weight + sorted_r[index][0] < max_w:  # если ген меняется w < w_склада
            weight += sorted_r[index][0]
            c += sorted_r[index][1]
            child[index] = 1 - child[index]
        elif child[index] == 1:  # если ген изменился на 0
            weight -= sorted_r[index][0]
            c -= sorted_r[index][1]
            child[index] = 1 - child[index]

    data = addWeight(weight, c, child, max_w, sorted_r)  # c - функция качества
    return data


def isEqual(parent1, parent2):
    if np.array_equal(parent1, parent2):
        return 1
    else:
        return 0

with open('items.txt', 'r') as f:
    content = f.readlines()

max_w = int(content[0].strip())

r = []
for line in content[1:]:
    item = tuple(map(int, line.strip().split()))
    r.append(item)
r.pop(0)

sorted_r = sorted(r, key=lambda x: (x[0], x[1]))
print(sorted_r)

k = 60  # количество итераций
len_r = len(sorted_r)

for i in range(1):
    print(f'\nНапишите через пробел: количество особей, количество особей для скрещивания и вероятность мутации')
    dt = input().split()
    k_vec = int(dt[0])
    k_osob = int(dt[1])
    mutation = float(dt[2])

start_time = time.time()
for test in range(1):
    print(f'\n\nОпыт {test + 1}:\n')
    population = []
    evaluations_random = []
    evaluations_linear = []
    evaluations_squar = []

    # генерация начальной популяции
    for i in range(k_vec):
        vec = np.zeros(len_r)
        num_ones = random.randint(1, len_r)  # Получение случайного числа элементов для замены
        indices = random.sample(range(len_r), num_ones)  # Получение списка случайных уникальных индексов
        weight = 0
        c = 0
        for index in indices:  # Замена элементов по индексам на 1
            if weight + sorted_r[index][0] > max_w:  # если превышает вес - то не берем индекс и продолжаем
                continue
            else:
                weight += sorted_r[index][0]
                vec[index] = 1
                c += sorted_r[index][1]

        data = addWeight(weight, c, vec, max_w, sorted_r)
        population.append(data)

    greate_population = sorted(population, key=lambda x: x[2], reverse=True)

    for ver in range(3):
        population = greate_population.copy()
        for i in range(k):  # Главный цикл генетического алгоритма
            # Отбор лучших векторов-кандидатов для скрещивания (3 способа)
            if ver == 0:
                # 1 - Случайный:
                parents = [(random.choice(population), random.choice(population)) for j in range(k_osob) if
                           not isEqual(random.choice(population), random.choice(population))]

            elif ver == 1:
                # 2 - Линейный:
                n = k_vec  # Количество особей
                population_by_probability = []  # Массив, отображающий вероятность выбора особи в зависимости от ее качества
                start = finish = 0
                for vec in population:
                    y = 2 * n
                    finish += y + 1
                    population_by_probability.extend([vec] * (finish - start))
                    n -= 1
                    start = finish + 1

                random.shuffle(population_by_probability)
                parents = []

                for j in range(k_osob):
                    parent1, parent2 = random.sample(population_by_probability, 2)

                    while isEqual(parent1, parent2) == 1 and len(population_by_probability) > 1:
                        parent2 = random.choice(population_by_probability)

                    parents.append((parent1, parent2))

            elif ver == 2:
                # 2 - Квадратичный:
                n = k_vec  # Количество особей
                population_by_probability_sq = []  # Массив, отображающий вероятность выбора особи в зависимости от ее качества
                start = finish = 0

                for vec in population:
                    y = n ** 2  # Квадратичный расчет параметра для распределения вероятностей
                    finish += y + 1
                    population_by_probability_sq.extend([vec] * (finish - start))
                    n -= 1
                    start = finish + 1

                random.shuffle(population_by_probability_sq)
                parents = []

                for j in range(k_osob):  # количество потомков
                    parent1, parent2 = random.sample(population_by_probability_sq, 2)

                    while isEqual(parent1, parent2) == 1 and len(population_by_probability_sq) > 1:
                        parent2 = random.choice(population_by_probability_sq)

                    parents.append((parent1, parent2))

            # Создание новой популяции путем скрещивания родителей
            new_population = []
            for parent_pair in parents:
                cross_point = random.randint(0, len_r - 1)
                parent1, parent2 = parent_pair

                new_population.append(makeChild(cross_point, parent1, parent2))  # 1 потомок
                new_population.append(makeChild(cross_point, parent2, parent1))  # 2 потомок

            # Объединение старой и новой популяции, сортировка и отбор лучших особей
            population.extend(new_population)
            sorted_population = sorted(population, key=lambda x: x[2],
                                       reverse=True)  # сортируем по убыванию функции качества
            population = sorted_population[:k_vec]  # оставляем выживших особей

            if ver == 0:
                evaluations_random.append(population[0][2])
            elif ver == 1:
                evaluations_linear.append(population[0][2])
            elif ver == 2:
                evaluations_squar.append(population[0][2])

        if ver == 0:
            print("Для случайной выборки")
            print(population[-1])  # последняя особь
            print(evaluations_random[-1])  # макс результат

            pylab.plot(range(k), [i for i in evaluations_random], label='Random')
        elif ver == 1:
            print("Для линейной выборки")
            print(population[-1])  # последняя особь
            print(evaluations_linear[-1])  # макс результат

            pylab.plot(range(k), [i for i in evaluations_linear], label='Linear')
        elif ver == 2:
            print("Для квадратичной выборки")
            print(population[-1])  # последняя особь
            print(evaluations_squar[-1])  # макс результат

            pylab.plot(range(k), [i for i in evaluations_squar], label='Squard')

        pylab.xlabel('Итерации')
        pylab.ylabel('Функция качества (стоимость)')
        pylab.title(f'Результат')
        pylab.legend()

print('Лучший ответ: ', max(evaluations_linear[-1], evaluations_random[-1], evaluations_squar[-1]))
print('Параметры: количество особей - ',  k_vec, ', количество особей для скрещивания - ', k_osob, ', вероятность мутации - ', mutation)

end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения: ", execution_time, "секунд")

plt.show()



