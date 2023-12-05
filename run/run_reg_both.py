from joblib import load
import numpy as np

def get_user_input():
    # 사용자로부터 입력 받기
    input_values = []
    print("""
          학기, 8-17시(10개의 시간 중, 해당하는 시간에 1 처리하고 나머지는 0 처리), \n 봄~겨울(4개의 계절 중, 해당하는 계절에 1 처리하고 나머지는 0 처리), \n
             보강주, 시험, 축제, 평소(4개 중 해당하는 때 1 처리하고 나머지는 0 처리), \n 월~금(5개의 평일 중, 해당하는 요일에 1 처리하고 나머지는 0 처리) \n
             '기온(°C)', '풍속(m/s)', '강수량(mm)', '습도(%)'를 숫자로 하나씩 적어주세요.
             """)
    for i in range(28):  # 특성의 개수에 따라 조정
        value = float(input(f"Enter feature {i+1} value: "))
        input_values.append(value)
    
    return np.array(input_values).reshape(1, -1)

def main():
    # 모델 불러오기
    loaded_model = load('linear_regression_both.joblib')

    # 사용자 입력 받기
    X_new = get_user_input()

    # 예측 수행
    predictions = loaded_model.predict(X_new)

    # 결과 출력
    print("Predicted value:", predictions[0])

if __name__ == "__main__":
    main()
