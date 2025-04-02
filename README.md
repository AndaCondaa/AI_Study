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

- <b>모델을 선정할 때는 초기에 Cross Validation을 활용해서 빠르게 모델이 낼 수 있는 퍼포먼스를 대략적으로 확인</b>

<br>



# Supervised Learning

## Regression

#### 🔹K-Nearest Neighbor Regression

단순히 가장 근접한 이웃의 평균값으로 회귀

#### 🔹Linear Regression

#####         ➢ Polynomial Regression

- 독립변수의 차수를 높임, 데이터 산점도가 곡선일 경우 유리하게 적용될 수 있음

#####         ➢ Multiple Regression

- 여러 개의 독립변수를 사용, 이 경우 Feature Scaling이 필요함.

#####         ➢ Lidge, Lasso 

- 규제를 추가한 선형회귀

<br>

<br>

## Classification

#### 🔹 K-Nearest Neighbor Classification

- 가장 근접한 이웃에 따라 분류

#### 🔹Logistic Regrssion

- 이름은 회귀이지만, 분류 모델.

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

- 모든 데이터에 대해 평균 에러를 계산하여 다음 Weight를 정함.

🔹Stochastic Gradient Descent

- 랜덤으로 하나의 데이터에 대해 손실을 계산하여 다음 Weight를 정함. Local minima 위험 가능성 높음.

🔹Mini Batch Gradient Descent

- 랜덤으로 몇 개의 데이터에 대한 평균 에러를 계산하여 다음 Weight를 정함.



Epoch: 모든 훈련 세트를 다 사용한 경우 1 에포크

- sklearn의 partial_fit()은 1 에포크 만을 학습함.

<br>

<br>

<br>

## Decsion Tree

🔹불순도 impurity

- criterion 매개변수 -> default: 'gini'

🔹정보이득 information gain

- 부모와 자식 노드 사이의 불순도 차이

🔹max_depth

- 트리의 깊이 조절 가능

🔹결정 트리는 표준화 필요 X

<br>

<br>

<br>

## Cross Validation

🔹sklearn의 cross_validate() 함수로 cv 값에 따른 score를 확인

🔹테스트 세트를 사용해서 모델이 낼 수 있는 퍼포먼스를 확인할 수 있음

🔹이 후 모델을 사용할 경우 모델 학습은 새로 해야함

<br>

<br>

<br>

## Hyperparameter Tunning

🔹GridSearchCV

🔹RandomizedSearchCV - Scipy로 unifrom, randint 등의 랜덤값 입력

<br>

- 그리드서치와 랜덤서치 모두 교차검증은 자동으로 포함되어 수행됨.

- best_estimator_에 가장 높은 점수를 받은 매개변수 조합으로 모델이 저장됨.

- CV 기본값은 5

- 따라서 수행은 (파라미터 경우의 수) * (CV 수)

<br>

<br>

<br>

## Tree Ensemble

🔹RandomForest

- Bootstrap sample : 독립 시행 샘플 -> 여러 개의 트리에서 중복 샘플이 있을 수 있음

- ❗️❗️oob_score=True  : 뽑은 샘플을 제외한 나머지로 훈련한 결정 트리를 평가 -> 교차 검증과 유사

- n_estimators : 트리 개수
- criterion : 손실 함수

🔹Extra Trees

- 일부 특성을 랜덤하게 선택하여 노드를 분할
- 부트스트랩 샘플말고 전체 샘플 사용

🔹Gradient Boosting

- 깊이가 얕은 결정 트리를 사용함
- subsample = 1 일 때, 모든 샘플 사용
- subsample값을 조정하면 확률적 경사 하강법이나 미니배치 경사 하강법과 비슷함

🔹Histogram-based Gradient Boosting

- 입력 특성을 256개의 구간으로 나눔 -> 최적의 분할을 빠르게 찾을 수 있음

🔹XGBoost

-Tree 외에 선형도 제공함, 'Hist'로 히스토그램 기반으로도 가능함

🔹LightGBM

<br>

<br>

<br>

<br>

# Unsupervised Learning

## K-Means Clustering

1. 임의의 클러스터 중심(Centroid)을 정하고, 그 중심에 가까운 샘플을 몇 개씩 선택하여 클러스터로 묶음
2. 클러스터 안에 있는 샘플들의 평균으로 Centroid를 조정함
3. 조정된 Centroid로 새로 클러스터를 묶음
4. 클러스터의 샘플 구성 변화가 없으면 종료



🔹Elbow

- 최적의 K값 찾기 (K=클러스터의 수)
- Inertia : 클러스터에 속한 샘플과 Centroid사이의 거리 제곱
- K값 증가 -> Inertia 감소
- 이를 통해 최적의 클러스터 개수를 찾는 방법
- 'K vs Inertia' 그래프에서 Elbow찾기

<br>

<br>

## ❗️Dimensionality Reduction❗️

데이터를 가장 잘 나타내는 일부 특성을 선택하여, 데이터의 크기를 줄임.

### PCA (Principal Component Analysis)

- 데이터에 있는 분산이 가장 큰 방향을 찾는 것 
- 주성분 하나를 찾으면 샘플을 투영하여 차원을 줄임 (해당 주성분 벡터 위의 점으로 표시됨)
-  주성분을 찾으면 해당 주성분에 수직이고 분산이 가장 큰 방향으로 다음 주성분을 찾으면서 이어감
- n_components = 주성분의 수
- 주성분의 수가 많을수록 데이터의 특성(즉 해당 샘플의 원래 정보)를 더 많이 담고 있으므로, Inverse할 때 원본과 비슷해짐
- 보통 첫 번째 주성분은 저주파 영역
- 첫 번째 주성분의 Explained variance가 당연히 가장 큼
- ❗️<b>즉, PCA 모델의 Component에는 주성분에 대한 정보 저장</b>
- ❗️<b>각 샘플을 PCA 모델로 Transform하면, 실제 샘플의 특성값이 아니라, 각 주성분에 대한 값이 저장됨</b>

- 주파수 도메인으로 분리시킨 것과 비슷해보임.
