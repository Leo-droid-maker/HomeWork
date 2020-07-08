def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for el in fact(5):
    print(el)

gen = fact(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# fact_5 = (((1 * 2) * 3) * 4) * 5
# print(fact_5)
