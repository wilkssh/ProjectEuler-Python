def even_fibonacci (ceiling):
    f1 = 1
    f2 = 2
    fnext = 0
    sum = 2

    while fnext < ceiling:
        fnext = f1 + f2
        f1 = f2
        f2 = fnext

        if fnext % 2 == 0:
            sum += fnext

    return sum

if __name__ == "__main__":
    print(even_fibonacci(4000000))