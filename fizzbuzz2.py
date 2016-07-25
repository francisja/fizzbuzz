while True:
    try:
        num = int(input("Fizz Buzz counting to what number?"))
        for n in range (1, num + 1):
            if n % 3 == 0 and n % 5 == 0:
                print("FizzBuzz")
            elif n % 3 == 0:
                print("fizz")
            elif n % 5 == 0:
                print("buzz")
            else:
                print(n)
        break
    except ValueError:
        print("I need an actual number!")