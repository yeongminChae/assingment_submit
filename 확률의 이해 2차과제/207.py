import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.stats import uniform # type: ignore

# 균등분포의 시작점과 분포의 너비 설정
start = 2
width = 8  # 10 - 2

# 확률밀도함수(PDF)와 누적확률분포(CDF)를 위한 x 값 생성
x = np.linspace(0, 12, 1000)
pdf = uniform.pdf(x, start, width)
cdf = uniform.cdf(x, start, width)

# PDF 그리기
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, pdf, 'r-', lw=2)
plt.title('확률밀도함수 (PDF)')
plt.xlabel('X')
plt.ylabel('확률밀도')
plt.grid(True)

# CDF 그리기
plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'b-', lw=2)
plt.title('누적확률분포 (CDF)')
plt.xlabel('X')
plt.ylabel('누적확률')
plt.grid(True)

plt.tight_layout()
plt.show()
