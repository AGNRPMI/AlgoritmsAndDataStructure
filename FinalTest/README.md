## Описание программы

Данная программа разработана согласно условия:

>Упрощенный вариант - бинарное дерево с балансировкой, добавление, удалением элементов.

>Необходимо превратить собранное на семинаре дерево поиска в полноценное 
левостороннее красно-черное дерево. И реализовать в нем метод добавления 
новых элементов с балансировкой.

Красно-черное дерево имеет следующие критерии:
• Каждая нода имеет цвет (красный или черный)
• Корень дерева всегда черный
• Новая нода всегда красная
• Красные ноды могут быть только левым ребенком
• У краной ноды все дети черного цвета

Соответственно, чтобы данные условия выполнялись, после добавления элемента 
в дерево необходимо произвести балансировку, благодаря которой все критерии выше станут валидными. 
Для балансировки существует 3 операции – левый малый поворот, правый малый поворот и смена цвета.

## Критерии оценивания:
Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"
"Зачет" ставится, если слушатель успешно выполнил
"Незачет"" ставится, если слушатель успешно выполнил


Слушатель превратить собранное на семинаре дерево поиска в полноценное левостороннее красно-черное дерево. 
И реализовать в нем метод добавления новых элементов с балансировкой.
плюс вся документация по классам и методам
'''

----------


## Описание алгоритма работы
1. Генерируется рандомный список или используется список по умолчанию
2. создаются Node, которым присваиваются значения списка
3. Node добавляется в Tree. первое значение в списке - корневое значение
4. через контекстное меню выбирается команда взаимодействия
   1. выводится список без изменений
   2. добавляются новые элементы в список и в Node. если добавляемое значение меньше значения в родительском узле, то новая вершина добавляется в левую ветвь, иначе - в правую. добавляются только уникальные значения
   3. сортировка по возрастанию или убыванию
   4. удаление элементов
   5. вывод дерева по ширине

--------

## Описание работы
* class Node - определяет вершины (ячейки с данными) бинарного дерева, в классе производится его инициализация. имеются указатели на правого и леовго потомка
* class Tree - определение класса бинарного дерева
    * def \__init__(self) - инициализатор
    * def __find(self, node, parent, value) рекурсивная функция поиска существующей вершины, к которой необходимо добавить новое значение по левой и правой ветви
    * def append(self, obj) - добавление вершины, в него передается класс Node. по условию
    если добавляемое значение меньше значения в родительском узле, то новая вершина добавляется в левую ветвь, иначе в правую. если добавляемое значение уже присутствует в дереве, то оно игнорируется 
    * def show_tree(self, node) - рекурсивная функция, отображающее бинарное дерево, показывает элементы в порядке возрастания или в порядке убывания на выбор пользователя
    * def show_wide_tree(self, node) - функция отображения дерева в ширину
    * def del_node(self, key) - функция удаление вершины 
    * def __del_leaf(self, s, p) - удаление листа (терминального дочернего элемента)
    * def __del_one_child(self, s, p) - удаление узла и переопределение новой вершины
    * def __find_min(self, node, parent) - поиск минимального элемента, реализуется для функции del_node(self, key)
* def GenerateList() - создание рандомного списка, если не требуется то создается список по умолчанию
* def AddNewElements() - добавление пользователем новых элементов в дерево с консоли
* def PrintListCommand(keys_dict = dict()) - вывод списка команд
* def TransformationCommand(tree = Tree(), list_1=list()) - реализация меню команд для взаимодействия с деревом
* WorkingProcess() - запускает цикл, предназначенный для повторного запуска приложения без использования команд консоли. программа запускается, на консоль выводится условия работы, описание и возможные команды. выбрав команду "y", программа выполняет указанный алгоритм, затем пользователю предлагается выполнить программу повторно, либо завершить работу 
* def ClearConsole() - зачистка консоли в начале работы и в конце
---------