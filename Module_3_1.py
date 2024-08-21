calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string)), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

test_one = string_info("capybara")
print(test_one)

test_two = string_info('armageddon')
print(test_two)

res2 = is_contains('urban', ['Hello', 'Bye', 'urban'])
print(res2)

res1 = is_contains('student', ['Hello', 'bye', 'urban'])
print(res1)
