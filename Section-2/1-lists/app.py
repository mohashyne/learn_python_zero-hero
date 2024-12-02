letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]


zeros = [0] * 5  # 0, 0, 0, 0, 0
print(zeros)

zeros_ones = [[[0] * 5, [1] * 4], [[2] * 4, [3] * 3]]

print(zeros_ones)


# combine
combined = "This variables are combined:", zeros + letters
# ('This variables are combined:', [0, 0, 0, 0, 0, 'a', 'b', 'c'])
print(combined)

# Range
numbers = list(range(0, 20))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers)

greetings = list("Hello World")
print(len(greetings))  # 11
print(greetings[3])  # l

for letters in greetings:
    if letters == "g":
        print(f"I found letter {letters} in {greetings}")
    else: "not found"
