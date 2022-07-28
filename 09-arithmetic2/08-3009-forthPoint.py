ps = []
for _ in range(3):
   ps.append([*map(int, input().split())])

cases = [{0, 1}, {0, 2}, {1, 2}]
distances = []
for i, c in enumerate(cases):
    c = iter(c)
    x0, y0 = ps[next(c)]
    x1, y1 = ps[next(c)]
    distances.append(((x1-x0)**2 + (y1-y0)**2, i))
diagonal_indexes = cases[max(distances)[1]]
middle_indexes = iter({0, 1, 2} - diagonal_indexes)
diagonal_indexes = iter(diagonal_indexes)
dx0, dy0 = ps[next(diagonal_indexes)]
dx1, dy1 = ps[next(diagonal_indexes)]
mx0, my0 = ps[next(middle_indexes)]
mx1 = dx1 + dx0 - mx0
my1 = dy1 + dy0 - my0
print(mx1, my1)
    
"""네 번째 점 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	24606	17677	15982	73.071%
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.

예제 입력 1 
5 5
5 7
7 5
예제 출력 1 
7 7
예제 입력 2 
30 20
10 10
10 20
예제 출력 2 
30 10"""
"""
풀이
1. 세 점으로 생긴 삼각형에 대해서 대각선을 이루는 점들 (dx0, dx1), (dx1, dy1) 과 직각을 가지는 중간점 (mx0, my0)을 구한다
2. 대각선을 이루는 점을의 중점이 같음을 이용 (dx0 + dx1) / 2 = (mx0 + mx1) / 2
하지만 "축에 평행한 직사각형 이 문제이므로" 그냥 3개 점에서 유일한 x값, y값을 출력하면 끝
문제를 잘 읽자
"""