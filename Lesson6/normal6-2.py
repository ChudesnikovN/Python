__author__ = 'Чудесников Никита'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы !!!
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика !!!
# 5. Получить список всех Учителей, преподающих в указанном классе
FAMILIES = ('Иванов', 'Петров','Сидоров','Кузнецов','Петренко','Столыпин','Саакян','Егоров','Морозов')
NAMES =  ('Ф.','А.','Д.','С.','Л.','В.','П.','Я.')
SUBJ = ('математика','физика','химия','литература','русский язык','иностранный язык')
import random
class School():
    def __init__(self,name):
        self.classes = []
        self.name = name

    def add_class(self,class_name):
        #idx = Class(class_name)
        self.classes.append(class_name)

    def ShowClasses(self):
        for cl in self.classes:
            print (cl.name)

    def ShowParents(self,name):
        for i in self.classes:
            for pup in i.pupils:
                if i.name == name:
                    pup.show_pup_parents()

    def ShowTeachers(self):
        for i in self.classes:
            for tc in i.teachers:
                tc.show_teacher()

    def Generate(self,classes,pupils,subjects):
        for id in range (int(classes)):
            i_class_name = str(random.randint(1,10)) + random.choice(('A','Б','В'))
            i_class = Class(i_class_name)
            self.add_class(i_class)
            for i in range(int(pupils)):
               i_class.add_pup(Pupil(random.choice(FAMILIES) + ' ' +random.choice(NAMES),
                                random.choice(FAMILIES) + ' ' +random.choice(NAMES),
                                random.choice(FAMILIES) + ' ' + random.choice(NAMES)))
            for i in range(int(subjects)):
                i_class.add_teach(random.choice(FAMILIES) + ' ' +random.choice(NAMES), random.choice(SUBJ))

    def showPupilInfo(self,name):
        for cl in self.classes:
            for pup in cl.pupils:
                if pup.name == name:
                    for teach in cl.teachers:
                        print((pup.name, cl.name, teach.name, teach.subject))


    def ShowPupils(self):
         for cl in self.classes:
             for pup in cl.pupils:
                 print(pup.name)

class Class() :
    def __init__(self,name):
        self.pupils = []
        self.name = name
        self.teachers = []

    def add_pup(self,name):
        self.pupils.append(name)

    def add_teach(self,name,subj):
        self.teachers.append(Teacher(name,subj))

    def show_teachers(self):
        for tc in self.teachers:
            print(tc.subject)

    def show_pupils(self):
        for pup in self.pupils:
            print(pup)

class Pupil():
    def __init__(self,name,mother,father):
        self.name = name
        self.mother = mother
        self.father = father

    def show_pup_parents(self):
        print ('Pupil: {}  His mother: {} His father: {}'.format(self.name,self.mother,self.father))


class Teacher():
    def __init__(self,name,subj):
        self.name = name
        self.subject = subj

    def show_teacher(self):
        print (self.name, self.subject)


