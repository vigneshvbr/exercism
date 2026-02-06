def is_armstrong_number(number):
    n = len(str(abs(number)))
    i = abs(number)
    sum = 0
    while i > 0:
        d = i % 10
        sum += d ** n
    
        i = i // 10
    return sum == abs(number)