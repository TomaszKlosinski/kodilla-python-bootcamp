num = 30
fibonacci = []

fibonacci.append(1)
for i in range(1,num):
    print(fibonacci[i], fibonacci[i-1])
    next_fib = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(next_fib)