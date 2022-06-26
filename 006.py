sum = 0
sum_of_squares = 0
for i in range(101):
    sum += i
    sum_of_squares += i**2

print(abs(sum**2 - sum_of_squares))
