terms = int(input("How many terms? "))
n1, n2 = 0, 1

if nterms <= 0:
    print("Please enter a positive integer")ḥ
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1

