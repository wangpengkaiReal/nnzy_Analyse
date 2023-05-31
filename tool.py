import json
import os

import jieba
import pymysql
import mysql.connector
from typing import Tuple, List

from snownlp import SnowNLP


def eachFile(path):
    child = []
    pathDir = os.listdir(path)
    for allDir in pathDir:
        child.append(os.path.join('%s/%s' % (path, allDir)))
    return child


# 读取文件内容
def readFile(path):
    fopen = open(path, 'r', encoding='utf8')  # r 代表read
    json_data = json.load(fopen)
    return json_data


# 文本情感分析
def Results(content_data):
    # 对文本分词
    incise_text = jieba.cut(content_data)
    emotion = SnowNLP(" ".join(incise_text)).sentiments
    if emotion <= 0.2:
        return '不行', emotion
    elif emotion <= 0.4:
        return '不太行', emotion
    elif emotion <= 0.6:
        return '一般', emotion
    elif emotion <= 0.8:
        return '还不错', emotion
    elif emotion <= 1:
        return '超赞', emotion


# Doris数据库操作类,兼容mysql
class Doris:
    # 连接数据库和创建游标
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="124.71.112.110",
            port=9030,
            user="admin",
            passwd="lfkj123",
            db="test",
            charset="utf8",
            autocommit=True,
        )
        self.cur = self.conn.cursor()  # 生成游标对象

    # 提交SQL语句
    def cursor(self, sql: str):
        self.cur.execute(sql)

    # 查询数据库数据
    def query(self, sql: str) -> Tuple[tuple]:
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    # fixme 插入数据(未测试)
    def insertion(self, table_name, value):
        values = (table_name,) + value[0]
        self.cur.execute(f'INSERT INTO %s VALUES ({"%s," * (len(values) - 1) + "%s"})' % values)

    # fixme 批量插入数据(未测试)
    def bulk_insertion(self, table_name: str, value: List[tuple]):
        self.cur.executemany(f'insert into {table_name} values({"%s," * (len(value[0]) - 1) + "%s"})', value)

    # 关闭数据库连接
    def __del__(self):
        self.conn.close()


doris = Doris()
