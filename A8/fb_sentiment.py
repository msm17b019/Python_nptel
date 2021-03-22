import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file='C:\\Users\\sujee\\Downloads\\fb_data.xls'
xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_names[0])
dfs=list(dfs['Timeline'])
print(dfs)


