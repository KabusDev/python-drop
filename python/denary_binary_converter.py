import math
# init stuff

int_check = False # boolean for triggering recurring function that converts the denary

# welcome message to explain purpose of program

print("""This is a Denary to Binary Converter.
To use this simply enter a number and the script will convert it.""")

global user_int


def conversion(denary):
    if denary < 1:  # recursion for function, skips 0 as division by 0 makes the world implode
        return denary
    else:
        conversion(denary / 2)  # using division by 2 method for converting denary to binary
        print(math.trunc(denary % 2), end='')  # prints the binary string in a clean format

        # using the truncation feature from python maths module to not have floats from the conversion
        # would have used a list but was not sure how to do it correctly

# main loop for recurring input

while True:
    try:
        user_int = int(input("\nEnter a Denary number: "))  # new line for formatting, easy to read, int input
        int_check = True  # boolean check
    except:
        if ValueError:  # should sanitize the numbers so that they are not decimal ect
            print("No Acceptable Number Input.")
            int_check = False

    if int_check is True:  # statement to trigger conversion
        conversion(user_int)  # using definition with input to get conversion