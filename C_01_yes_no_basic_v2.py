
# functions go here

def yes_no(question):
    """Checks users enter yes / no"""

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if  response == "yes" or  response =="y" :
            return "yes"
        elif  response == "no" or  response =="n" :
            return "no"
        else:
            print("please enter yes / no")


# Main routine
want_instructions = yes_no("Do you want instructions? ")
print(f"you chose {want_instructions}")

print("we done")