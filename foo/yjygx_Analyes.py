import datetime
import pandas as pd
import tool
from tool import doris


# 一键游广西,情感分析及数据库写入
def Data_Analyse(path):
    path_list = tool.eachFile(path)
    # 清空表中的数据
    doris.cursor(f'truncate table  test.nnzy_commentdata_analyes')
    usersvalues = []
    for ropen in path_list:
        json_data = tool.readFile(ropen)['data']['list']
        for data in json_data:
            # 时间戳转换成时间字符串
            data_time = data['updateTime']
            dateArray = datetime.datetime.utcfromtimestamp(int(data_time/1000))
            otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")

            # 情感分析
            analsyResults, emotion = tool.Results(data['content'])

            # 数据库写入
            doris.cursor(f"INSERT INTO test.nnzy_commentdata_analyes VALUES ('{otherStyleTime}', {data['uid']}, "
                         f"'{data['content']}', '一键游广西' , '{data['ctitle']}', '{analsyResults}', {emotion})")
            usersvalues.clear()


# 创建Dataframe对象
def Dataf():
    df = pd.DataFrame(columns=['updataTime', 'uid', 'content', 'ctitle', 'analsyResults', 'emotionScore'])
    return df


# 数据写入dataframe
def input_data(df, otherStyleTime, uid, content, ctitle, analsyResults, emotion):
    df = df.append({
        'updataTime': otherStyleTime,
        'uid': uid,
        'content': content,
        'ctitle': ctitle,
        'analsyResults': analsyResults,
        'emotionScore': emotion
    }, ignore_index=True)
    return df
