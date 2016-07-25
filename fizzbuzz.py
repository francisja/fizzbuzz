print("Fizz Buzz counting to 100")
for n in range (1, 100):
    if n % 3 == 0 and n % 5 == 0:
       print("Fizz Buzz")
    elif n % 3 == 0:
       print("fizz")
    elif n % 5 == 0:
       print("buzz")
    elif n % 3 != 0 and n % 5 != 0:
       print(n)
    