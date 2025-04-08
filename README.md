# ML 정리

- Deep Learning 으로 나아가기 위한 ML 기본 지식 정리
- 따라서, DL과 직접적인 연관성이 적은 Tree Model 등은 제외

<br>
<br>

## 필요 ❗️❗️❗️❗️❗️❗️❗️❗️
분류 회귀 등에서 사용되는 로스함수를 정리하자 !<br>
분류 회귀 등에서 사용되는 정확도에 대한 지표를 정리하자 !<br>
그리고 그에따른 tol값 쓰는 것도 이해하자<br>


## 메모

- Feature 관련
  - 트리가 아닌 선형/비선형 모델에서는 정규화 필수
  - 0/1 이진 특성의 경우는 그대로 사용
  - 순서형/범주형 변수는 원핫인코딩해서 바이너리로 만드는게 좋음 -> 순서형에서 1,2,3 과 같은 값이 그 사이의 크기를 반영하여 모델이 학습할 수 있음
- 나이브 베이즈 분류
  - 각 특성을 개별로 취급하여 파라미터를 학습하고, 각 특성에서의 클래스 통계를 단순히 취합하는 방식

<br>

<br>

## Regularization

- 과대적합을 억제
- 가중치를 0에 가깝게 -> 특성이 출력에 주는 영향 ⬇️-> 모델의 복잡도 ⬇️  -> 일반화 ⬆️
- Ridge (L2 Regularization)
  - L2 Norm의 제곱을 패널티로 적용
  - 결과 : 부드러운 모델
- Lasso (L1 Regularization)
  - 실제로 0이 되는 계수가 생김 -> Feature selection으로 볼 수 있음
  - 결과 : 희소 모델

<br>
<br>

## SVM

- 매개변수 설정과 데이터 스케일에 아주 민감함

- Kernel trick : 데이터를 고차원 공간에 매필함
  - 다항식 커널 : 특성의 가능한 조합을 지정된 차수까지 모두 계산
  - RBF(radial basis function)(가우시안 커널) : 차원이 무한한 특성 공간에 매핑
- Support Vector = 결정 경계에 위치한 데이터 포인트
- Parameters
  - gamma (가우시안 커널에서 사용)
    - 가우시안 커널 폭의 역수
    - 작은 값은 넓은 영역, 큰 값은 좁은 영역
    - gamma ⬆️ -> 모델 복잡도 ⬆️
  - C
    - 규제
    - 각 포인트의 중요도 (dual_coef_값)을 제한
    - C ⬆️ -> 모델 복잡도 ⬆️
- 비슷한 의미의 특성으로 이루어진 중간 규모 데이터셋에 잘 맞음

- 샘플이 많거나 스케일이 다르면 별로 좋지 않음, 매개변수에 아주 많이 민감함
- BUT, 스케일이 비슷한 (예. 픽셀값) 경우는 괜찮음.

<br>

<br>

## MLP

- 여거 개의 가중치 합을 은닉층을 통해 계산하는 것은 결국 수학적으로는 하나의 가중치 합을 추정하는 것과 같아서, 선형 모델과 같음 -> 따라서 또 다른 기교가 필요 -> 활성화 함수 (activation function) -> 더 복잡한 함수 학습 가능
  - ReLU(rectified linear unit) - (0, 무한)
  - 하이퍼볼릭 탄젠트(hyperbolic tangent) - (-1, 1)
  - Logistic (sigmoid function) - (0, 1) (비추천❌)
- 보통 분류의 경우 신경망 마지막 출력층에 sigmoid/softmax 함수를 적용하여 최종 출력 y를 계산
-  Hidden Unit과 Hidden Layer의 개수가 중요함
- 신경망의 복잡도 제어
  - 은닉층의 수
  - 은닉층의 유닛 개수
  - 규제 (alpha)
  - Dropout - 은닉층 유닛의 일부를 작동시키지 않아서 앙상블시키는 것 같은 효과
  - Early Stop
- 먼저 충분히 과대적합되어서 문제를 해결할 만한 큰 모델 생성 -> 이후, 구조를 줄이거나 규제를 강화해서 일반화 성능 향상
