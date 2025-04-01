# ML_Study

딥러닝에 들어가기 전, 전통적인 머신러닝에 대한 학습을 정리함.

<br>

## Flow

<b>데이터 전처리 ▶︎ 데이터 분석 ▶︎ 평가</b>

<br>

<b>➢ 데이터 전처리</b>

▶️데이터의 결측치 확인

▶️데이터의 경향성 확인 (EDA 관점)

▶️훈련 세트와 테스트 세트 분할

▶️<b>데이터를 그냥 한 번 Plot하면서 보는 것도 중요!!! 산점도 확인!!❗️❗️❗️</b>

▶️<b>Feature Engineering</b>❗️

▶️<b>Standard Scale</b>❗️

<br>

<br>

## Regression

#### 🔹K-Nearest Neighbor Regression

단순히 가장 근접한 이웃의 평균값으로 회귀

#### 🔹Linear Regression

#####         ➢ Polynomial Regression

​            독립변수의 차수를 높임, 데이터 산점도가 곡선일 경우 유리하게 적용될 수 있음

#####         ➢ Multiple Regression

​            여러 개의 독립변수를 사용, 이 경우 Feature Scaling이 필요함.

#####         ➢ Lidge, Lasso 

​            규제를 추가한 선형회귀

<br>

<br>

## Classification

#### 🔹 K-Nearest Neighbor Classification

가장 근접한 이웃에 따라 분류

#### 🔹Logistic Regrssion

이름은 회귀이지만, 분류 모델.

​        ▶️ 시그모이드 : 이진 분류에서 z값을 0~1사이로 만듦.

​        ▶️ 소프트맥스 : 다중 분류에서 모든 클래스의 확률 합을 1로 만듦. 즉 정규화

#### 🔹SVM (Support Vector machine)❗️❗️

혼자 학습해 볼 필요 있음❗️

<br>

<br>

<br>

## Gradient Descent

데이터에 대한 손실함수의 최소값을 찾는 방법. 특정 weight에서의 학습 데이터의 error를 계산하고, 다음 Weight를 계산하는 과정.

🔹Batch Gradient Descent

모든 데이터에 대해 평균 에러를 계산하여 다음 Weight를 정함.

🔹Stochastic Gradient Descent

랜덤으로 하나의 데이터에 대해 손실을 계산하여 다음 Weight를 정함. Local minima 위험 가능성 높음.

🔹Mini Batch Gradient Descent

랜덤으로 몇 개의 데이터에 대한 평균 에러를 계산하여 다음 Weight를 정함.



Epoch: 모든 훈련 세트를 다 사용한 경우 1 에포크

- sklearn의 partial_fit()은 1 에포크 만을 학습함.



