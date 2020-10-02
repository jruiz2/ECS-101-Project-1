#code.py
#ECS 101
#Tristan Waddell, Julia Ruiz, Melissa Tang, Xinyi Wang
#Given a string, converts the string into our binary code, and prints

#Asks user for input
my_string = input("Enter a string: ")
my_ans = ""
ch = ""

#Finds the code for the given character
def findCode(ch):
    code = ""
    if ch == "a":
        code = "00010 "
    if ch == "b":
        code = "000000 "
    if ch == "c":
        code = "11011 "
    if ch == "d":
        code = "11111 "
    if ch == "e":
        code = "00001 "
    if ch == "f":
        code = "000001 "
    if ch == "g":
        code = "000010 "
    if ch == "h":
        code = "10100 "
    if ch == "i":
        code = "10000 "
    if ch == "j":
        code = "000011 "
    if ch == "k":
        code = "000100 "
    if ch == "l":
        code = "10001 "
    if ch == "m":
        code = "11010 "
    if ch == "n":
        code = "11000 "
    if ch == "o":
        code = "01010 "
    if ch == "p":
        code = "000101 "
    if ch == "q":
        code = "000110 "
    if ch == "r":
        code = "10111 "
    if ch == "s":
        code = "10101 "
    if ch == "t":
        code = "00111 "
    if ch == "u":
        code = "00110 "
    if ch == "v":
        code = "000111 "
    if ch == "w":
        code = "001000 "
    if ch == "x":
        code = "001001 "
    if ch == "y":
        code = "00000 "
    if ch == "z":
        code = "001010 "
    if ch == "A":
        code = "01011 "
    if ch == "B":
        code = "001011 "
    if ch == "C":
        code = "01111 "
    if ch == "D":
        code = "01001 "
    if ch == "E":
        code = "00110 "
    if ch == "F":
        code = "00100 "
    if ch == "G":
        code = "001101 "
    if ch == "H":
        code = "11001 "
    if ch == "I":
        code = "01101 "
    if ch == "J":
        code = "001110 "
    if ch == "K":
        code = "001111 "
    if ch == "L":
        code = "010000 "
    if ch == "M":
        code = "01100 "
    if ch == "N":
        code = "11100 "
    if ch == "O":
        code = "010001 "
    if ch == "P":
        code = "010010 "
    if ch == "Q":
        code = "010011 "
    if ch == "R":
        code = "010100 "
    if ch == "S":
        code = "01100 "
    if ch == "T":
        code = "10110 "
    if ch == "U":
        code = "010101 "
    if ch == "V":
        code = "010110 "
    if ch == "W":
        code = "10010 "
    if ch == "X":
        code = "010111 "
    if ch == "Y":
        code = "011000 "
    if ch == "Z":
        code = "011001 "
    if ch == ".":
        code = "01000 "
    if ch == ",":
        code = "011010 "
    if ch == "-":
        code = "011011 "
    if ch == "!":
        code = "011100 "
    if ch == "'":
        code = "011101 "
    if ch == '"':
        code = "011110 "
    if ch == "\n":
        code = "011111 "
    if ch == " ":
        code = "00011 "
    return code

#Loops through the given string and finds the code for each character
for i in range(0, len(my_string)):
    val = findCode(my_string[i])
    my_ans = my_ans + val

#Prints the binary code
print (my_ans)

