#### [ML 정리](docs/ML.md)

#### [DL 정리](docs/DL.md)

# Computer Vision

<br>

## 이미지 분류

대부분의 합성곱 네트워크는 특징맵의 크기를 줄이면서 차원 수를 증가시키는 구조

LeNet , AlexNet, VGG, GoogLeNet, ResNet

#### LeNet

- 활성화 함수로 출력층에서 시그모이드, 나머지 계층에서 하이퍼볼릭 탄젠트 사용

#### AlexNet

- 최대값 풀링, ReLU
- LeNet과의 중요한 차이
  - ReLU 사용 -> 기울기 소실 문제 X, 기울기 소실 문제는 계층을 깊게 쌓을 수 없게 만들기 때문에 중요함
  - 드롭아웃 추가 -> 과대적합 완화

#### VGG

- AlexNet이 11x11, 5x5, 3x3의 큰 커널을 사용한 것과 달리, 3x3의 작은 커널만을 사용하여 Local Features 학습에도 좋고 비선형성을 더 많이 확보

#### ResNet

- 기본 블록에서는 3x3 2개 계층을 블록으로 해서 잔차연결
- 병목 블록에서는 1x1, 3x3, 1x1 게층을 묶어서 블록화, 연상량 감소, ResNet-50, 101, 152에서 사용





## F1

- 요약
  - F1-score - Precision과 Recall의 조화 평균 (하나의 클래스에 대해 계산)
  - Macro F1 - 각 클래스의 F1-score 평균 (모든 클래스 동등하게)
  - Micro F1 - 전체 TP/FP/FN을 먼저 합산한 뒤 F1 계산 (전체 평균) (클래스 비율을 반영하지 XXX)
  - Weighted F1 - 클래스별 F1을 클래스 비율로 가중 평균
- Precision
  - 양성이라고 판단한 것 중 실제로 양성인 것의 비율
  - 진양성/(진양성+위양성)
- Recall
  - 실제 양성인 것 중 모델이 양성이라고 예측한 것의 비율
  - 진양성/(진양성+위음성)

- F1 score
  - 2 * (Precision * Recall) / (Precision + Recall)
  - 조화 평균인 이유 : Precision과 Recall 중 더 작은 값에 영향을 많이 받게 하기 위함
