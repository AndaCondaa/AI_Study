# ML 정리

- Deep Learning 으로 나아가기 위한 ML 기본 지식 정리
- 따라서, DL과 직접적인 연관성이 적은 Tree Model 등은 제외

<br>

<br>

## 메모

- Feature 관련
  - 트리가 아닌 선형/비선형 모델에서는 정규화 필수
  - 0/1 이진 특성의 경우는 그대로 사용
  - 순서형/범주형 변수는 원핫인코딩해서 바이너리로 만드는게 좋음 -> 순서형에서 1,2,3 과 같은 값이 그 사이의 크기를 반영하여 모델이 학습할 수 있음

<br>

<br>

## Regularization

- 과대적합을 억제
- 가중치를 0에 가깝게 -> 특성이 출력에 주는 영향 ⬇️-> 모델의 복잡도 ⬇️  -> 일반화 ⬆️

- Ridge (L2 Regularization)
  - L2 Norm의 제곱을 패널티로 적용
  - alpha ⬆️ -> regularization ⬆️
  - 결과 : 부드러운 모델
- Lasso (L1 Regularization)
  - 실제로 0이 되는 계수가 생김 -> Feature selection으로 볼 수 있음
  - alpha ⬆️ -> regularization ⬆️
  - 결과 : 희소 모델

<br>
<br>

