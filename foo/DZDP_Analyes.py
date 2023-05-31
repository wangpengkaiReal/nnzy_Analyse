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
            Time = data['addTime'].replace('T', ' ').replace('Z', '').replace('.000', '')
            print(Time)

            # 获取评论文本
            for test in data['reviewBody']['children'][0]['children']:
                if test.get('text') is not None:
                    text_list.append(test.get('text'))
            analsyResults, emotion = tool.Results('\n'.join(text_list))
            print(analsyResults)
            print(emotion)
            exit()
            text_list.clear()
            print(text_list)
            break
        break
