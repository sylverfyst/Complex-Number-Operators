/* Complex.cc */

#include <iostream>
#include "Complex.h"

//division still needs to be done, as does the conjugate function

Complex::Complex(int a, int b) : a(a), b(b) {}

Complex Complex::operator+(const Complex &o) const {

    return Complex(a + o.a, b + o.b);
}

Complex Complex::operator+(int n) const {

    return Complex(a + n, b);
}

Complex Complex::operator-(const Complex &o) const {

    return Complex(a - o.a, b - o.b);
}

Complex Complex::operator-(int n) const {

    return Complex(a - n, b);
}

Complex Complex::operator*(const Complex &o) const {

    return Complex((a * o.a) - (b * o.b), (a * o.b) + (b * o.a));
}

Complex Complex::operator*(int n) const {

    return Complex(a * n, b * n);
}

Complex Complex::operator/(const Complex &o) const {

    return Complex(a * o.b, b * o.a);
}

Complex Complex::operator/(int n) const {

    return Complex(a, b * n);
}

Complex operator+(int n, const Complex &o) {

    return o + n;
}

Complex operator-(int n, const Complex &o) {

    return Complex(n) - o;
}

Complex operator*(int n, const Complex &o) {

    return o * n;
}

Complex operator/(int n, const Complex &o) {

    return Complex(n) / o;
}

ostream &operator<<(ostream &out, const Complex &o) {

    out << "(" << a << " + " << b << "i " << ")";
    return out;
}