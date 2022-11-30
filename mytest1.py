import traceback
#global d_age, h_age


def calculator():

    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years

        if d_age < 0:
            print("Dog's age cannot be a negative number")
        elif d_age > 0:
            human_age=dog_to_human_age(d_age)
            print(type(human_age))
            human_age = float(human_age)
            human_age = round(human_age, 3)

            print("The given dog age {} is {} in human years".format(d_age, human_age))

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())


def dog_to_human_age(d_age):
    d_age=float(d_age)
    if d_age == 1:
        h_age = 1*15
    elif d_age == 2:
        h_age = 2*12
    elif d_age == 3:
        h_age = 3*9.3
    elif d_age == 4:
        h_age = 4*8
    elif d_age == 5:
        h_age = 5*7.2
    else:
        h_age= d_age*8
    return h_age
calculator() # This line calls the calculator function
