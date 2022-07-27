from markupsafe import escape

class User:
    def __init__(self, firstName, lastName, email, password, passwordrepeat, licenseplate, cardnumber, expiration, firstNameCard, lastNameCard):
        self.firstName = escape(firstName)
        self.lastName = escape(lastName)
        self.email = escape(email)
        self.password = escape(password)
        self.passwordrepeat = escape(passwordrepeat)

        self.licenseplate = escape(licenseplate)

        self.cardnumber = escape(cardnumber)
        self.expiration = escape(expiration)
        self.firstNameCard = escape(firstNameCard)
        self.lastNameCard = escape(lastNameCard)