# Author : Fransiskus Agapa
from countries import OCountry
from countries import TCountry

print("\n== Country Menu ==")
print("1. Input Data")
print("2. Display Data")
print("E. Exit")
choice = input("choice: ")

invalid = 1                             # condition to count if there is anything goes wrong / invalid
data_exist = 1                          # to see whether data has been updated or not
one_country = OCountry("NoName", "NoConstForm", "NoLanguage", 0)
one_language = False
two_country = TCountry("NoName", "NoConstForm", "NoLanguage", 0)
two_language = False

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Input Data ]\n")
        invalid  = (invalid * 0) + 1               # reset value
        name1 = input("Name of a country: ")
        if name1.isdigit():
            print("\n[ Invalid name - string only ]\n")
            invalid += 1
        else:
            name1 = name1.capitalize()

        const_form1 = input("Constitutional form: ")
        if const_form1.isdigit():
            print("\n[ Invalid input - string only ]\n")
            invalid += 1
        else:
            const_form1 = const_form1.capitalize()

        language1 = input("Language: ")
        if language1.isdigit():
            print("\n[ Invalid language = string only ]\n")
            invalid += 1
        else:
            language1 = language1.capitalize()

        try:
            print("Input amount of language/s spoken: ", end=" ")
            amount_of_language1 = int(input())
        except ValueError:
            print("\n[ Invalid input - number only ]\n")
            invalid += 1

        response_language = input("Are there more than one language spoken (y/n): ").lower()   # make user input to lower case
        if response_language == 'y':
            one_language = True
        elif response_language == 'n':
            one_language = False
        else:
            print("\n[ Invalid response ]")

        print("\n> 2nd Country")
        name2 = input("Name of a country: ")
        if name2.isdigit():
            print("\n[ Invalid name - string only ]\n")
            invalid += 1
        else:
            name2 = name2.capitalize()

        const_form2 = input("Constitutional form: ")
        if const_form2.isdigit():
            print("\n[ Invalid input - string only ]\n")
            invalid += 1
        else:
            const_form2 = const_form2.capitalize()

        language2 = input("Language: ")
        if language2.isdigit():
            print("\n[ Invalid language = string only ]\n")
            invalid += 1
        else:
            language2 = language2.capitalize()

        try:
            print("Input amount of language/s spoken: ", end=" ")
            amount_of_language2 = int(input())
        except ValueError:
            print("\n[ Invalid input - number only ]\n")
            invalid += 1

        response_language = input("Are there more than one language spoken (y/n): ").lower()  # make user input to lower case
        if response_language == 'y':
            two_language = True
        elif response_language == 'n':
            two_language = False
        else:
            print("\n[ Invalid response ]")

        invalid -= 1
        if invalid == 0:
            data_exist -= 1
            one_country = OCountry(name1, const_form1, language1, amount_of_language1)
            two_country = TCountry(name2, const_form2, language2, amount_of_language2)
            print("\n== Data Updated ==")
        else:
            print("\n== Update Failed ==")

    elif choice == '2':
        print("\n[ Display Data ]\n")
        if data_exist == 0:
            print("\n> 1st Country")
            one_country.the_name()
            one_country.the_constitutional_form()
            one_country.the_language()
            one_country.amount_language()
            if one_language:
                one_country.speak_more_than_one_language()

            print("\n> 2nd Country")
            two_country.the_name()
            two_country.the_constitutional_form()
            two_country.the_language()
            two_country.amount_language()
            if two_language:
                two_country.speak_more_than_one_language()
        else:
            print("[ No Data Update ]")
            print("\n> 1st Country ")
            print("No Name")
            print("No Constitutional Form")
            print("No Language")
            print("Unknown Amount of Language")

            print("\n> 2nd Country ")
            print("No Name")
            print("No Constitutional Form")
            print("No Language")
            print("Unknown Amount of Language")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Country Menu ==")
    print("1. Input Data")
    print("2. Display Data")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")

