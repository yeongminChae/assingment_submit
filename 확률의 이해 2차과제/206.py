from scipy.stats import norm # type: ignore

# 정규분포의 기댓값은 mu, 분산은 sigma^2 입니다.
mu, sigma = 12, 3 

# X가 6보다 크고 7보다 작을 확률을 구하기 위해서는 각각의 cdf를 구하고,
# 상한에서 하한을 빼줍니다.
probability = norm.cdf(7, mu, sigma) - norm.cdf(6, mu, sigma)

print(f'6보다 크고 7보다 작을 확률: {round(probability, 4)}')

