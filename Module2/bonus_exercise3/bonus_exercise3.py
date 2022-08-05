num = 30
fibonacci = [1, 1]

for i in range(1, num):
    next_fib = fibonacci[i] + fibonacci[i - 1]
    fibonacci.append(next_fib)

print(fibonacci)
