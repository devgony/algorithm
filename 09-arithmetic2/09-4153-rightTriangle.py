while True:
    sides = [*map(int, input().split())]
    if sides == [0, 0, 0]: break;
    sides.sort()
    a, b, c = sides
    if a**2 + b**2 == c**2: print("right")
    else: print("wrong")
"""직각삼각형 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	40031	20847	18698	51.985%
문제
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

예제 입력 1 
6 8 10
25 52 60
5 12 13
0 0 0
예제 출력 1 
right
wrong
right"""
"""
풀이
sort() 는 self 를 정렬 하고 None 을 return한다
python은 array의 각 elements 한번에 비교 연산 가능하다 -> 주소가 아닌 깞을 비교한다
cases 다 받고 results 한번에 출력 하지 않아도 된다
"""