# 인코딩 한글은 cp949로 설정
from urllib.request import urlopen
from os.path import getsize
f = open('stockcode.txt', 'rt', encoding='cp949')
data = f.read()
print(data)
f.close()

###############
line_num = 1
line = f.readline()
while line:
    print('%d %s' % (line_num, line))
    line = f.readline()
    line_num += 1
f.close()

###############
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' % (line_num+1, line), end='')
f.close()

###############
spos = 105
size = 500

h = open('stockcode_part.txt', 'w')

f.seek(spos)  # 파일을 읽을 위치를 seek()으로 spos만큼 이동
data = f.read(size)
h.write(data)

h.close()
f.close()

###############

file1 = 'stockcode.txt'
file_size1 = getsize(file1)

print('file name : %s\tfile size : %d', file1, file_size1)

###############

url = 'https://www.python.org'
with urlopen(url) as f:  # with open(파일 경로, 모드) as 파일 객체:
    # 처리 코드 -> with as 구문을 빠져나가게 되면 자동으로 close() 함수를 호출하여 파일을 닫음
    doc = f.read().decode()
    print(doc)
    with open('pythonhome.html', 'w') as h:
        h.writelines(doc)

# 인터넷에 있는 이미지를 내 pc로 저장하기
imgurl = 'https://images.chosun.com/resizer/g8idcFcDZScJIs26gdWQJYtRQJM=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/JTRAZWPHTVEQWBAB2MFQ6IQYSI.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
