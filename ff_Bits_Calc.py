# Puts stuff at end and start
def statement_generator(text, decoration):
    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
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


# Main routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    if data_type == "integer":
        var_integer = num_check("Enter an integer: ", 0)

    # For images, ask for width and height
    # (must be integers more than / equals to 1)
    elif data_type == "image":
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)

    else:
        var_text = input("Enter some text: ")
