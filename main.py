import random

r = [(3, 266), (13, 442), (10, 671), (9, 526), (7, 388), (1, 245), (8, 210), (8, 145), (2, 126), (9, 322)]  # 36
max_w = 35  # максимальный размер склада
k_vec = 20  # количество векторов ????
k = 50  # количество итераций

array_vec = []

for i in range(k_vec):
    vec = [0] * len(r)

    # Получение случайного числа элементов для замены
    num_ones = random.randint(1, len(r) - 1)  # ????

    # Получение списка случайных уникальных индексов
    indices = random.sample(range(len(r)), num_ones)

    # Замена элементов по индексам на 1
    weight = 0
    c = 0
    for index in indices:
        vec[index] = 1
        weight += r[index][0]
        c += r[index][1]

    data = [vec, weight, c]
    array_vec.append(data)

sorted_array_vec = sorted(array_vec, key=lambda x: x[2])
print(*sorted_array_vec, sep="\n")

