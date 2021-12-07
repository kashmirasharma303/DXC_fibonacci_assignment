# Program to display the Fibonacci sequence up to n-th term
# Input Required => Integer value for length of sequence which need to be generated.


# nterms = int(input("Please enter the number of terms in Fibonacci sequence: "))


def get_fibonacci(nterms):
    # Initializing the first two terms
    t1, t2 = 0, 1
    count = 0
    fibonacci = []
    # Check if the number of terms is valid

    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return t1
    elif nterms == 1:
        fibonacci.append(str(t1))
        return(','.join(fibonacci))
    # generate fibonacci sequence
    else:

        while count < nterms:
            fibonacci.append(str(t1))
            nth = t1 + t2
            # update values
            t1 = t2
            t2 = nth
            count += 1
        return(','.join(fibonacci))


#get_fibonacci(nterms)
