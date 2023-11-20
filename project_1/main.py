import matplotlib.pyplot as plt
import numpy as np
import random
import csv 

def ex_1():

    for i in range(100):
        if i% 3 == 0: 
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        elif i%5 ==0 and i%3 ==0:
            print("FizzBuzz")
        else:
            print(i)
    pass

def ex_2():
        import csv 
        import random 
        print("Podaj ilosc liczb do wygenerowania:")
        n = int(input()) 
        print("Podaj zakres dolny:")
        a = int(input()) 
        print("Podaj zakres gorny")
        b = int(input())
        random_num_ls = []

        for _ in range(n):
            random_num = random.uniform(a,b)
            random_num_ls.append(round(random_num))

        with open('wyniki.csv', mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(zip(random_num_ls))

    pass

def ex_3():
    import csv
    read_num = []
    with open('wyniki.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                read_num.append(float(value))
    n = len(read_num)
    mean = sum(read_num)/n
    sd = [(x-n)**2 for x in read_num]
    standard_deviation = sum(sd)/n
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
    return n

def ex_5():
    pass

def ex_6():
    pass

def ex_7():
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
