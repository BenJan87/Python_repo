from classes import Eliptic_curve_finite_field, Point
import math


def find_point_leading_infinity(P: Point, curve: Eliptic_curve_finite_field):
    new_y = -P.y % curve.p
    print(new_y)
    x_1, x_2, x_3 = cubic_roots(curve.a, curve.b - (new_y)**2)
    print(x_1 % curve.p)
    return x_1, x_2, x_3



def cubic_roots(c, d, a=1, b=0):
    delta0 = b*b - 3*a*c
    delta1 = 2*b*b*b - 9*a*b*c + 27*a*a*d
    C = ((delta1 + math.sqrt(delta1*delta1 - 4*delta0*delta0*delta0))/2)**(1/3)
    if C == 0:
        x1 = x2 = x3 = -b / (3*a)
    else:
        x1 = (-b + C + delta0/C)/(3*a)
        x2_real = x3_real = (-b - (1 + 1j*math.sqrt(3))*C + delta0/((1 + 1j*math.sqrt(3))*C))/(3*a)
        x2_imag = (b + (1 + 1j*math.sqrt(3))*C - delta0/((1 + 1j*math.sqrt(3))*C))/(6*a)
        x3_imag = (b - (1 + 1j*math.sqrt(3))*C - delta0/((1 + 1j*math.sqrt(3))*C))/(6*a)
    return x1, (x2_real + x2_imag*1j), (x3_real + x3_imag*1j)


if __name__ == "__main__":
    p = 9739
    curve = Eliptic_curve_finite_field(497, 1768, p)
    P = Point(8045, 6936)
    result = find_point_leading_infinity(P, curve)
    print(result)