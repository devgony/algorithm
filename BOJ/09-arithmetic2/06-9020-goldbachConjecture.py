from math import sqrt, ceil
def eratosthenes_sieve(m, n):
    sieve = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(sqrt(n)+1)):
        if sieve[i]:
            j = 2
            while i * j <= n:
                sieve[i * j] = False
                j += 1
    return [i for i in range(m, n+1) if sieve[i]], sieve

def find_min_diff(tuples):
    v, i = min([(abs(b-a), i) for i, (a, b) in enumerate(tuples)])
    return tuples[i]

t = int(input())
ns = []
for _ in range(t):
    ns.append(int(input()))
primes, sieve = eratosthenes_sieve(0, max(ns))
for n in ns:
    partitions = []
    for p in primes:
        if sieve[n - p]: partitions.append((p, n - p))
    a, b= find_min_diff(partitions)
    print(a, b)
"""골드바흐의 추측 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	44501	18694	14507	41.038%
문제
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

제한
4 ≤ n ≤ 10,000
예제 입력 1 
3
8
10
16
예제 출력 1 
3 5
5 5
5 11"""
"""
풀이
1. 시간초과
    n-p 가 prime 인지 판별할 때마다 primes를 순회하는게 아니라
    미리 sieve를 받아서 index로 접근해야 함 n^2 => n
2. 오답
    primes의 절반은 n/2가 아니다
    n/2를 해도 n이므로 괜히 n을 줄이지 말고 n^2을 줄이는 방법을 찾자
3. sort 불필요
    tuple(1, 2)에 대한 sort는 order by 1, 2 와 같으므로 처음 찾은 p, n-p 즉 asc순으로 이미 정렬이 되어있다.
"""