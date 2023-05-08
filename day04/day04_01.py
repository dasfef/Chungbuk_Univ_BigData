import numpy
import csv

f = open('../DataAnalysis/DATA/age.csv')
data = csv.reader(f)
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위) >> ')