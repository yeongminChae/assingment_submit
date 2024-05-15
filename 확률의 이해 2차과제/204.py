from scipy.stats import poisson  # type: ignore

lambda_param = 500 * 0.0002
# 포아송 분포의 파라미터는 어느 단위 시간이나 공간에서 
# 어떤 사건이 발생하는 평균 횟수를 의미합니다.

prob = poisson.pmf(0, lambda_param) + poisson.pmf(1, lambda_param)
probabilities = 1 - prob

print(f'두 명 이상이 해당 될 확률: {round(probabilities, 4)}')
print(f'포아송 분포의 기댓값: {lambda_param}')  
print(f'포아송 분포의 분산: {lambda_param}')