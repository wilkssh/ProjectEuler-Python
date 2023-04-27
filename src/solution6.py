if __name__ == "__main__":
    sum = 0
    square = 0
    for num in range(1,101):
        sum += num * num
        square += num
    square *= square
    print(sum-square)