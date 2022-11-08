#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#


def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you again,", name)
    return name

# first python program
if __name__ == "__main__":
    newname = main()
    print(newname, " How are you")
