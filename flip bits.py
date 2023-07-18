#a program that would flip bits i.e
# 1 -> 0, 0 -> 1

bina = input("Enter a binary string: ")

def invert_bits(bits):
    inverted = ""
    for i in bits:
        if i == "1":
            inverted += "0"
        elif i == "0":
            inverted += "1"
        else:
            print("Binary suppose to contain either 1 or 0")
            break

    print(inverted)

invert_bits(bina)


# def flip(binary_string):

#     k = binary_string.split(" ")
#     print(k)

#     # for i in binary_string:
#     #     if i == "0":
#     #         binary_string[i] = "1"
#     #     elif i == "1":
#     #         binary_string[i] = "0"

#     print(binary_string)


# flip(bina)