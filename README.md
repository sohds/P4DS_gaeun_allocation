# P4DS_gaeun_allocation (Team 5)
2022-2 데이터사이언스캡스톤디자인I의 프로젝트를 2023-2 파이썬을이용한데이터사이언스 연계실습 시간에 디벨롭 시켜보았습니다.

<br>

## 팀원 소개
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/sohds">
        <img src="https://github.com/sohds/P4DS_gaeun_allocation/assets/122262388/014af6bc-d377-4187-ab38-0fd09fbcaab6" width="100px;" alt=""/>
        <br />
        <sub>오서연</sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>2022111746</sub>
        <br>
        <sub>전처리, 모델링</sub>
    </td>
    <td align="center">
      <a href="https://github.com/BEGOODDS">
        <img src="https://github.com/sohds/P4DS_gaeun_allocation/assets/122262388/e1fc3845-a1e6-445d-9472-13dc8929622e" width="100px;" alt=""/>
        <br />
        <sub>김유빈</sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>2022111729</sub>
        <br>
        <sub>전처리, 시각화</sub>
    </td>
    <td align="center">
      <a href="https://github.com/jinnypstar">
        <img src="https://github.com/sohds/P4DS_gaeun_allocation/assets/122262388/72a5c24b-f901-4759-8644-61a1fbe4cf28" width="100px;" alt=""/>
        <br />
        <sub>박서진</sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>2022111738</sub>
        <br>
        <sub>전처리, 시각화</sub>
    </td>
  </tr>
  <tr>
    </td>
  </tr>
</table>
</td>

<br>
<br>

# 주제 및 목표

## 캡스톤 주제 및 목표

### 주제

- 서울여대 총동문회 주관 카페 ‘가은’의 날짜별 및 시간별 인력 배치의 적절성

### 목표

- 가은의 **운영효율화**를 통한 **이익 극대화**
  
    - **고용인원의 효율적 배치**를 통한 인건비 절감
      
- **고객 만족도 향상**
  
    - 고객 대기시간감소 인한 만족도를 높임
 
<br>
<br>

## P4DS 주제

### 주제

- 서울여대 총동문회 주관 카페 ‘가은’의 운영 효율화를 위한 모델 설계
  
    - 카페 ‘가은’의 매출 분석
        - 메뉴 간의 연관 규칙 분석 → 인기메뉴 파악 및 세트 메뉴 제안
          
    - 날짜별 및 시간별 인력 배치의 적절성
        - 주문횟수에 영향을 주는 요인 분석

### 목표

- 가은 판매 데이터 분석을 통한 운영 이익 극대화 방안 제시


<br>
<br>

## 분석 과정

### 수집한 데이터

1. 기존 데이터
    - 2022년 3월 2일 ~ 2022년 12월 21일 날짜별 주문 데이터(i0302_sample.xls)
      
2. 추가 데이터
    - 2022년 3월 2일 ~ 2022년 12월 30일 노원구 날씨 데이터(nowon_climate_data_220302_221231.xlsx)

<br>

### 시각화

- 데이터 현황 확인을 위한 시각화 진행

