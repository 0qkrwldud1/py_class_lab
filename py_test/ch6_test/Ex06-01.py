import csv
import glob
import os

## 전역 변수부
file_list = glob.glob(os.path.join('CSV/folder/', '*.csv'))
firstYN = True

## 메인 코드부
for input_file in file_list :
    with open(input_file, "r", encoding="utf-8") as inFp :
            with open("CSV/강원인구통합-2.csv", "a", newline='', encoding="utf-8") as outFp:
                csvReader = csv.reader(inFp)
                csvWriter = csv.writer(outFp)
                header_list = next(csvReader)

                if firstYN == True :
                    csvWriter.writerow(header_list)
                    firstYN = False

                for row_list in csvReader:
                    csvWriter.writerow(row_list)

print('Save. OK~')