"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
KEGS_AMOUNT = 90
NUMS_AMOUNT = 9
NUMS_IN_LINES = 1
LINES_AMOUNT = 1

class Card:
    def __init__(self,nums_amount,lines_amount, nums_in_lines):
        self.card = []
        self.NumIndex = []
        self.nums_amount = nums_amount
        self.lines_amount = lines_amount
        self.nums_in_lines = nums_in_lines


    def Generate(self):
        _index = []
        tmp =[]
        for j in range (0,self.lines_amount):
            _index = list(range(j*self.nums_amount, (j + 1) * self.nums_amount))
            for i in range(0,self.nums_in_lines):
                x = random.choice(_index)
                self.NumIndex.append(x)
                _index.remove(x)
        self.NumIndex.sort()
        print(self.NumIndex)

        nums = list(range(1, KEGS_AMOUNT + 1))
        for j in range(0,self.lines_amount):
            for i in range(0,self.nums_in_lines):
                x = (random.choice(nums))
                tmp.append(x)
                tmp.sort()
                nums.remove(x)
            self.card.extend(tmp)
            tmp = []
        print(self.card)

    def PrintCard(self):
        tmp_index = 0
        print ('--*'*self.nums_amount)
        for i in range(0, self.lines_amount * self.nums_amount):
            if i in self.NumIndex:
                if len(str(self.card[tmp_index])) == 1:
                    print(' '+ str(self.card[tmp_index]),end=' ')
                else:
                    print(str(self.card[tmp_index]), end =' ')
                tmp_index += 1
            else:
                print('--',end =' ')
            if (i+1) % self.nums_amount == 0:
                print()
        print('--*'*self.nums_amount)

    def IsIn(self,num):
        for i in range (0, len(self.card)):
            if str(self.card[i]) == str(num):
                self.card[i] = 'xx'
                return True
        return False

    def IsEmpty(self):
        fl = True
        for _item in self.card:
            if _item != 'xx':
                fl = False
                break
        return fl



if __name__ == '__main__':
    #Kegs = []
    Kegs = list(range(1, KEGS_AMOUNT+1))
    random.shuffle(Kegs)
    MyCard = Card(NUMS_AMOUNT, LINES_AMOUNT, NUMS_IN_LINES)
    MyCard.Generate()
    CompCard = Card(NUMS_AMOUNT, LINES_AMOUNT, NUMS_IN_LINES)
    CompCard.Generate()

    for i in Kegs:
        print('Ваша карточка:')
        MyCard.PrintCard()
        print('Карточка компьютера:')
        CompCard.PrintCard()
        print('Выпал бочонок: ',i)
        answer = input('Зачеркнете? y/n ')
        if answer == 'y':
            if MyCard.IsIn(i) == True:
                CompCard.IsIn(i)
            elif MyCard.IsIn(i) == False:
                print ('Вы проиграли!')
                break
        elif answer == 'n':
            if MyCard.IsIn(i) == True:
                print('Вы проиграли!')
                break
            elif MyCard.IsIn(i) == False:
                CompCard.IsIn(i)

        if MyCard.IsEmpty() == True:
            print('Вы выиграли!!')
            MyCard.PrintCard()
            break
        if CompCard.IsEmpty() == True:
            print('Увы, компьютер выиграл!!')
            CompCard.PrintCard()
            break

