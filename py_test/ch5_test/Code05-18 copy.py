inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("text/text.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

i = 0
while i<3 :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    #print(inStr, end = "")
    print("%d : %s" %(i+1 ,inStr), end = "")

inFp.close()
