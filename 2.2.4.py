result = a = 0

while 1:
    a = int(input("정수입력:"))
    if a < 0:
        break
    result += a
print(result)
