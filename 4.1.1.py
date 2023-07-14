def palindrome(a):
    count = 0
    for i in range(len(a)):
        if a[i] != a[-i-1]:
            print("FALSE")
            break
        else:
            count +=1
    if count == len(a):
        print("TRUE")

munja = input()
munja = munja.lower()
munja = munja.replace(' ','')
palindrome(munja)


