#
#
# Python version
#
#

class Complex:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, int):
            return Complex(self.a + other * self.b, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a * other.b + other.a * self.b, self.b * other.b)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, int):
            return Complex(self.a, self.b * other)
        elif isinstance(other, Complex):
            return Complex(self.a * other.b, self.b * other.a)
        else:
            raise TypeError

    def __float__(self):
        return float(self.a) / self.b

    def __int__(self):
        return self.a / self.b

    def __mul__(self, other):
        if isinstance(other, int):
            return Complex(self.a * other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a * other.a, self.b * other.b)
        else:
            raise TypeError

    def __radd__(self, other):
        return self + other

    def __rtruediv__(self, other):
        return Complex(other) / self

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return Complex(other) - self

    def __str__(self):
        return '(' + str(self.a) + ' / ' + str(self.b) + ')'

    def __sub__(self, other):
        if isinstance(other, int):
            return Complex(self.a - other * self.b, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a * other.b - other.a * self.b, self.b * other.b)
        else:
            raise TypeError

if __name__ == '__main__':

    a = Complex(1, 2)
    b = Complex(2, 3)

    i = 5

    print('%s + %s = %s' % (a, b, a + b))
    print('%s - %s = %s' % (a, b, a - b))
    print('%s * %s = %s' % (a, b, a * b))
    print('%s / %s = %s' % (a, b, a / b))

    print('%s + %i = %s' % (a, i, a + i))
    print('%s - %i = %s' % (a, i, a - i))
    print('%s * %i = %s' % (a, i, a * i))
    print('%s / %i = %s' % (a, i, a / i))

    print('%i + %s = %s' % (i, a, i + a))
    print('%i - %s = %s' % (i, a, i - a))
    print('%i * %s = %s' % (i, a, i * a))
    print('%i / %s = %s' % (i, a, i / a))