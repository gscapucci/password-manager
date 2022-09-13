from hashlib import sha256
class PasswordManager:

    def decimal_byte_to_binary(self, number: int) -> str:
        num :str = ''
        while number > 0:
            num += str(number % 2)
            number = number // 2
        while len(num) < 8:
            num += '0'
        return num[::-1]

    def decimal_byte_to_hex(self, number: int) -> str:
        num :str = ''
        letter :list = ['a', 'b', 'c', 'd', 'e', 'f']
        while number > 0:
            res = number % 16
            if number < 10:
                num += str(res)
            else:
                num += letter[res - 10]
        return num[::-1]

    def setUserAndPass(self) -> None:
        print("Set username and password:")
        username :str = input('Username: ')
        password :str = input('Password: ')
        adm_file = open('adm.txt', 'w')
        binpass_str :str = ''
        for i in sha256(password.encode()).digest():
            binpass_str += self.decimal_byte_to_binary(i)
        adm_file.write(username + ' ' + binpass_str)

    def access(self):
        is_running = True
        while is_running:
            input_text = input('PM > ')
            if input_text == 'exit':
                is_running = False

    def start(self) -> None:
        adm_file = open('adm.txt')
        pass_file_str :str = adm_file.read()
        adm_file.close()
        if len(pass_file_str) == 0:
            self.setUserAndPass()
            
        print("Log in:")
        adm_file = open('adm.txt')
        pass_file_str = adm_file.readline()
        splited_file = pass_file_str.split()
        username :str = input('Username: ')
        password :str = input('Password: ')
        if splited_file[0] == username:
            binpass_str :str = ''
            for i in sha256(password.encode()).digest():
                binpass_str += self.decimal_byte_to_binary(i)
            if binpass_str == splited_file[1]:
                self.access()



if __name__ == '__main__':
    pm = PasswordManager()
    print(pm.decimal_byte_to_hex(0))
    print(pm.decimal_byte_to_hex(1))
    print(pm.decimal_byte_to_hex(2))
    print(pm.decimal_byte_to_hex(3))
    print(pm.decimal_byte_to_hex(4))
    print(pm.decimal_byte_to_hex(5))
    print(pm.decimal_byte_to_hex(6))
    print(pm.decimal_byte_to_hex(7))
    print(pm.decimal_byte_to_hex(8))
    print(pm.decimal_byte_to_hex(9))
    print(pm.decimal_byte_to_hex(10))
    print(pm.decimal_byte_to_hex(11))
    print(pm.decimal_byte_to_hex(12))
    print(pm.decimal_byte_to_hex(13))
    print(pm.decimal_byte_to_hex(14))
    print(pm.decimal_byte_to_hex(15))
    print(pm.decimal_byte_to_hex(16))
    print(pm.decimal_byte_to_hex(17))