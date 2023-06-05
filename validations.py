import re

def validation_email(email):
    regular_expression_email = ('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+.[(a-z)]+$')
    return re.match(regular_expression_email, email) is not None

#emails = ['oscar123@gmail.com', 'paco.com', '123.com']
#for email in emails:
    #print("probando si el '{}' es valido => {}".format(email, validation_email(email)))

def validation_name(name):
     regular_expression_name = ('^[(A-Za-z)]+$')
     return re.match(regular_expression_name, name) is not None

#names = ["oscar", "2", "jesus"]
#for name in names:
    #print("probando si el name", name ,"es valido =>  ", validation_name(name))

def validation_phone(phone):
        regular_expression_phone = r'^\d+$'
        return re.match(regular_expression_phone, phone) is not None

#phones = ["31138951524", "3006015635", "pppppppppp"]
#for phone in phones:
    #print("probando si '{}' es un phone? => {}" .format(phone, validation_phone(phone)))


#try:
#        if float(phone):
#            return True
#     except:
#            return False
