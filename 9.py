# coding=utf-8
import numpy as np
import random
import timeit

while True:
    vvod = input(' ')  # Вибираємо одне із значень для нашої змінної
    metod = input(' ')
    sortirovka = input(' ')


    def bubl_up(s):  # заводимо функцію для бульбашкового методу по зростанню
        global count  # Заводим 2 лічильника і робимо їх глобальними щоб мати змогу викликати їх при необхідності
        global shanger
        count = 0
        shanger = 0
        for i in range(1, n):  # Бульбашковий алгоритм
            for j in range(n - 1, i - 1, -1):
                count += 1
                if (A[j - 1] > A[j]):
                    shanger += 1
                    A[j], A[j - 1] = A[j - 1], A[j]
        print(A)


    def bubl_down(s):  # заводимо функцію для бульбашкового методу по спаданню
        global count
        global shanger
        count = 0
        shanger = 0
        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):
                count += 1
                if (A[j - 1] < A[j]):
                    shanger += 1
                    A[j], A[j - 1] = A[j - 1], A[j]
        print(A)


    def select_up(s):  # функція для алгоритму сортування(зростання)
        global count_se
        global shanger_se
        count_se = 0
        shanger_se = 0
        for i in range(n - 1):  # алгоритм вибору
            min = i
            for j in range(i + 1, n):
                count_se += 1
                if A[j] < A[min]:
                    shanger_se += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)


    def select_down(s):  # функція для алгоритму сортування(спадання)
        global count_se
        global shanger_se
        count_se = 0
        shanger_se = 0
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                count_se += 1
                if A[j] > A[min]:
                    shanger_se += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)


    def insertion_up(s):  # функція для алгоритму сортування вставки(зростання)
        global count_ins
        global shanger_ins
        count_ins = 0
        shanger_ins = 0
        for i in range(1, n):  # алгоритм вставки
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] > key:
                count_ins += 2
                shanger_ins += 1
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
        print(A)


    def insertion_down(s):  # функція для алгоритму сортування вставки(спадання)
        global count_ins
        global shanger_ins
        count_ins = 0
        shanger_ins = 0
        for i in range(1, n):
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] < key:
                count_ins += 2
                shanger_ins += 1
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
        print(A)


    if vvod == '1':
        x = int(input('Введіть кількість цифр'))
        A = np.zeros(x, dtype=int)  # масив з випадковими значеннями
        for i in range(x):
            A[i] = random.randint(0, 100000)
        print(A)
        n = len(A)
        s = x
    else:
        x = int(input('Введіть кількість цифр'))
        while x > 30:
            x = int(input('Введіть кількість до 30'))
        A = np.zeros(x, dtype=int)
        for i in range(x):
            A[i] = int(input('Введіть число '))
        print(A)
        n = len(A)
        s = x


    def xarakteristika_bubl(countner):  # функції для оцінки методів
        print(countner)
        print(shanger)
        t = timeit.timeit(number=10000)
        print(t)


    def xarakteristika_select(countner):
        print(countner)
        print(shanger_se)
        t = timeit.timeit(number=10000)
        print(t)


    def xarakteristika_ins(countner):
        print(countner)
        print(shanger_ins)
        t = timeit.timeit(number=10000)
        print(t)


    if metod == '1':
        if sortirovka == '1':
            bubl_up(s)
            xarakteristika_bubl(countner=count)  # counter поіменований параметр функції
        else:
            bubl_down(s)
            xarakteristika_bubl(countner=count)
    elif metod == '2':
        if sortirovka == '1':
            select_up(s)
            xarakteristika_select(countner=count_se)
        else:
            select_down(s)
            xarakteristika_select(countner=count_se)
    else:
        if sortirovka == '1':
            insertion_up(s)
            xarakteristika_ins(countner=count_ins)
        else:
            insertion_down(s)
            xarakteristika_ins(countner=count_ins)
    result = input('Хочите продовжити? Якщо так - 1, Якщо ні - інше: ')  # повторне виконання програми
    if result == '1':
        continue
    else:
        break
