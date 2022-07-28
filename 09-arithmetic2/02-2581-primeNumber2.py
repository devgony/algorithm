from math import sqrt
def eratosthenes_sieve(m, n):
    sieve = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(sqrt(n)+1)):
        if sieve[i]:
            j = 2
            while i * j <= n:
                sieve[i * j] = False
                j += 1
    return [i for i in range(m, n+1) if sieve[i]]

m = int(input())
n = int(input())
primes = eratosthenes_sieve(m, n)
if len(primes):
    print(f"{sum(primes)}\n{min(primes)}")
else:
    print(-1)
"""소수
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	68826	26341	22558	38.800%
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61
예제 입력 2 
64
65
예제 출력 2 
"""
"""
풀이
에라토스테네스의 체
m ~ n 의 범위 에 대해 n 개의 배열로 [0],[1] index는 False, 나머지는 True 인 sieve 생성
2부터 시작하여 해당 수의 배수들을 배열에서 False 로 전환
"""