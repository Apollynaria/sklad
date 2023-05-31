import random

r = [(3, 266), (13, 442), (10, 671), (9, 526), (7, 388), (1, 245), (8, 210), (8, 145), (2, 126), (9, 322)]  # 36
max_w = 35  # максимальный размер склада
k_vec = 20  # количество векторов ????
k = 50  # количество итераций

array_vec = []

for i in range(k_vec):
    vec = [0] * len(r)  # массив 0
    array_r = r.copy()  # копируем изначальный массив
    weight_vec = 0
    c = 0
    random.shuffle(array_r)
    for j in range(len(r)):
        if not array_r:  # проверяем, есть ли еще элементы в списке
            break
        rnd_el = array_r.pop()
        individual = r.index(rnd_el)  # выбор случайной особи из всех
        if r[individual][0] + weight_vec <= max_w:
            vec[individual] = 1
            weight_vec += r[individual][0]
            c += r[individual][1]
    pair = [vec, c]
    array_vec.append(pair)

sorted_array_vec = sorted(array_vec, key=lambda x: x[1])
print(*sorted_array_vec, sep="\n")


