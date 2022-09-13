from asyncore import write
from hashlib import sha256
import sys

class PasswordManager:

    def __decimal_byte_to_binary(self, number: int) -> str:
        num :str = ''
        while number > 0:
            num += str(number % 2)
            number = number // 2
        while len(num) < 8:
            num += '0'
        return num[::-1]

    def __decimal_byte_to_hex(self, number: int) -> str:
        num :str = ''
        letter :list = ['a', 'b', 'c', 'd', 'e', 'f']
        if number == 0:
            num += '0'
        while number > 0:
            res = number % 16
            number = number // 16
            if res < 10:
                num += str(res)
            else:
                num += letter[res - 10]
        return num[::-1]

    def __setUserAndPass(self) -> None:
        print("Set username and password (Exit: <Esc+Enter>):")
        username :str = input('Username: ')
        if ord(username[0]) == 27:
            sys.exit(1)
        password :str = input('Password: ')
        if ord(username[0]) == 27:
            sys.exit(1)
        adm_file = open('adm.txt', 'w')
        hexpass_str :str = ''
        for i in sha256(password.encode()).digest():
            hexpass_str += self.__decimal_byte_to_hex(i)
        adm_file.write(username + ' ' + hexpass_str)

    def __access(self):
        is_running = True
        password_file = open('passwords.txt', 'r+')
        splited_file = password_file.read().split()
        password_file.truncate()
        password_file.close()
        while is_running:
            input_text = input('PM > ')
            if input_text == 'exit':
                is_running = False
            elif input_text == 'add':
                username :str = input('Username: ')
                if ord(username[0]) == 27:
                    break
                if username in splited_file:
                    raise Exception('Username already used')
                password :str = input('Password: ')
                if ord(password[0]) == 27:
                    break
                splited_file.append(username)
                splited_file.append(password)
            elif input_text == 'list':
                print('Username | Password')
                for i in range(len(splited_file)):
                    text :str = splited_file[i]
                    if i % 2 == 0:
                        text += ' | '
                    else:
                        text += '\n'
                    print(text, end='')
        password_file = open('passwords.txt', 'r+')
        for i in range(len(splited_file)):
            text :str = splited_file[i]
            if i % 2 == 0:
                text += ' '
            else:
                text += '\n'
            password_file.write(text)
        password_file.close()

    def start(self) -> None:
        adm_file = open('adm.txt', 'w+')
        pass_file_str :str = adm_file.read()
        adm_file.close()
        if len(pass_file_str) == 0:
            password_file = open('passwords.txt', 'w')
            password_file.close()
            self.__setUserAndPass()
            
        print("Log in (Exit: <Esc+Enter>):")
        adm_file = open('adm.txt')
        pass_file_str = adm_file.readline()
        splited_file = pass_file_str.split()
        while True:
            username :str = input('Username: ')
            if len(username) == 0:
                raise Exception("Invalid input")
            if ord(username[0]) == 27:
                sys.exit(1)
            password :str = input('Password: ')
            if ord(password[0]) == 27:
                sys.exit(1)
            if len(password) == 0:
                raise Exception("Invalid input")
            if splited_file[0] == username:
                binpass_str :str = ''
                for i in sha256(password.encode()).digest():
                    binpass_str += self.__decimal_byte_to_hex(i)
                if binpass_str == splited_file[1]:
                    self.__access()
                    sys.exit(0)


if __name__ == '__main__':
    pm = PasswordManager()