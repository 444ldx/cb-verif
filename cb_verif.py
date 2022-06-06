class CreditCardVerification():
    def __init__(self, card_number:str):
        self.card_number = card_number.replace(' ', '')
        self.issuing_industry = {'1': 'Compagnies aériennes',
                                 '2': 'Compagnies aériennes',
                                 '3': 'Organismes de voyages ou de loisirs',
                                 '4': 'Etablissements bancaires et financiers',
                                 '5': 'Etablissements bancaires et financiers',
                                 '6': 'Merchandising',
                                 '7': 'Pétrole',
                                 '8': 'Télécommunications',
                                 '9': 'Supports nationaux'}
        self.issuing_institution = {'40': 'Visa',
                                    '41': 'Visa',
                                    '42': 'Visa',
                                    '43': 'Visa',
                                    '44': 'Visa',
                                    '45': 'Visa',
                                    '46': 'Visa',
                                    '47': 'Visa',
                                    '48': 'Visa',
                                    '49': 'Visa',  
                                    '34': 'American Express',
                                    '37': 'American Express',
                                    '51': 'Mastercard',
                                    '55': 'Mastercard'}
    
    def format_check(self):
        """Checks that the card number is equal to 16 digits

        Returns:
            bool: The number is equal to 16 digits
        """
        return True if len(self.card_number) == 16 else False
        
    def get_validity(self):
        """Checks the validity of the card number using Luhn's algorithm

        Returns:
            bool: Card validity
        """
        nDigits = len(self.card_number)
        nSum = 0
        isSecond = False
        
        for i in range(nDigits - 1, -1, -1):
            d = ord(self.card_number[i]) - ord('0')
        
            if (isSecond == True):
                d = d * 2
    
            nSum += d // 10
            nSum += d % 10
    
            isSecond = not isSecond
        
        return True if nSum % 10 == 0 else False
    
    def get_industry(self):
        """Returns the name of the card issuing industry

        Returns:
            str: Card issuing industry
        """
        return self.issuing_industry[self.card_number[0]]
    
    def get_institution(self):
        """Returns the name of the card issuing institution

        Returns:
            str: Card issuing institution
        """
        return self.issuing_institution[self.card_number[0] + self.card_number[1]]

    def get_number_formatting(self):
        """Returns the card number formatted by block of 4 digits

        Returns:
            str: Card number formatted
        """
        card_number_formatting = str()
        for i in range(1, len(self.card_number) + 1):
            card_number_formatting = card_number_formatting + self.card_number[i - 1]
            if i % 4 == 0 and i != 16:
                card_number_formatting = card_number_formatting + ' '
        return card_number_formatting

    def get_informations(self):
        """Returns all map information

        Returns:
            dict: Card number, vilidity, industry and institution
        """
        if self.format_check():
            if self.get_validity():
                return {'card_number': self.get_number_formatting(),
                        'valid': True,
                        'industry': self.get_industry(),
                        'institution': self.get_institution()}
        return {'card_number': self.card_number,
                'valid': False}

class Messages():
    def __init__(self, args:dict={'err': True}):
        self.args = args

    def card_valid_message(self):
        return f"Validité : Valide\nIndustrie : {self.args['industry']}\nInstitution : {self.args['institution']}"
    
    def card_not_valid_message(self):
        return f"Validité : Non valide"
    
    def card_error_message(self):
        return f"Le numéro de CB est trop court !"
    
print('£247 CARD VERIF')
while True:
    print(' ')
    card_number = input("Numéro de CB : ")
    if len(card_number) > 0:
        verification = CreditCardVerification(card_number).get_informations()
        if verification['valid']:
            print(Messages(verification).card_valid_message())
        else:
            print(Messages(verification).card_not_valid_message())
    else:
        print(Messages(verification).card_error_message())