1. 전체 **인기메뉴** 분석: 막대그래프 (bargraph_menu.ipynb)
    1. 시각화 배경
        - 인기메뉴 분석
            - 전체적인 메뉴 데이터의 현황을 파악하기 위해, 메뉴별 주문 횟수를 막대그래프로 시각화
    2. 시각화 활용 데이터
        - ‘merge_menu_sum.csv’ 파일 활용
    3. 시각화(png 파일)
        
        ![Untitled](https://github.com/sohds/P4DS_gaeun_allocation/blob/main/visualization/png/bargraph_menu.png)
        
        → 상위 10가지 인기메뉴 출력
        
2. **주문 데이터 분포 비교** : 박스 플롯 (boxplot_sum.ipynb)
    1. 시각화 배경
        - 모델링을 진행할 기간 설정 필요
            - 주문 데이터에는 1, 2학기 전체의 주문 데이터가 있지만 1학기의 데이터와 2학기의 데이터의 특성이 다름.
            - 2학기는 전면 대면이었던 반면, 1학기는 부분 대면이었어서 1학기의 주문 데이터를 2학기와 함께 사용하여 모델링을 진행해도 될지 의문이 듦.
        - 데이터의 전반적인 분포 확인
            - 데이터의 평균 및 이상치 확인을 위한 시각화 진행
   
    2. 시각화 활용 데이터
        - ‘dayoftheweek_add.xlsx’ 파일 활용
   
    3. 시각화(png 파일)
        
        ![boxplot_for_all.png](https://github.com/sohds/P4DS_gaeun_allocation/blob/main/visualization/png/boxplot_for_all.png)
        
        → 1, 2학기 전체에서 이상치가 발생, 
        
        1학기, 2학기의 주문 횟수를 별도로 시각화 
        
        - 1학기 박스 플롯에서만 이상치를 확인
        - 1학기의 평균이 2학기 평균보다 낮음.
        
        ⇒ 1, 2학기 전체의 주문 데이터보다 2학기의 주문 데이터로 모델링을 진행하는 것이 더 유의미하다고 판단
        
<br>


### P4DS 데이터 분석 과정

1. **FP-Growth** 을 활용한 메뉴 간의 연관 규칙 분석
    1. FP-Growth Algorithm 선정 배경
        - 대규모 데이터 셋에 맞는 알고리즘 필요
            - 우리가 사용하는 데이터는 9만 건이 넘어가는 데이터셋이기 때문에, Apriori 알고리즘보다 대규모 데이터셋에서 효율적인 FP-Growth 알고리즘을 활용
        - Candidate 문제가 생기지 않는 알고리즘 필요
            - Apriori 알고리즘이 candidate를 너무 많이 생성해 문제가 되는 것을 해결한 FP-Growth 알고리즘이 더 적합하다고 판단.
    2. FP-Growth Algorithm 개념
        
        [Association Rule Mining 개념 - WIKI에서 확인](https://github.com/sohds/P4DS_gaeun_allocation/wiki/Association-Rule-Mining)
        
    3. FP-Growth 활용 방향
        - 메뉴 데이터 간의 연관 규칙 생성
            - antecedents과 consequents의 support값, confidence값, lift값 확인
    4. 전처리 과정 (merge_menu_sum.ipynb 파일 내에서 진행)
        - ‘merged_files.xlsx’를 활용하여 시간별 각 메뉴 주문량을 나타냄
            
            → merge_menu_sum.csv
            
    5. 생성 알고리즘 코드 (fpgrowth_menu.ipynb)
        - FP-Growth Algorithm에 맞게 전처리 재진행 후 알고리즘 적용
          
    6. 결과
        1. 음료 조합
            - support값과 confidence값이 모두 높은 itemset
                - 복숭아아이스티 → 샷추가 (support: 0.889, confidence: 0.957)
                - 아메리카노 → 아이스티 (support: 0.880, confidence: 0.950)
                - 아메리카노 → 샷추가 (support: 0.860, confidence: 0.929)
            - ‘샷추가’가 포함된 칼럼이 support값과 confidence값이 매우 높음
        2. 디저트 조합
            - 디저트가 포함된 itemset 중에, support 값과 confidence값이 높은 itemset
                - 햄치즈샌드위치 → 복숭아아이스티 + 샷추가 (support: 0.465, confidence: 0.99)
                  
    7. 제안점
        1. 음료 조합
            - 아이스티 주문량에 대비하여 사전에 충분한 양의 베이스를 제조
            - 아메리카노 주문량에 대비하여 사전에 충분한 양의 물 준비
        2. 디저트 조합
            - 햄치즈샌드위치, 복숭아아스티, 샷추가
                - 부가적인 제안점 (카페 가은의 이윤 증대를 위한 제안)
                - 햄치즈샌드위치의 유통기한이 짧은 특성을 고려하여 인기 메뉴 중 하나인 아샷추를 함께 파는 것을 제안

<br>
    
2. **Linear Regression**을 활용한 주문횟수에 영향을 주는 요인 분석
    1. 개념
        
        [Linear Regression의 개념 - WIKI에서 보기](https://github.com/sohds/P4DS_gaeun_allocation/wiki/Regression)
        
    2. 활용 방향
        - 시간대별 주문횟수에 영향을 미치는 요인 분석
            - `R-squared`로 모델 적합도 확인
            - 각 feature의 가중치(coefficients)값 확인
    3. 전처리 과정 (cross_reg_2nd.ipynb)
        - One-Hot Encoding을 통해 ‘final_for_models.xlsx’ 파일 안의 categorical data를 binary data로 변환
    4. 모델링 코드 (cross_reg_2nd.ipynb)
        - Regression 모델에 맞게 전처리 후 Linear Regression 진행
    5. 결과
        - Regression 모델 적합도 확인
        
        ```
        Average R² Score: 0.745286946293847
        ```
        
        - $mean(R^2)=0.7453$으로, 괜찮은 성능을 보임.
            - 인력 예측 모델로서의 사용도 충분히 고려할 수 있을 것으로 예상
         <img src="https://github.com/sohds/P4DS_gaeun_allocation/blob/main/visualization/png/reg_feature_coef_2nd.png" width="500px;" alt=""/>
         <img src="https://github.com/sohds/P4DS_gaeun_allocation/blob/main/visualization/png/reg_pred_2nd.png" width="500px;" alt=""/>

        
        - 각 요인별 가중치 확인
            - 12시, 11시, 14시, 13시, 축제, 화요일 순으로 (+)의 영향을 끼침.
            - 16시, 17시, 15시, 금요일, 9시, 보강주 순으로 (-)의 영향을 끼침.

    6. 제안점
        - 인력 제안
            - (+) 영향을 끼치는 요인에는, 알바생을 보강하는 방향을 제안
            - (-) 영향을 끼치는 요인에는 알바생을 덜 사용하는 방향을 제안
        - 마케팅 제안
            - 알바생을 덜 사용하지 않을거면, 세트 메뉴 할인 등을 (-) 영향인 시간대(15시 이후)에 진행해서 사람들을 더 오게 만드는 전략을 택하는 방법도 좋은 마케팅 방법이 될 것으로 예상

3. Decision Tree Classification
    1. 개념
        
        [Classification](https://github.com/sohds/P4DS_gaeun_allocation/wiki/Classification)
        
    2. 활용 방향
        - 시간대별 주문횟수에 영향을 미치는 요인 분석
            - F1 Score로 모델 적합도 확인
            - 각 feature의 중요도(importance)값 확인
    3. 전처리 과정  (decisiontree_2nd.ipynb 파일 내에서 진행)
        - ‘final_for_modles.xlsx’ 안의 categorical 데이터들을 Decision Tree 모델이 이해할 수 있는 One-Hot Encoding을 통해 binary data로 변환
        - 혼잡도 전처리
            - 혼잡도 개념 설명
            
            ![histogram.jpeg](https://prod-files-secure.s3.us-west-2.amazonaws.com/bfc5abc4-9bcf-48a0-a286-bd48a263cc78/4904db52-596a-4430-b2f5-4ad2e96ea716/histogram.jpeg)
            
            - Decision Tree Classification을 위해 혼잡도 계산
                - 합계 열을 기준으로, 주문 혼잡도를 계산
                    - 혼잡: 55 이상
                    - 보통: 55 미만 25 이상
                    - 여유: 25 미만
    4. 모델링 코드 (decisiontree_2nd.ipynb)
        - Decision Tree 모델에 맞게 전처리 후 Decision Tree Classification 진행
    5. 결과
        - Decision Tree Classification 시각화 결과
        
        ![tree_visual_2nd.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/bfc5abc4-9bcf-48a0-a286-bd48a263cc78/d965d9ae-2764-4deb-b6e3-55a13fe95f77/tree_visual_2nd.png)
        
        - 각 특성들의 중요도 수치 확인
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bfc5abc4-9bcf-48a0-a286-bd48a263cc78/4a5e28e0-9b19-49ce-b7d8-cf23a6adb84c/Untitled.png)
        
        ‘3-4교시’, ‘금요일’, ‘11시’, ‘기온’ 순으로 높은 중요도를 보임.
        
    6. 개선점
        - 발생 문제
            - 노드를 나누는 기준이 처음부터 확실하지 않음을 확인 (3-4교시(12-15시)인데, 11시가 아닌 경우와 11시인 경우를 나눔)
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/bfc5abc4-9bcf-48a0-a286-bd48a263cc78/407937d6-6f8a-4f20-bdb0-18e7045e3146/Untitled.png)
            
            - Feature Importance가 긍정적(양수)으로 영향을 미치는 것인지, 부정적(음수)으로 미치는 것인지 확인할 방법이 없음 (vs. Linear Regression)
            - one-hot encoded 변수들이 Decision Tree에서 분류 지표로 쓰일 때, 기준이 너무 애매하게 쓰인다. (변수의 기준이 ≥ 0.5가 아니라, ≤ 0.5로, `**not 변수**`라는 기준으로 사용된다는 점)
        - 개선점
            - One-Hot Encoding만 가능한 줄 알고 모델링을 진행했는데, Ordinal Encoding도 가능하다는 점을 알게 되어, ‘feat_dt_2nd.ipynb’ 모델을 다시 돌려봄.
                - 기존 model/decisiontree_(학기).ipynb 파일들과 달리, **Ordinal Encoding**을 진행하고 시간의 경우 int형으로 넣어주는 시도 진행
            - Decision Tree가 지표는 좋게 나왔는데 노드 기준에 대한 부분에 아쉬웠어서 Random Forest 모델을 사용하는 등의 방법을 사용할 수 있을 것 같음.

### 마무리

- 아쉬운 점 및 추후 디벨롭
    - 변수로 중요하게 작용했던 시계열 특성에 맞춰, 시계열 분석에 맞는 모델을 사용해보는 것이 좋을 것 같음.
