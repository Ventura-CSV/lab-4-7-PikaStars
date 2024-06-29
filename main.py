def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    prev = int(input("Enter a number:"))
    while True:
        num = int(input("Enter a number:"))
        if num > prev:
            break
        else:
            prev = num
            continue
            
    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
