import os
import random
from random import randint
import time
import math
import sys
from itertools import combinations
from random import sample



def PrintTaskDescription():
    print(" ")
    print("************************************************************************************************")
    print("Создать Бинарное дерево с балансировкой, добавлением и удаление элементов")    
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

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
 
class Tree:
    def __init__(self):
        self.root = None
 
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
 
        if value == node.data:
            return node, parent, True
 
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
 
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
 
        return node, parent, False
 
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
 
        s, p, fl_find = self.__find(self.root, None, obj.data)
 
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
 
        return obj
 
    def show_tree(self, node, _up_or_down):
        
        if node is None:
            return
        
        if _up_or_down == 'u':
            self.show_tree(node.left, _up_or_down)
            print(node.data)
            self.show_tree(node.right, _up_or_down)
        if _up_or_down == 'd':
            self.show_tree(node.right, _up_or_down)
            print(node.data)
            self.show_tree(node.left, _up_or_down)
 
    def show_wide_tree(self, node):
        print("Отображение дерева в ширину:")
        if node is None:
            return
 
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn
 
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
 
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
 
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
 
        return node, parent
 
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)
 
        if not fl_find:
            return None
 
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)
 
def GenerateList():
    min_value = int(input("Введи минимальное число: "))
    max_value = int(input("Введи максимальное число: "))
    row = int(input("Введи количество чисел в диапазоне: "))
    list = sample(range(min_value, max_value), row)
    return list 

def AddNewElements():
    entered_list = input("Введите числа, разделенные пробелом: ").split()
    num_list = list(map(int, entered_list))
    return num_list

def PrintListCommand(keys_dict = dict()):
    for keys, value in keys_dict.items():
        print(keys,":", value)

def TransformationCommand(tree = Tree(), list_1=list()):
    hot_keys = {'1' : 'показать список', '2' : 'добавить элементы', '3':'сортировать элементы', 
                '4': 'удалить элементы', '5' : 'показать дерево', '0' : 'выход из меню'}
    
    command = None

    while not (command == hot_keys.keys):
        print("")
        PrintListCommand(hot_keys)
        print("")
        command = input("Введите команду: ")
        if command == '1':
            print(list_1)
            

        elif command == '2':
            new_list = AddNewElements()
            for x in new_list:
                tree.append(Node(x))
            
            for number in new_list:
                if number not in list_1:
                    list_1.append(number)
                
            print("элементы добавлены")
            

        elif command == '3':
            up_or_down = None
            while not (up_or_down == 'u' or up_or_down == 'd'):
                print("сортировка по возрастанию(u) или по убыванию(d)")
                up_or_down = input("введите (u) или (d)")
                if up_or_down == 'u':
                    print("по возрастанию: ")
                    break
                    
                elif up_or_down == 'd':
                    print("по убыванию: ")
                    break
                    
                else:
                    print("команда не распознана, введите еще раз")
                    
                    
            t.show_tree(t.root, up_or_down)
            

        elif command == '4':
            del_element = int(input("введите удаляемый элемент: "))
            tree.del_node(del_element)
            list_1.remove(del_element)
            print(f"элемент {del_element} удален")
            

        elif command == '5':
            tree.show_wide_tree(tree.root)
            

        elif command == '0':
            print("")
            break
            
        else:
            print("команда не распознана, введите еще раз")
            print(" ")
    



# начало главного метода
ClearConsole()
PrintTaskDescription()
isOpen = True # true задается по умолчанию для хотя бы одного запуска
while (isOpen):
    isOpen = WorkingProcess()

    if isOpen == True:
        v = list()
        
        new_list = None
        while not (new_list == 'y' or new_list == 'n'):
            new_list = input("сгенерировать список? (y/n)")
            if new_list == 'y':
                v = GenerateList()
                print("создается список:")
                
            elif new_list == 'n':
                print("используем список по умолчанию:")
                v = [10, 5, 7, 16, 13, 2, 20]
                
            else:
                print("команда не распознана, введите еще раз")
                print(" ")
        print(v)
        print()

        t = Tree()

        for x in v:
            t.append(Node(x))
        
        TransformationCommand(t, v)
       
        print("")
        
   
input('')
ClearConsole()
