def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    # Make name uppercase
    names = fullname.upper()
    # Separate into different words
    names = names.split()
    initials = ""
    for name in names:
        initials += name[0]
    return initials

def main():
    names_list = ["Ozzie Smith", "Bonnie blair","George","Daniel Day Lewis","adam von hall",]
    for name in names_list:
        print("The initials of", name, "are", get_initials(name))


if __name__ == "__main__":
    main()