__author__ = 'Чудесников Никита'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

import math


class Triangle:

    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.bx = bx
        self.cx = cx
        self.ay = ay
        self.by = by
        self.cy = cy
        self.AB = (math.sqrt(math.fabs((bx - ax)) ** 2 + math.fabs((by - ay)) ** 2))
        self.BC = (math.sqrt(math.fabs((cx - bx)) ** 2 + math.fabs((cy - by)) ** 2))
        self.AC = (math.sqrt(math.fabs((ax - cx)) ** 2 + math.fabs((ay - cy)) ** 2))


    def _perimetr(self):
        P = self.AB + self.BC + self.AC
        return P

    def _square(self):
        _half_p = self._perimetr()
        S = math.sqrt(_half_p * (_half_p - self.AC) * (_half_p - self.AB) * (_half_p - self.BC))
        return S

    def _height(self):
        _s = self._square() * 2 / self.AC
        return _s


if __name__ == '__main__':
    tria = Triangle(1,1,2,2,3,1)
    tria2 =Triangle(2,2,3,3,4,2)
    print('Height = ', tria2._height())
    print('Square = ', tria2._square())
    print('Perimetr = ', tria2._perimetr())
