class Countries:

    def english_speaking_country(self):
        print(" This country speaks english")

    def speak_more_than_one_language(self):
        print("This country speaks more than one language")


class OCountry(Countries):

    def __init__(self, name, constitutional_form, language, amount_language_spoken):
        self.name = name  # instance variable
        self.const_form = constitutional_form
        self.language = language
        self.amount_language_spoken = amount_language_spoken

    def the_name(self):
        print("This country is " + self.name)

    def the_constitutional_form(self):
        print("The constitutional form of " + self.name + " is " + self.const_form)

    def the_language(self):
        print("The language that is spoken is " + self.language)

    def amount_language(self):
        print("The country speak about " + str(self.amount_language_spoken) + " language/s")


class TCountry(Countries):

    def __init__(self, name, constitutional_form, language, amount_language_spoken):
        self.name = name
        self.const_form = constitutional_form
        self.language = language
        self.amount_language_spoken = amount_language_spoken

    def the_name(self):
        print("This country is " + self.name)

    def the_constitutional_form(self):
        print("The constitutional form of " + self.name + " is " + self.const_form)

    def the_language(self):
        print("The language that is spoken is " + self.language)

    def amount_language(self):
        print("The country speak about " + str(self.amount_language_spoken) + " language/s")
