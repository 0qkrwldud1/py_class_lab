hap, i = 0,0

for i in range(3333, 10000) :

    if i % 1234 == 0 :
        continue
    hap += i
    
    if hap >= 100000 :
        hap -= i
        break
    
print("3333~9999의 합계(1234의 배수 제외) : %d" % hap)
