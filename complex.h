/*
 *
 *  C++ version
 *
 */

/* Complex.h */

#ifndef Complex_H
#define Complex_H

#include <iostream>

using std::ostream;

struct Complex {

    Complex(int = 0, int = 1);

    Complex operator+(const Complex &) const;
    Complex operator-(const Complex &) const;
    Complex operator*(const Complex &) const;
    Complex operator/(const Complex &) const;

    Complex operator+(int) const;
    Complex operator-(int) const;
    Complex operator*(int) const;
    Complex operator/(int) const;

    friend Complex operator+(int, const Complex &);
    friend Complex operator-(int, const Complex &);
    friend Complex operator*(int, const Complex &);
    friend Complex operator/(int, const Complex &);

    friend ostream &operator<<(ostream &, const Complex &);

private:

    int b;
    int a;
};

#endif /* Complex_H */
