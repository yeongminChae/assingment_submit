end_point, start_point = 10, 2
total_range = end_point - start_point 
 
# X가 6보다 크고 8보다 작을 확률은 X가 6과 8사이에 존재할 확률 (8 - 6) = 2
target_range = 2 
probability = target_range / total_range

# 연속형 균등분포의 기댓값은 분포의 최대값과 최소값의 평균값
expected_val = (end_point + start_point) / 2

print(f'6보다 크고 8보다 작을 확률: {round(probability, 4)}')
print(f'연속형 균등분포의 기댓값: {expected_val}')

