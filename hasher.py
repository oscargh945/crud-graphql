import bcrypt

def password_incognit(password):
    password = password.encode('utf-8')
    sal = bcrypt.gensalt()
    password_hasheada = bcrypt.hashpw(password, sal)
    return password_hasheada

def password_match():
    pass

# password = "papo123"
# password2 = password.encode('utf-8')

# print(password)
# print(password2)

# if password_incognit(password):
#     print("esta es la contraseña hasheada => ", password_incognit(password))

# print("esta es la contraseña normal => ", password)

# password2 = password.encode()
# passw = password_incognit(password)

# print("comparando las contraseñas...")
# if bcrypt.checkpw(password2, passw):
#     print("Las contraseñas coinciden")
# else:
#     print("Las contraseñas NO coinciden!!!")
