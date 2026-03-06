def hex_output():
    decnum = 0
    hexnum = input("Enter a hex number to convert to decimal: ")
    for number, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** number)
    print(f"The decimal value of {hexnum} is {decnum}.")

if __name__ == "__main__":
    hex_output()