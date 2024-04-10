from scipy.stats import poisson

n = 1000  # 사람의 수
p = 0.002  # 한 사람이 질병 A로 사망할 확률

expected_value = p * n  # 기대값 & 포아송 분포의 매개변수 (평균)

prob = poisson.cdf(1, expected_value)  # 연간 1명 이하가 사망할 확률

print(f"연간 1명 이하가 질병 A로 인해 사망할 확률: {round(prob, 4)}")
print(f"기댓값 (연간 사망자 수): {expected_value}")
