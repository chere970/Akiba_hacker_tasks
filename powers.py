
def fun(n):
    if n>=1 and n<=20:
        for i in range(0,n):
            print(i**2)
    else:
        print("The number is out of Bound")


if __name__ == '__main__':
    n = int(input())
    fun(n)