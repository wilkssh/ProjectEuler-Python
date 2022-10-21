from configparser import NoOptionError


def multiple_sum(val):
    sum = 0
    for num in range(val):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


if __name__ == "__main__":
    print(multiple_sum(1000))