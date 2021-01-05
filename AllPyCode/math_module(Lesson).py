import math

# math.pi передает чмсло пи

print(math.pi)

# math.e передает число Эйлера(2.718281828459045)

print(math.e)

# math.exp(x) вычисляет экспонент числа в скобках (e(число Эйлера) в степени x)

an_int = 6
a_neg_int = -8
a_float = 2.00

print(math.exp(an_int))
print(math.exp(a_neg_int))
print(math.exp(a_float))

# P.S если передать не число, то будет ошибка(TypeError)

# math.log(x), math.log10(), math.log2(), math.log(x, y) все это вычисляет логарифм числа в скобках
# если переданно только одно числло то по умолчанию будет использованно число Эйлера(см.Пример)

print(math.log(10))
print(math.log10(50))
print(math.log2(8))
print(math.log(8, 2))
print(math.log1p(10))

# math.ceil() округляет число вверх

print(math.ceil(20.3))

# math.fabs() модуль числа

print(math.fabs(-23))

# math.floor() округляет число вниз

print(math.floor(20.3))

# math.fsum(iterable) возвращает сумму всех элементов

print(math.fsum([1, 2, 3]))

# math.gcd(x, y) передает наибольший общий делитель

print(math.gcd(8, 100))

# math.expm1(x) возвращает число Эйлера в степени x и отнимает от результата 1

print(math.expm1(2))
print(2.718281828459045 * 2.718281828459045)

# pow(x, y) или math.pow(x, y) возводит x в степень y

print(pow(2, 2), math.pow(2, 2))

# math.sqrt() прердает квадратный корень числа

print(math.sqrt(22))

# math.sin(a) прердает синус a в радианах

print(math.sin(20))

# math.cos(a) прердает косинус a в радианах

print(math.cos(20))

# math.tan(a) прердает тангенс a в радианах

print(math.tan(20))

# math.asin(a) передает инвертированный синус, также есть math.acos(a), math.atang(a).

x = math.cos(20)

print(math.asin(x))  # !!! принимает только синус, также и в math.acos() и math.atang()

# math.degrees(a) конвертирует радианны в градусы а math.radians(a) наоборот

print(math.degrees(20), math.radians(20))

# math.copysign(x, y) возвращает модуль числа x со знаком числа y

print(math.copysign(2, 1), math.copysign(2, -1))

# math.factorial(x) передает факториал числа x

print(math.factorial(20))

# math.fmod(x, y) передает остаток при делении x на y

print(math.fmod(20, 43))

# math.frexp(x) передает мантиссу и экспоненту числа x

print(math.frexp(20))

# math.ldexp(x, i) передает X * (2 в степени i)

print(math.ldexp(20, 2))

# math.isfinite(x) проверет являеться ли x числом

print(math.isfinite(2))

# math.isnan(x) проверяет являеться ли x не числом

print(math.isnan(2))

# math.isinf(x) проверяет бесконечность ли x

i = 10/3

print(math.isinf(i))

# math.modf(x) передает дробную и целую часть числа

print(math.modf(20.222))

# math.trunc(x) делает число x целым

print(math.trunc(20.57))

# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) показывает близки ли числа a и b друг к другу
# rel_tol прередает максимальную разницу для близости
# abs_tol прередает минимальную разницу для близости
# они оба принимают от 0 до 1 где 0.01 это 1 процент а 1 это 100 процентов

print(math.isclose(2, 2))

print(math.isclose(2, 2.2, rel_tol=0.05, abs_tol=0.001))

print(math.isclose(2, 2.2, rel_tol=0.3, abs_tol=0.2))

# math.isqrt(x) возвращает квадратный корень числа

print(math.isqrt(4))
