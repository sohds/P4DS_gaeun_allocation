import pickle

# 모델 불러오기
with open('model_load/decision_tree_model_2nd.pkl', 'rb') as file:
    loaded_model = pickle.load(file)