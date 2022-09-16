# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
# DP

import sys
sys.stdin = open('2579.txt')

# DP
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
a = l[0]
b = max(l[1], l[2])
c = l[3]
d = max(l[4], l[5])
e = l[6]
# 연속된 세 개의 계단을 모두 밟아서는 안 된다.
# 각 단계를 올라갈 때마다 얻을 수 있는 최댓값을 얻어야 한다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 1 : 1
# 2 : 2+4 or 3+4
# 3 : 4
# 4 : 4+5 or 4+6
# 5 : 7
# 6 : 7+8 or 7+9
# 7 : 10
