import os
import sys
import random
from random import randint
import time
import math
from itertools import combinations


def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("сделать задачу про игральные кубики и количество различных комбинаций.")    
    print("То есть 1,2 равнозначно 2,1 и считается за одну комбинацию.")    
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

def GetNumDice():
    print("Введите количество бросаемых кубиков (не менее 1): ")
    x = 0
    while not(x>0):
        try:
            x = int(input("Введите число не менее 1: "))        
        except:
            print("Преобразование прошло неудачно, введи корректное значение")

    return int(x)

def GetNumSideDice():
    print("Введите количество граней у бросаемых кубиков (не менее 4): ")
    x = 0
    while not(x>3):
        try:
            x = int(input("Введите число не менее 4: "))        
        except:
            print("Преобразование прошло неудачно, введи корректное значение")

    return int(x)

def GetTypeDice(_num_dice, _num_side_dice):
    max_num_combinations = _num_side_dice ** _num_dice
    print(f"Вы бросаете {_num_dice} кубиков с количеством сторон {_num_side_dice}")
    print(f"бросок типа {_num_dice}d{_num_side_dice}, максимальное количество комбинаций {max_num_combinations}")
    print("")
    return max_num_combinations

def UseEnumerationComb(_num_dice, _num_side_dice, _max_num_combinations):
    start = time.time()
    unique_combinations = list()
    L = [i+1 for i in range(_num_side_dice)]
    
    unique_combinations = [",".join(map(str, comb)) for comb in combinations(L, _num_dice)]

    
    
    
    final = time.time()
    
    print(f"задача решена через вложенные списки за время :{final-start},")
    print(f"Количество уникальных комбинаций составляет {unique_combinations.__len__()} из {_max_num_combinations} возможных ")
    print()


def Factorial(n):
    fact = 1    
    for i in range(1, n+1):
        fact = fact * i
    return fact

def GetMathCombination(_num_dice, _num_side_dice, _max_num_combinations ):
    start = time.time()
    unique_comb = Factorial(_num_side_dice) / (Factorial(_num_side_dice- _num_dice)*Factorial(_num_dice))

    final = time.time()
    print(f"задача решена через факториал за время :{final-start},")
    print(f"количество уникальных комбинаций {unique_comb} из возможных {_max_num_combinations}")
    
    

# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        num_dice = GetNumDice()
        num_side_dice = GetNumSideDice()
        max_num_combinations = GetTypeDice(num_dice, num_side_dice)
        GetMathCombination(num_dice, num_side_dice, max_num_combinations )
        print("")
        UseEnumerationComb(num_dice, num_side_dice, max_num_combinations)
        print("")
        #UseEnumerationComb(num_dice, num_side_dice, max_num_combinations)
        #print("")
        



input('')
ClearConsole()