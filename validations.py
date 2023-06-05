import re

def validation_email(email):
    regular_expression_email = ('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+.[(a-z)]+$')
    return re.match(regular_expression_email, email) is not None

def validation_name(name):
     regular_expression_name = ('^[(A-Za-z)]+$')
     return re.match(regular_expression_name, name) is not None

def validation_phone(phone):
        regular_expression_phone = r'^\d+$'
        return re.match(regular_expression_phone, phone) is not None
