def solution(number):
    sum_number = int(sum(n for n in range (number) if n % 3 == 0 or n % 5 == 0))
    return (sum_number)