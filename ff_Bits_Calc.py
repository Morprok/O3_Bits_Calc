# Puts stuff at end and start
def statement_generator(text, decoration):
    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Test
# displays instructions / information
def instruction():
    statement_generator("Instruction / information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie:24 bits per pixel). For text, "
          "we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as any calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    return ""


# checks user choice is 'integer', 'tex' or 'image'
def user_choice():
    # Lists of valid responses

    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture" "pic"]

    # asking if text / inger / image
    # loop to allow multiple calculations per session
    valid = False
    while not valid:

        # asking for Text
        response = input("file type (integer / text / image): ").lower()

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            print("Please choose a valid file type!")
            print()


# checks input is a number more than  given value
def num_check(question, low):
    valid = False
    while not valid:

        error = f'PLease enter a integer that is more than ' \
                f'(or equal to) {low}'

        try:

            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


# TEST
# calculates the # of bits for text (# of characters x 8)
def text_bits():
    print()
    # ask user for string . . .
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    print()
    print(f"\'{var_text}\' has {var_length} characters . . . ")
    print(f"# of bits is {var_length} x 8 . . . ")
    print(f"We need {num_bits} bits to represent {var_text}")
    print()

    return ""


# TEST
# calculates amount of bits in image
def image_bits():
    # get width and height . . .
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print(f"# of pixels = {image_height} x {image_width} = {num_pixels}")
    print(f"# bits = {num_pixels} x 24 = {num_bits}")
    print()

    return ""


# TEST
# converts decimal to binary and states how
def int_bits():
    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print(f"{var_integer} in binary is {var_binary}")
    print(f"# of bits is {num_bits}")

    return ""


# Main routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instruction()

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    if data_type == "integer":
        int_bits()

    # For images, ask for width and height
    # (must be integers more than / equals to 1)
    elif data_type == "image":
        image_bits()

    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()
