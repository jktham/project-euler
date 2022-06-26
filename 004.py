palindromes = []
for i in range(1000):
    for j in range(1000):
        k = str(i*j)
        if k == k[::-1]:
            if palindromes.count(k) == 0:
                palindromes.append(int(k))

palindromes.sort()
print(palindromes[-1])
