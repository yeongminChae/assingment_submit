from scipy.stats import binom  # type: ignore

n, p = 500, 0.0002
# n : 시행 횟수, p : 성공할 확률

probability = 1 - (binom.pmf(0, n, p) + binom.pmf(1, n, p))

print(f'두 명 이상이 해당 될 확률: {round(probability, 4)}')
print(f'이항분포의 기댓값: {n * p}')  
print(f'이항분포의 분산: {round(n * p * (1 - p), 4)}')

