sequence = [1, 2]
while sequence[-1] + sequence[-2] < 4000000:
    sequence.append(sequence[-1] + sequence[-2])

sum = 0
for i in range(len(sequence)):
    if (sequence[i] % 2 == 0):
        sum += sequence[i]

print(sum)
