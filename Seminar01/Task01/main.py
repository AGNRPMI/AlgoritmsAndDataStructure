import os
import sys
import random
from random import randint
import time
import math


def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("найти все простые числа от 1 до N, где N вводится пользователем. Реализовать три различных ")    
    print("алгоритма, включая решето Эратосфена. Оценить эффективность каждого подхода.")    
    print("Простое число - натуральное число p, которое делится на 1 и на само число p")    
    print("************************************************************************************************")
    print(" ")

def WorkingProcess():
    choice = None
    while not (choice == 'y' or choice == 'n'):
        choice = input("желаете выполнить алгоритм? (y/n)")
        if choice == 'y':
            print("выполняется программа...")
            print(" ")
            _isOpen = True
        elif choice == 'n':
            print("завершение программы... Нажмите Enter")
            print(" ")
            _isOpen = False
        else:
            print("команда не распознана, введите еще раз")
            print(" ")
    return _isOpen

def ClearConsole():
    os.system('cls')

def GetNumberRow():
    print("Необходимо определить диапазон для поиска простых чисел")
    print("Первое простое число = 2, последнее число должно быть больше 2")
    x = 0
    while not(x>2):
        try:
            x = int(input("Введите число больше чем 2: "))        
        except:
            print("Преобразование прошло неудачно, введи корректное значение")

    return int(x)

def UseSieveEratosthenes(n):
    start = time.time()
    N = int(n) 
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:            
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    final = time.time()
    print(f"задача решена Методом Решета Эратосфена за время :{final-start},")
    print(f"количество простых чисел от 0 до {N}: {primes.__len__()}")
    if primes.__len__()<=30:
        print(primes)
    else:
        print("слишком много значений, список выводиться не будет")
    
def UseEnumeration(n):
    start = time.time()
    primes = list()
    j = 0
    for number in range(0, n + 1): 
        if number > 1: 
            for i in range(2, number): 
                if(number % i) == 0: 
                    break 
            else:
                j= j+1 
                primes.insert(j,number)   

    final = time.time()
    print(f"задача решена Методом Перебора за время :{final-start},")
    print(f"количество простых чисел от 0 до {n}: {primes.__len__()}")
    if primes.__len__()<=30:
        print(primes)
    else:
        print("слишком много значений, список выводиться не будет")

def CheckPreviousNumber(n):
    start = time.time()
    primes = [2]
    for k in range(3, n+1, 2):
        i = 0
        while k > primes[i]:
            if k % primes[i] == 0:
                break
            if primes[i] * 2 > k:
                primes.append(k)
                break
            i +=1
    

    final = time.time()
    print(f"задача решена Методом Проверки деления на предыдущие числа за время :{final-start},")
    print(f"количество простых чисел от 0 до {n}: {primes.__len__()}")
    if primes.__len__()<=30:
        print(primes)
    else:
        print("слишком много значений, список выводиться не будет")

# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):    
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        #метод перебора, метод случайностей, метод бинарного поиска
        first_number = 2
        last_number = GetNumberRow()
        print("")
        UseSieveEratosthenes(last_number)
        print("")
        UseEnumeration(last_number)
        print("")
        CheckPreviousNumber(last_number)
        print("")
        
        
 
        
        
        



input('')
ClearConsole()
