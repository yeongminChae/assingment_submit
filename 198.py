from scipy.stats import binom

n = 1000  # 사람의 수
p = 0.002  # 한 사람이 질병 A로 사망할 확률

a = binom.pmf(0, n, p)  # 0명 사망할 확률
b = binom.pmf(1, n, p)  # 1명 사망할 확률
total_prob = a + b  # 1명 이하가 사망할 확률

expected_value = n * p  # 기댓값 계산

print(f"연간 1명 이하가 질병 A로 인해 사망할 확률: {round(total_prob, 4)}")
print(f"기댓값 (연간 사망자 수): {expected_value}")
