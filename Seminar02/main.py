import os
import random
from random import randint
from random import sample
import time


def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Реализовать алгоритм пирамидальной сортировки (сортировка кучей)")    
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


def LEFT(i):
    return 2*i + 1

def RIGHT(i):
    return 2*i + 2

def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def heapify(A, i, size):
    left = LEFT(i)
    right = RIGHT(i)
 
    largest = i
    if left < size and A[left] > A[i]:
        largest = left
 
    if right < size and A[right] > A[largest]:
        largest = right
 
    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, size)

def pop(A, size):
    if size <= 0:
        return -1
 
    top = A[0]
    A[0] = A[size - 1]
    heapify(A, 0, size - 1)
 
    return top

def heapsort(A):
    n = len(A)
    i = (n - 2) // 2
    while i >= 0:
        heapify(A, i, n)
        i = i - 1
 
    while n:
        A[n - 1] = pop(A, n)
        n = n - 1
  


# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        # блок кода для исполнения программы
        if __name__ == '__main__':

            min_value = int(input("Введи минимальное число: "))
            max_value = int(input("Введи максимальное число: "))
            row = int(input("Введи количество чисел в диапазоне: "))

 
            
            start = time.time()
            list = sample(range(min_value, max_value), row)
            print("исходный список: ")
            print(list)
            heapsort(list)
            print("сортированный список: ")
            print(list)
            final = time.time()
            print(f"Затраченное время {final-start}")
        print("")
        



input('')
ClearConsole()
