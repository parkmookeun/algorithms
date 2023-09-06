##큰 수 문제
##n,m,k = map(int,input().split())
##number = list(map(int,input().split()))
##
##number.sort()
##big1 = number[-1]
##big2 = number[-2]
##
##print(big1,big2)
##answer = 0
##i = 0
##while m > 0:
##    if i % 2 == 0:
##        if m >= k:
##            answer += big1*k
##            m -= k
##        else:
##            answer += big1*m
##            break
##    else:
##        answer += big2
##        m -= 1
##    i += 1
##    
##print(answer)


## 숫자 카드 게임
##n,m = map(int, input().split())
##smallst = []
##for i in range(n):
##    hang = list(map(int,input().split()))
##    smallst.append(min(hang))
##
##
##print(max(smallst))
##


## 1이 될때까지
n,k = map(int,input().split())
count = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

print(count)
