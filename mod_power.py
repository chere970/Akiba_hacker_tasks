# Enter your code here. Read input from STDIN. Print output to STDOUT

def pow(a,b,c):
    power= a**b
    mod=power%2
    print(power)
    print(mod)
    
if __name__=='__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    pow(a,b,c)