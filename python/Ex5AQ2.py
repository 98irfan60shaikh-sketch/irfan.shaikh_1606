n=int(input("enter a number: "))
def is_even_odd(n):
    if n % 2 == 0:
        print(f"number is {n} and it is even")
    else:
        print(f"number is {n} and it is odd")
is_even_odd(n)