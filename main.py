import random
import numpy as np
import matplotlib.pyplot as plt
import pylab


def addWeight(weight_, c_, vec_, max_w_, sorted_r_):  # добавление веса, если вес не максимальный
    sorted_r_for_add = sorted_r_.copy()
    while weight_ < max_w_:
        for i in range(len(vec_)):  # цикл по вектору
            if weight_ + sorted_r_for_add[0][0] <= max_w_ and vec_[i] == 0:  # проверка, можно ли добавлять
                weight_ += sorted_r_for_add[0][0]
                vec_[i] = 1
                c_ += sorted_r_for_add[0][1]
                sorted_r_for_add.pop(0)
            else:  # если не нужно, то уже добавить не сможем, тк отсортированно по весу
                break
        break
    return [vec_, weight_, c_]


def isEqual(parent1, parent2):
    if np.array_equal(parent1, parent2):
        return 1
    else:
        return 0


r = [(11, 137), (6, 62), (7, 160), (15, 34), (3, 16), (5, 182), (12, 37), (15, 114), (12, 55), (9, 41), (12, 130),
     (13, 33), (10, 72),
     (9, 18), (2, 181), (7, 142), (5, 14), (8, 126), (12, 62), (9, 183), (4, 28), (2, 114), (6, 125), (3, 98), (1, 105),
     (6, 52), (12, 125),
     (12, 164), (13, 133), (11, 48), (11, 172), (2, 133), (4, 191), (4, 28), (12, 56), (2, 136), (5, 142), (14, 185),
     (7, 53), (2, 9),
     (14, 154), (11, 83), (4, 85), (5, 59), (3, 148), (14, 17), (7, 43), (3, 154), (10, 87), (12, 147), (13, 161),
     (13, 52), (14, 3),
     (11, 72), (8, 10), (1, 91), (7, 141), (6, 132), (2, 161), (3, 111), (15, 16), (8, 110), (4, 24), (11, 51),
     (13, 43), (10, 106),
     (15, 141), (15, 109), (2, 22), (4, 74), (13, 57), (11, 156), (4, 68), (15, 26), (8, 12), (13, 82), (15, 14),
     (15, 161), (15, 123),
     (13, 183), (3, 31), (4, 58), (11, 46), (11, 55), (13, 171), (11, 107), (9, 35), (9, 38), (11, 54), (4, 163),
     (12, 181), (8, 63), (2, 38),
     (2, 143), (5, 93), (8, 40), (10, 183), (6, 169), (7, 178), (9, 92)]

r = [(54, 297),
     (95, 295),
     (36, 293),
     (18, 292),
     (4, 291),
     (71, 289),
     (83, 284),
     (16, 284),
     (27, 283),
     (84, 283),
     (88, 281),
     (45, 280),
     (94, 279),
     (64, 277),
     (14, 276),
     (80, 275),
     (4, 273),
     (23, 264),
     (75, 260),
     (36, 257),
     (90, 250),
     (20, 236),
     (77, 236),
     (32, 235),
     (58, 235),
     (6, 233),
     (14, 232),
     (86, 232),
     (84, 228),
     (59, 218),
     (71, 217),
     (21, 214),
     (30, 211),
     (22, 208),
     (96, 205),
     (49, 204),
     (81, 203),
     (48, 201),
     (37, 196),
     (28, 194),
     (6, 193),
     (84, 193),
     (19, 192),
     (55, 191),
     (88, 190),
     (38, 187),
     (51, 187),
     (52, 184),
     (79, 184),
     (55, 184),
     (70, 181),
     (53, 179),
     (64, 176),
     (99, 173),
     (61, 172),
     (86, 171),
     (1, 160),
     (64, 128),
     (32, 123),
     (60, 114),
     (42, 113),
     (45, 107),
     (34, 105),
     (22, 101),
     (49, 100),
     (37, 100),
     (33, 99),
     (1, 98),
     (78, 97),
     (43, 94),
     (85, 94),
     (24, 93),
     (96, 91),
     (32, 80),
     (99, 74),
     (57, 73),
     (23, 72),
     (8, 63),
     (10, 63),
     (74, 62),
     (59, 61),
     (89, 60),
     (95, 56),
     (40, 53),
     (46, 52),
     (65, 50),
     (6, 48),
     (89, 46),
     (84, 40),
     (83, 40),
     (6, 35),
     (19, 28),
     (45, 22),
     (59, 22),
     (26, 18),
     (13, 15),
     (8, 12),
     (26, 11),
     (5, 6),
     (9, 5)]

sorted_r = sorted(r, key=lambda x: (x[0], x[1]))
print(sorted_r)

# max_w = 58  # максимальный размер склада
max_w = 3818
k = 60  # количество итераций
len_r = len(sorted_r)

for i in range(1):
    print(f'\nНапишите через пробел: количество особей, количество особей для скрещивания и вероятность мутации')
    dt = input().split()
    k_vec = int(dt[0])
    k_osob = int(dt[1])
    mutation = float(dt[2])

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

        print(indices)
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

                data = addWeight(weight, c, child, max_w, sorted_r)  # c - функция качества
                new_population.append(data)  # добавляем потомка в популяцию

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
        pylab.legend
        pylab.text(0, 0, "My Text", fontsize=14)

plt.show()
