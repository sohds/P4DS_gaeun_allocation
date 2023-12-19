# regression에서 활용될 데이터의
# one-hot encoding 해주기 전, 


# 각 함수는 데이터프레임의 특정 열을 받아 해당 매핑을 적용하고 변환된 열을 반환

# df라는 데이터프레임과 변환하고자 하는 열의 이름을 매개변수로 받음
# 그 후, 해당 열을 매핑 딕셔너리를 사용하여 변환하고, 변환된 열을 데이터프레임에 다시 할당하는 구조


def map_season(df, column_name):
    season_mapping = {
        '0': '봄',
        '1': '여름',
        '10': '가을',
        '11': '겨울'
    }
    df[column_name] = df[column_name].astype(str).replace(season_mapping)
    return df


def map_event(df, column_name):
    event_mapping = {
        '0' : '평소',
        '1' : '축제',
        '2' : '시험',
        '3' : '보강주'
    }
    df[column_name] = df[column_name].astype(str).replace(event_mapping)
    return df


def map_day(df, column_name):
    day_mapping = {
        '0' : '월요일',
        '1' : '화요일',
        '2' : '수요일',
        '3' : '목요일',
        '4' : '금요일'
    }
    df[column_name] = df[column_name].astype(str).replace(day_mapping)
    return df


def map_hour(df, column_name):
    hour_mapping = {
        '8' : '8시',
        '9' : '9시',
        '10' : '10시',
        '11' : '11시',
        '12' : '12시',
        '13' : '13시',
        '14' : '14시',
        '15' : '15시',
        '16' : '16시',
        '17' : '17시'
    }
    df[column_name] = df[column_name].astype(str).replace(hour_mapping)
    return df

def map_hour_int(df, column_name):
    hour_mapping = {
        '8' : 8,
        '9' : 9,
        '10' : 10,
        '11' : 11,
        '12' : 12,
        '13' : 13,
        '14' : 14,
        '15' : 15,
        '16' : 16,
        '17' : 17
    }
    df[column_name] = df[column_name].astype(str).replace(hour_mapping)
    return df


def categorize_hour(hour):
    if hour in [8, 9, 10, 11]:
        return '1-2교시'
    elif hour in [12, 13, 14]:
        return '3-4교시'
    elif hour in [15, 16, 17]:
        return '5-6교시'
    else:
        return None