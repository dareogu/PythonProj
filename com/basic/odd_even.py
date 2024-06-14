# a = 1
# while a < 17:
#     if (a % 2 == 0):
#         print(a, "this is even")
#     else:
#         print(a, "this is odd")
#     a += 1

numberList = [12, 25, 30, 0, 79, 812, 84, 55, 6]
even = []
odd = []
while len(numberList) > 0:
    number = numberList.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
pass
print("evenList", even)
print("oddList", odd)
