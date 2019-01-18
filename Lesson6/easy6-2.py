__author__ = 'Чудесников Никита'

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class Trape ():
    def __init__(self, ax,ay,bx,by,cx,cy,dx,dy):
        self.AB = (math.sqrt(math.fabs((bx - ax)) ** 2 + math.fabs((by - ay)) ** 2))
        self.BC = (math.sqrt(math.fabs((cx - bx)) ** 2 + math.fabs((cy - by)) ** 2))
        self.CD = (math.sqrt(math.fabs((cx - dx)) ** 2 + math.fabs((cy - dy)) ** 2))
        self.AD = (math.sqrt(math.fabs((ax - dx)) ** 2 + math.fabs((ay - dy)) ** 2))
        self.vectAB = [bx - ax, by - ay]
        self.vectCD = [dx - cx, dy - cy]

    def _is_trape (self):
        if self.vectAB[0] / self.vectCD[0] == self.vectAB[1] / self.vectCD[1]:
            return False
        else:
            return True

    def _is_equal(self):
        if self._is_trape() == True:
            return  True if self.AB == self.CD else False
        else:
            return 'its not a trape'

    def sides_lenght(self):
        return self.AB, self.BC, self.CD, self.AD

    def _perimetr(self):
        return self.AB + self.BC + self.CD + self.AD


    def _square(self):
        _s = ((self.AD + self.CD) / 4) * math.sqrt((4 * self.AB ** 2) - (self.CD - self.BC) ** 2)
        return _s



if __name__ == '__main__':
    Tr = Trape(1,1,2,2,3,2,4,1)
    print('Is equal? ', Tr._is_equal())
    print('Sides lenght: ',Tr.sides_lenght())
    print('P = ',Tr._perimetr())
    print('S= ',Tr._square())
