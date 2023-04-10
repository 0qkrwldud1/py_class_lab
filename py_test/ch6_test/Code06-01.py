#inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")
inFp = open("CSV/singer1.csv", "r", encoding="utf-8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()