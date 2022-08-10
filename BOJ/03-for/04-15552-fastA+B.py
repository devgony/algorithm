from sys import stdin

n = int(input())
r = []
for i in range(1, n+1):
    a, b = map(int, stdin.readline().split())
    r.append(a + b)
for v in r:
    print(v)
'''입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

예제 입력 1 
5
1 1
12 34
5 500
40 60
1000 1000
예제 출력 1 
2
46
505
100
2000'''