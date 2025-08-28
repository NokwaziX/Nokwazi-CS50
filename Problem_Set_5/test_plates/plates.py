'''
                        ********************* REQUIREMENTS **************************

#Rule1: Atleast two letters @ beginning
#Rule2: Max 6 & Minimum 2 characters
#Rule3: No numbers in the middle, only at the end
#Rule4: First number !=0
#Rule5: Letters and numbers ONLY! -  alphanumeric

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str.
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

'''


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


#THIS FUNC CHECKS IF ALL REQUIREMENTS ARE MET
def is_valid(plate):
    #Use 'not' to check if the plate does NOT follow the rule - it will return FALSE as it should

    if not plate[0:2].isalpha():        #Rule1 - if NOT 2 letters @ beginning of plate, its False
        return False

    if not 2 <= len(plate) <= 6:         #Rule2 - if plate number is NOT greater than/equal to 2 and NOT less/equal to 6, its False
        return False

    if not plate.isalnum():             #Rule5 - if plate is NOT alphanumeric, its False
        return False

    #For the digits that must be at the end

    for i in range(len(plate)):         #For the indices in the range of the length of the plate
        char = plate[i] #Go to the plate and take the symbol at index i

        if char.isdigit():
            if not plate[i:].isdigit():         #Rule3 - if that index after the letter is not a number return FALSE
                return False

            if char == '0':                 #Rule4 - another check to see if number is zero
                return False

            break
    return True #Return true if plate is opposite of the above

if __name__ == "__main__":
    main()
