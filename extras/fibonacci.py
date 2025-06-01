def solution():
    try:
        n = int(input("Digite um número inteiro: "))

        if n == 0:
            return print("0")
        if n == 1:
            return print("0 1")

        print(" 0")
        print(" 1")

        one = 0
        two = 1

        while n > 2:
            current = one + two
            one = two
            two = current
            n -= 1

            print(f" {current}")

    except ValueError:
        print("Isso não é um número inteiro válido!")


solution()


# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]

#     seq = fibonacci(n - 1)
#     seq.append(seq[-1] + seq[-2])
#     return seq


# val=fibonacci(25)

# print(val)
