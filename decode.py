# decode.py
# ECS 101
# Tristan Waddell, Julia Ruiz, Melissa Tang, Xinyi Wang
# Given binary code, converts the binary code into a string, and print

# Asks user for an input
my_string = input("Enter a bit string separated by spaces: ")
my_ans = ''

# Use if statement to find the corresponding letter for each bit string
def newCode(bits):
    code = ""
    if bits == "00010":
        code = "a"
    if bits == "000000":
        code = "b"
    if bits == "11011":
        code = "c"
    if bits == "11111":
        code = "d"
    if bits == "00001":
        code = "e"
    if bits == "000001":
        code = "f"
    if bits == "000010":
        code = "g"
    if bits == "10100":
        code = "h"
    if bits == "10000":
        code = "i"
    if bits == "000011":
        code = "j"
    if bits == "000100":
        code = "k"
    if bits == "10001":
        code = "l"
    if bits == "11010":
        code = "m"
    if bits == "11000":
        code = "n"
    if bits == "01010":
        code = "o"
    if bits == "000101":
        code = "p"
    if bits == "000110":
        code = "q"
    if bits == "10111":
        code = "r"
    if bits == "10101":
        code = "s"
    if bits == "00111":
        code = "t"
    if bits == "00110":
        code = "u"
    if bits == "000111":
        code = "v"
    if bits == "001000":
        code = "w"
    if bits == "001001":
        code = "x"
    if bits == "00000":
        code = "y"
    if bits == "001010":
        code = "z"
    if bits == "01011":
        code = "A"
    if bits == "001011":
        code = "B"
    if bits == "01111":
        code = "C"
    if bits == "01001":
        code = "D"
    if bits == "001100":
        code = "E"
    if bits == "00100":
        code = "F"
    if bits == "001101":
        code = "G"
    if bits == "11001":
        code = "H"
    if bits == "01101":
        code = "I"
    if bits == "001110":
        code = "J"
    if bits == "001111":
        code = "K"
    if bits == "010000":
        code = "L"
    if bits == "01100":
        code = "M"
    if bits == "11100":
        code = "N"
    if bits == "010001":
        code = "O"
    if bits == "010010":
        code = "P"
    if bits == "010011":
        code = "Q"
    if bits == "010100":
        code = "R"
    if bits == "01100":
        code = "S"
    if bits == "10110":
        code = "T"
    if bits == "010101":
        code = "U"
    if bits == "010101":
        code = "V"
    if bits == "10010":
        code = "W"
    if bits == "010111":
        code = "X"
    if bits == "011000":
        code = "Y"
    if bits == "011001":
        code = "Z"
    if bits == "01000":
        code = "."
    if bits == "011010":
        code = ","
    if bits == "011011":
        code = "-"
    if bits == "011100":
        code = "!"
    if bits == "011101":
        code = "'"
    if bits == "011110":
        code = '"'
    if bits == "011111":
        code = "\n"
    if bits == "00011":
        code = " "
    return code

# Splits the string into an array
my_string = my_string.split()

# A loop that passes through each individual number of the bit string and adds it to the answer
for i in range(0, len(my_string)):
    val = newCode(my_string[i])
    my_ans = my_ans + val

#Prints the string
print (my_ans)

