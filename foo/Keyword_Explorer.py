import pandas
import wordcloud
import jieba.analyse
import pandas as pd
from tool import doris


# 数据处理,关键词提取
def explorer():
    data = doris.query(f"select updataTime,	content from nnzy_commentdata_analyes")
    df = pd.DataFrame(columns=['time', 'keyword'])
    # 处理数据,做成dataframe格式
    for i in data:
        df = df.append({
            'time': pd.to_datetime((i[0])).strftime('%Y-%m'),
            'keyword': i[1]
        }, ignore_index=True)
    nnzy_keyword = keyword(df)
    word_cloud(nnzy_keyword)


# 提取关键词
def keyword(df: pandas.DataFrame) -> list:
    nnzy_keyword = []
    # 通过jieba库的textrank方法提取每一条数据的关键词
    for key in df['keyword']:
        for i in jieba.analyse.textrank(key):
            nnzy_keyword.append(i)
    return nnzy_keyword


def word_cloud(kword: list):
    stopwords = {'还有', '有点', '没有', '不会', '小时'}  # 去掉不需要显示的词
    # 词云设置,msyh.ttc电脑本地字体,可以写成绝对路径
    wc = wordcloud.WordCloud(font_path="msyh.ttc",
                             width=1000,
                             height=700,
                             background_color='white',
                             max_words=50,
                             stopwords=stopwords
                             )
    wc.generate(' '.join(kword))  # 加载词云文本
    wc.to_file("南宁之夜关键词.png")  # 保存词云文件
