import matplotlib.pyplot as plt
import numpy as np
import random
import csv 
import os
import datetime

def ex_1():
    for i in range(100):
        if i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        else:
            print(i)
    pass

def ex_2():
    print("Podaj ilosc liczb do wygenerowania:")
    n = int(input()) 
    print("Podaj zakres dolny:")
    a = int(input()) 
    print("Podaj zakres gorny")
    b = int(input())
    random_num_ls = []

    for _ in range(n):
        random_num = random.uniform(a, b)
        random_num_ls.append(round(random_num))

    with open('wyniki.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(random_num_ls))

    pass

def ex_3():
    read_num = []
    with open('wyniki.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                read_num.append(float(value))
    n = len(read_num)
    mean = sum(read_num) / n
    sd = [(x - mean) ** 2 for x in read_num]
    standard_deviation = (sum(sd) / n) ** 0.5
    max_value = max(read_num)
    min_value = min(read_num)
    sort = sorted(read_num)
    print(mean)
    print(standard_deviation)
    print(min_value)
    print(max_value)
    print(sort)
    pass

def ex_4(n):
    n = int(input("Podaj liczbę:"))

    def fibo_gen(n):
        a, b = 0, 1

        for _ in range(n):
            yield a
            a, b = b, a + b
    fib = fibo_gen(n)
    for num in fib:
        print(num)
    return n

def ex_5():
    n = int(input())

    def plot_fibo(n):
        def fibo_gen(n):
            a, b = 0, 1

            for _ in range(n):
                yield a
                a, b = b, a + b

        fib = fibo_gen(n)
        fibo_numbers = [num for num in fib]

        plt.figure(figsize=(8, 6))
        plt.plot(fibo_numbers, marker='o', linestyle='-', color='r')
        plt.title(f'Ciag fibonacziego(pierwsze {n} liczb)')
        plt.xlabel('Indeks')
        plt.ylabel('Wartosc liczbowa')
        plt.grid(True)
        plt.show()

    plot_fibo(n)
    pass

def ex_6():
    n = int(input())

    def gen_slownik(n):
        slownik = {x: x**2 for x in range(1, n+1)}
        for key, value in slownik.items():
           print(f"Klucz: {key}, Wartość: {value}")
        return slownik

    wynik = gen_slownik(n)
    pass

def ex_7():
    n = int(input())

    def gen_slownik(n):
        slownik = {x: x**2 for x in range(1, n+1)}
        for key, value in slownik.items():
           print(f"Klucz: {key}, Wartość: {value}")
        return slownik
        
    def sum_slownik(slownik):
        suma = sum(slownik.values())
        print(f"Suma wartości w słowniku: {suma}")
        return suma

    wynik = gen_slownik(n)
    sum_slownik(wynik)
    pass

def ex_8():
    pass

def ex_9():
    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()

