def fibonacci_check(num):
    fib_seq = [0, 1]

    while fib_seq[-1] < num:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    if num in fib_seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
resultado = fibonacci_check(num)
print(resultado)
