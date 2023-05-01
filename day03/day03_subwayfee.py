import csv
f = open("C:\\Users\\User\Desktop\WORK\데이터분석\DATA\subwayfee.csv", encoding = "cp949")
data = csv.reader(f)
next(data)

mx = 0
rate = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4] / row[6]
    if rate > mx :
        mx = rate
print(mx)