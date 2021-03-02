import csv
import random
import os
 
os.chdir("/Users/suhyeonglee/output")
''' # 모아서 셔플한 기사를 태그와 제목(내용) 2가지만 남긴 csv로 저장
file = open('Article_unity.csv', 'r', encoding='utf-8')
line = file.readlines()
random.shuffle(line)
rcsv = csv.reader(line)

file_write = open('Article_shuffled.csv', 'w', encoding='utf-8', newline="")
wcsv = csv.writer(file_write)
 
for i in rcsv:
    try:
        wcsv.writerow([i[0].strip(), i[2]])
    except:
        pass
'''
#모아서 셔플한 기사를 태그와 제목(내용) 2가지만있는 txt로 변환
with open('test.csv', 'r') as inp, open('myfile.txt', 'w') as out:
    for line in inp:
        line = line.replace(',', '\t')
        out.write(line)
