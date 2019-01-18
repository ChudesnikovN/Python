__author__ = 'Чудесников Никита'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os

os.chdir('C:\\Datas')


class Factory():
    def __init__(self):
        self.workers = []
        self.fact = []

    def AddWorkers(self):
        with open("workers.txt") as file_handler:
            file_list = file_handler.read().splitlines()
        file_list = file_list[1:]
        for line in file_list:
            # print(line)
            self.workers.append(Worker(line))

    def GetFact(self):
        with open("hours_of.txt") as file_handler:
            file_list = file_handler.read().splitlines()
        file_list = file_list[1:]
        for _w in self.workers:
            for line in file_list:
                if line.split()[0] +' '+ line.split()[1] == _w.name:
                    _w.fact = int(line.split()[2])



    def PrintSalary(self):
        for worker in self.workers:
            if worker.fact >= worker.norma:
                Salary = worker.salary + 2* worker.salary *((worker.fact-worker.norma)/worker.norma)
            else:
                Salary = worker.salary * (worker.fact / worker.norma)
            print('{} норма: {}  отработал: {} Получка: {}'.format(worker.name, worker.norma, worker.fact,Salary))


    def WorkersInfo(self):
        for _w in self.workers:
            _w.WorkerInfo()

    def PrintFact(self):
        for _f in self.fact:
            _f.PrintVedomost()


class Worker():
    def __init__(self, str):
        self.name = str.split()[0] + ' ' + str.split()[1]
        self.salary = int(str.split()[2])
        self.norma = int(str.split()[4])


    def WorkerInfo(self):
        print('Name = {} Salary = {} Norma = {} Fact ={}'.format(self.name, self.salary, self.norma,self.fact))





PepsiCo = Factory()

PepsiCo.AddWorkers()
PepsiCo.GetFact()
PepsiCo.PrintSalary()


