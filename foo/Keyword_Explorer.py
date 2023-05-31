from datetime import datetime
import pandas as pd
from tool import doris


# 数据关键词分析
def explorer():
    data = doris.query(f"select updataTime,	content from nnzy_commentdata_analyes")
    df = pd.DataFrame(columns=['time', 'keyword'])
    # 处理数据,做成dataframe格式
    for i in data:
        df = df.append({
            'time': pd.to_datetime((i[0])).strftime('%Y-%m'),
            'keyword': i[1]
        }, ignore_index=True)

    print(df.groupby('time').groups)


def keyword():
    ...
