def numbers(n):
    result = ""

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j <= 20:
                sum_pair = i + j

                if n % sum_pair == 0:
                    result += str(i) + str(j)

    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    anw = numbers(n)
    print(f"Ответ: {anw}")
else:
    print("Число должно быть от 3 до 20.")