def test(number):
    one = number // 10
    two = one % 100
    return two

one = 1234
two = 5678

result = (test(one) + test(two))

print(result)


