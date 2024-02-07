while(True):
    n = str(input())
    if n == "0":
        break
    elif n == n[::-1]:
        print("yes")
    else:
        print("no")
