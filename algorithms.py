def bisection(input_range : list, f , epsilon: float) -> float:
    a = input_range[0]
    b = input_range[1]
    x = (a + b) / 2

    if f(x) == 0:
        return x

    while abs(f(x)) > epsilon:
        if f(a) * f(x) < 0:
            b = x
        if f(x) * f(b) < 0:
            a = x
        x = (a + b) / 2
    return x

def newton(input_range : list, f, d, iterations: int) -> float:
    x = input_range[0]
    for i in range(iterations):
        x = x - (f(x)/d(x))
    return x