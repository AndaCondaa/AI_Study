# ML 정리

- Deep Learning 으로 나아가기 위한 ML 기본 지식 정리
- 따라서, DL과 직접적인 연관성이 적은 Tree Model 등은 제외





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

