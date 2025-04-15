# DL 정리

## Loss Function

- 신경망은 결국 Loss Function을 가지고 손실이 최소가 되는 매개변수, 즉 가중치를 찾는 과정

- <b>특정 매개변수일 때,  정해지는 손실함수의 미분에 집중</b>❗️

- 정확도를 지표로 삼으면, 거의 모든 곳에서 미분값이 0이기 때문에 학습에 사용할 수 없음, 즉 손실함수의 미분가능 연속성때문에 사용함 (활성화함수로 계단함수를 생각)

- 종류
  - 오차제곱합(SSE)
    - $E =\frac{1}{2} \sum(y_k-t_k)^2$
    - 분류 문제일 경우?
      - 모든 타겟(타겟종류)에 대한 Sigmoid 또는 Softmax 값을 가지고 적용하기 때문에 분류에서는 잘 사용 ❌
  - Cross Entropy Error (CEE)
    - $E = - \sum t_k\log y_k$
    - 분류에서 원핫인코딩 된 경우, 정답값이 아닌 레이블은 $t_k$가 0이 되므로, 정답 레이블로 추정한 확률로 확인하는 개념

<br>

<br>

## Backpropagation

수치미분 대신 손실함수의 기울기를 계산하는 방법 → 해석적 방법

<br>

<br>

## Optimization

- SGD
  - $W ← W - \eta \frac{\partial L}{\partial W}$
  - 문제에 따라 지그재그 형태를 보이면서 비효율적으로 찾아가는 문제가 있음
- Momentum
  - $v ← \alpha v - \eta \frac{\partial L}{\partial W}$ 
  - $W ← W + v$
- AdaGrad
  - $h ← h + \frac{\partial L}{\partial W} \odot \frac{\partial L}{\partial W}$ 
  - $W ← W - \eta \frac{1}{\sqrt h}\frac{\partial L}{\partial W}$ 
  - Learning rate decay 기술을 적용
  - 개별 매개변수에 <b>Ada</b>ptive하게 학습률을 조정하면서 진행
  - h의 역수를 곱해주고 있기 때문에, 크게 갱신된 매개변수는 학습률이 점차 작아짐
- Adam
  - Mometum과 AdaGrad를 융합한 듯한 방법
  - ❗️❗️논문 참고

<br>

<br>

## 학습 관련 기술

- 초기값 
  - Weight decay
    - 과대적합을 억제해서 범용 성능을 높이는 테크닉
  - 일반적으로 가중치를 균일한 값으로 설정하면, 오차역전파법에서 모든 가중치의 값이 똑같이 갱신되는 문제 발생 -> 무작위로 설정해야 함
  - 문제
    - Gradient vanishing
      - 가중치를 표준편차 1인 정규분포를 사용할 때,  활성화 함수의 출력이 0과 1에 치우쳐 분포하게 되면 역전파의 기울기 값이 점점 작아지다가 사라짐
    - 표현력 제한
      - 표준편차를 줄이면 gradient vanishing 문제는 사라지지만, 뉴런에서 모두 비슷한 값을 출력하면서 표현력을 제한함
  - Xavier 초기값 (자비에 초기값)
    - 앞 층의 입력 노드 수와 다음 층의 출력 노드 수를 고려한 설정값 제안
    - 간단하게는 앞 계층의 노드가 $n$개일 때, 표준편차가 $\frac{1}{\sqrt n}$인 분포를 사용
    - 활성화 함수가 선형이라는 전제로 이끈 결과이기때문에,  tanh, sigmoid일 때는 중앙 부근이 선형이라고 볼 수 있어서 적당함, ReLU에서는 부적절❌❌
  - He 초기값 (카이밍 히)
    - 앞 계층의 노드가 $n$개일 때, 표준편차가 $\sqrt \frac{2}{n}$인 분포를 사용















































































