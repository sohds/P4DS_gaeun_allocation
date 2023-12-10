# one-hot encoding 해준 뒤, dataframe의 열 이름 정돈을 위한 함수

# 데이터프레임의 모든 열 이름을 순회
# '_' 문자를 기준으로 문자열을 분리하고, 마지막 부분만을 새 열 이름으로 사용

def rename_columns(df):
    new_columns = {}
    for col in df.columns:
        if '_' in col:
            new_name = col.split('_')[-1]  # '_' 문자를 기준으로 분리하고 마지막 부분을 선택
            new_columns[col] = new_name
        else:
            new_columns[col] = col  # '_'가 없는 열은 그대로 유지

    df.rename(columns=new_columns, inplace=True)
    return df
