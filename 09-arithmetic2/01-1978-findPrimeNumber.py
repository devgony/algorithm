from math import sqrt
def prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

n = int(input())
numbers = map(int, input().split())
count = 0;
for number in numbers:
    if prime(number): count += 1
print(count)
"""소수 찾기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	92887	43906	35534	47.709%
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3"""
"""
풀이
1은 소수가 아니다
약수의 특징을 활용해 sqrt(n) 까지만 연산 수행
"""