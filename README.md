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

▶️<b>데이터를 그냥 한 번 Plot하면서 보는 것도 중요</b>

▶️<b>Feature Engineering</b>❗️

▶️<b>Standard Scale</b>❗️

<br>

<br>

## Regression

#### 🔹K-Nearest Neighbor Regression

단순히 가장 근접한 이웃의 평균값으로 회귀

#### 🔹Linear Regression

#####         ➢ Polynomial Regression

#####         ➢ Multiple Regression

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

데이터에 대한 손실함수의 최소값을 찾는 방법

🔹Batch Gradient Descent

모든 데이터에 대한 MSE(손실함수 예.)를 계산하여 다음 Weight를 정함



