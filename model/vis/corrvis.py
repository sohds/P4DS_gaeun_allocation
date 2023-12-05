# heatmap 으로 시각화

import matplotlib.pyplot as plt
import seaborn as sns

def corr_heatmap(corr, cols) :
    
    fig = plt.figure(figsize = (12, 10))
    ax = fig.gca()
          
    plt.rcParams['font.family'] = 'Malgun Gothic'     # 한국어 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False        # 마이너스 깨짐 방지

    # sns.set(font_scale = 1.5)  # heatmap 안의 font-size 설정
    heatmap = sns.heatmap(corr.values, annot = True, fmt='.2f', 
                        yticklabels = cols, xticklabels = cols, ax=ax, cmap = "RdYlBu") # annot_kws={'size': 15},
    
    plt.tight_layout() ## 여백을 조정
    plt.show()