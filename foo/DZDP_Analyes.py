import datetime
import pandas as pd
import tool
from tool import doris
from snownlp import SnowNLP


def DZDP_Analyes(path):
    text_list = []
    path_list = tool.eachFile(path)
    for ropen in path_list:
        json_data = tool.readFile(ropen)['reviewInfo']['reviewListInfo']['reviewList']
        for data in json_data:
            # 评论时间
            time = data['addTime'].replace('T', ' ').replace('Z', '').replace('.000', '')

            # 用户ID
            user_id = data['userId']

            # 获取评论文本,及文本情感分析
            for test in data['reviewBody']['children'][0]['children']:
                if test.get('text') is not None:
                    text_list.append(test.get('text'))
            analsyResults, emotion = tool.Results('\n'.join(text_list))

            # 数据库插入
            text = '\n'.join(text_list)
            doris.cursor(f"INSERT INTO test.nnzy_commentdata_analyes VALUES ('{time}', '{user_id}', '{text}', '大众点评', "
                         f"'南宁之夜', '{analsyResults}', '{emotion}')")
            text_list.clear()
