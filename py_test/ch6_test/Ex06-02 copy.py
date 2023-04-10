import csv
import struct
from tkinter import *

## 전역 변수부
inRawName = 'RAW/cat256.raw'
outRawName = 'RAW/cat256_out-2.raw'
cvsName =  'CSV/cat256-2.csv'
row, col = 256, 256

## 메인 코드부
## RAW --> CSV로 저장
rawFp = open(inRawName, 'rb')
csvFp = open(cvsName,'w', newline='')
csvWriter = csv.writer(csvFp)
csvWriter.writerow(['행', '열', '픽셀 값'])
for i in range(row) :
    for k in range(col) :
        value = int(ord(rawFp.read(1)))
        row_list = [i, k, value]
        csvWriter.writerow(row_list)
rawFp.close()
csvFp.close()

## CSV 파일을 흑백으로
csvFp = open(cvsName,'r')
csvReader = csv.reader(csvFp)
headerList = next(csvReader)
csvList = []
for cList in csvReader :
    value = int(cList[2])
    if value > 128 :
        value = 255
    else :
        value = 0
    csvList.append([cList[0], cList[1], value])

## CSV --> RAW
rawFp = open(outRawName, 'wb')
for cList in csvList :
        x, y, value = map(int , cList)
        rawFp.write(struct.pack('B', value))
rawFp.close()
print('Save. OK~')

## 함수 선언 부분 ##
def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
    paper.put(rgbString)

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# 파일 --> 메모리
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw
loadImage(cvsName)

# 메모리 --> 화면 
displayImage(inImage)

canvas.pack()
window.mainloop()


