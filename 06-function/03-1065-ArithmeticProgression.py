n = int(input())
c = 0
def ap(a1, n, d):
    return a1 + (n - 1) * d

for i in range(1, n + 1):
    numbers = list(map(int, str(i)))
    if len(numbers) < 3:
        c += 1
    else:
        a1 = numbers[0]
        d = numbers[1] - a1
        for index, number in enumerate(numbers): 
            if number != ap(a1, index + 1 , d):
                break
            if index == len(numbers) - 1:
                c += 1
print(c)
"""문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1 
110
예제 출력 1 
99
예제 입력 2 
1
예제 출력 2 
1
예제 입력 3 
210
예제 출력 3 
105
예제 입력 4 
1000
예제 출력 4 
144
예제 입력 5 
500
예제 출력 5 
119"""