## 함수 선언 부분 ##
def plus( v1, v2) :
     result = 0
     result = v1 + v2
     return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" % hap)


a = input("문자열입력 : " )
if   a.isdigit() :
     print("숫자")
elif a.isalnum() :
     print("글자, 숫자")
else :
     print("모르겠습니다.")   

     