import random
import numpy as np
import matplotlib.pyplot as plt

r = [(1, 119), (7, 134), (6, 126), (2, 4), (8, 68), (4, 58), (10, 165), (4, 41), (6, 51), (3, 168), (9, 6), (9, 49),
     (8, 124), (7, 45), (2, 117), (2, 176), (10, 94), (5, 190), (7, 165), (1, 179), (3, 168), (3, 23), (7, 101),
     (9, 139), (3, 172), (2, 107), (8, 192), (1, 105), (3, 26), (5, 162), (6, 147), (3, 25), (6, 178), (5, 28),
     (5, 121), (5, 66), (10, 76), (5, 118), (9, 147), (3, 183), (1, 15), (6, 5), (7, 53), (4, 123), (5, 29), (5, 75),
     (3, 194), (10, 8), (3, 39), (9, 155)]  # 36

sorted_r = sorted(r, key=lambda x: (x[0], x[1]))
print(sorted_r)

max_w = 47  # максимальный размер склада
k_vec = 200  # количество векторов  ????
k_osob = 100  # количество особей в каждой итерации для скрещивания ????
k = 100  # количество итераций
mutation = 0.1  # вероятность мутации

len_r = len(sorted_r)

population = []
evaluations = []

# генерация начальной популяции
for i in range(k_vec):
    vec = np.zeros(len_r)

    # Получение случайного числа элементов для замены
    num_ones = random.randint(1, len_r)

    # Получение списка случайных уникальных индексов
    indices = random.sample(range(len_r), num_ones)

    # Замена элементов по индексам на 1
    weight = 0
    c = 0
    for index in indices:
        if weight + sorted_r[index][0] > max_w:  # если превышает вес - то не берем индекс и идем дальше
            continue
        else:
            weight += sorted_r[index][0]
            vec[index] = 1
            c += sorted_r[index][1]

    # добавление веса, если вес не максимальный
    sorted_r_for_add = sorted_r.copy()
    while weight < max_w:
        for index in reversed(vec):  # цикл по вектору с конца
            if weight + sorted_r_for_add[-1][0] <= max_w:  # проверка, нужно ли добавлять
                weight += sorted_r_for_add[-1][0]
                index = 1
                c += sorted_r_for_add[-1][1]
                sorted_r_for_add.pop()
            else:  # если не нужно, то уже добавить не сможем, тк отсортированно по весу
                break
        break

    data = [vec, weight, c]
    population.append(data)

# Главный цикл генетического алгоритма
for i in range(k):
    # Отбор лучших векторов-кандидатов для скрещивания (здесь реализовать 3: случайный (+), линейный, квадратичный)

    # 1 - Случайный:
    parents = []
    for j in range(k_osob):  # количество потомков
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        parents.append((parent1, parent2))

    # Создание новой популяции путем скрещивания родителей
    new_population = []
    for parent_pair in parents:
        child = np.zeros(len_r)
        cross_point = random.randint(0, len_r - 1)
        parent1, parent2 = parent_pair

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
            if child[index] == 0 and weight + sorted_r[index][
                0] < max_w:  # если ген меняется на 1 и меньше размера склада
                weight += sorted_r[index][0]
                c += sorted_r[index][1]
                child[index] = 1 - child[index]
            elif child[index] == 1:  # если ген изменился на 0
                weight -= sorted_r[index][0]
                c -= sorted_r[index][1]
                child[index] = 1 - child[index]

        # добавление веса, если вес не максимальный
        sorted_r_for_add = sorted_r.copy()
        while weight < max_w:
            for index in reversed(child):  # цикл по вектору с конца
                if weight + sorted_r_for_add[-1][0] <= max_w:  # проверка, нужно ли добавлять
                    weight += sorted_r_for_add[-1][0]
                    index = 1
                    c += sorted_r_for_add[-1][1]
                    sorted_r_for_add.pop()
                else:  # если не нужно, то уже добавить не сможем, тк отсортированно по весу
                    break
            break

        data = [child, weight, c]  # c - функция качества
        new_population.append(data)  # добавляем потомка в популяцию

    # Объединение старой и новой популяции, сортировка и отбор лучших особей
    population.extend(new_population)
    sorted_population = sorted(population, key=lambda x: x[2], reverse=True)  # сортируем по убыванию функции качества
    population = sorted_population[:k_vec]  # оставляем выживших особей

    evaluations.append(population[0][2])

print(population[-1])  # последняя особь
print(evaluations[-1])  # макс результат

plt.plot(range(k), [i for i in evaluations], label='Best')
plt.xlabel('Итерации')
plt.ylabel('Функция качества (стоимость)')
plt.title('Результат работы')
plt.legend()
plt.show()
