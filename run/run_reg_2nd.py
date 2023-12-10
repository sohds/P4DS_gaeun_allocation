import pickle

# 모델 불러오기
with open('model_load/reg_2nd.pkl', 'rb') as file:
    loaded_model = pickle.load(file)