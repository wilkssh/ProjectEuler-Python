if __name__ == "__main__":
    a = 3
    b = 2
    c = 1

    while c < 1000:
        while b < 1000:            
            while a < 1000:
                print(f'A {a} B {b} C {c}')
                ##print(f'{a} {b} {c}')
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    print(f'HERE {a} {b} {c}')
                a += 1
            b += 1
        c += 1