num = int(input())
result = str(num)

if num >= 10000:
    result = str(num//1000) + 'k'
elif num >= 0:
    pass

print(result)
