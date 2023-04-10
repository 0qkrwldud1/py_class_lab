with open("CSV/singer1.csv", "r", encoding="utf-8") as inFp :

    inStr = inFp.readline()
    print(inStr, end = "")

    inStr = inFp.readline()
    print(inStr, end = "")
