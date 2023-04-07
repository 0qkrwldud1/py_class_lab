ss = '파이썬은완전재미있어요!'

sslen = len(ss)
for i in range(0, sslen) :
     if i % 2 == 1 :
          continue
     print(ss[i] + '#', end = '')
