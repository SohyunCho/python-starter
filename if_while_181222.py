# a = int(input())
# if (a < 3):
#     print("a는 3보다 작다")
# elif (a >= 3):
#     print("a는 3 이상이다")
# while -> 조건문이 false 가 될때까지 intent된 애들을 계속 실행시킨다
# 증감식
# ++ prefix/postfix
# ++a (연산자 우선순위 - 0순위) / a++ 얘는 좀 뒷순위 13? (python에선 안 먹힘..)
# --


# a = int(input())
# while (a < 10):
#     print(a)
#     a += 1

# a = int(input())
# while (a < 10):
#     print(a)
#     continue  # 이게 있으면 여기까지의 액션이 무한 반복됨
#     a += 1

# a = int(input())
# while (a < 20):
#     print(a)
#     break


# 소현님꺼
# a = int(input())
# while (20 > a >= 11):
#     print(a)
#     a += 1

# 기호님꺼
# a = int(input())
# while (a < 20):
#     if (a <= 10):
#         break
#     print(a)
#     a += 1


well = int(input())
upForDay = int(input())
down = int(input())
days = 1
totalUp = 0

while (totalUp <= well):
    totalUp += upForDay  # totalUp = totalUp + upForDay
    if (totalUp >= well):
        break
    days += 1
    totalUp -= down  # totalUp = totalUp - down
print("우물을 탈출하는데 걸리는 일 수 : %d" % days)
