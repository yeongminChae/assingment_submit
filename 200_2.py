a = 0.02  # 질병에 걸린 사람의 비율
b = 1 - a  # 질병에 걸리지 않은 사람의 비율
c = 0.01  # 질병에 걸린 사람이 음성 반응을 보일 확률
d = 0.98  # 질병에 걸리지 않은 사람이 음성 반응을 보일 확률

negative_and_disease = d * b  # 검사가 음성이면서 실제로 질병에 걸리지 않은 경우의 확률
all_negative_case = c * a + d * b  # 검사가 음성으로 나올 수 있는 모든 경우의 확률

print(
    f"진단 검사 결과가 음성 반응일 때, 이 사람이 질병에 걸리지 않았을 확률: {round(negative_and_disease / all_negative_case, 4)}")
