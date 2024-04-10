def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def permutation(n, m):
    return factorial(n) / factorial(n-m)


def combination(n, m):
    return permutation(n, m) / factorial(m)


answer = combination(7, 2) / combination(10, 2)
print(f"구입 상품 중 불량품이 하나도 없는 경우의 확률 : {round(answer, 3)}")
print(f"구입 상품 중 불량품이 적어도 하나 있는 경우의 확률 : {round(1 - answer, 3)}")
