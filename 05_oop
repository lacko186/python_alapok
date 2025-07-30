class Login:
    def __init__(self, username, email, password):
        self.username = username
        self.password = password

class Registration:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

felhasznalok = []


def bejelentkezes():
        username = input('Felhasználónév: ')
        password = input('Jelszó: ')
        for user in felhasznalok:
            if user.username == username and user.password == password:
                print(f'Sikeres bejelentkezés, üdvözöllek {user.username}!')
                return
        print('Hibás felhasználónév vagy jelszó!')

def regisztracio():
        username = input('Felhasználónév: ')
        email = input('Email: ')
        password = input('Jelszó: ')
        new_user = Registration(username, email, password)
        felhasznalok.append(new_user)
        print(f'Sikeres regisztráció, üdvözöllek {new_user.username}!')
        return
    
belepes = int(input('1. Bejelentkezés || 2. Regisztráció : '))

if belepes == 1:
    bejelentkezes()
elif belepes == 2:
    regisztracio()





felhasznalok = []




