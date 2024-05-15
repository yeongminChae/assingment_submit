from scipy.stats import binom  # type: ignore

n, p, k = 10, 0.5, 5
# n : 시행 횟수, p : 성공할 확률, k : 성공 횟수

probability = binom.pmf(k, n, p)

print(f'5명이 치유될 확률: {round(probability, 3)}')
print(f'치유차수의 평균: {n * p}')  
print(f'치유차수의 분산: {n * p * (1 - p)}')

