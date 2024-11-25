import re
import os
import random
import string


class All_About_Encryption:
    def __init__(self):
        self.text_to_encrypt: str = ""
        self.shift_value: int = -1

        self.eng_pattern = r"^[A-Za-z]+$"
        self.key: str = "LIME"
        self.encrypted_text: str = ""

    def set_text_to_encrypt(self, new_text_to_encrypt: str):
        if new_text_to_encrypt == "":
            return "Вы не ввели данные для строки!"
        if not bool(re.match(self.eng_pattern, new_text_to_encrypt)):
            return "Строка введена некорректно!"
        self.text_to_encrypt = new_text_to_encrypt

    def set_shift(self, new_shift_value):
        if not new_shift_value:
            return "Не введена величина сдвига!"
        try:
            new_shift_value = int(new_shift_value)
        except:
            return "Нужна цифровая величина сдвига!"
        self.shift_value = new_shift_value

    def set_encrypted_text(self, new_encrypted_text: str): self.encrypted_text = new_encrypted_text

    def change_text_to_encrypt(self, new_text: str):
        self.text_to_encrypt = new_text

    def change_shift_value(self, new_value: int):
        self.shift_value = new_value

    def show_text_to_encrypt(self): return self.text_to_encrypt
    def show_shift_value(self): return self.shift_value
    def show_key(self): return self.key
    def show_regex(self): return self.eng_pattern
    def show_encrypted_text(self): return self.encrypted_text


class User_Choice:
    def __init__(self):
        self.users_choice: str = ""
        self.users_choice_of_text: str = ""

    def change_choice(self, new_choice: str): self.users_choice = new_choice
    def change_text_gen_choice(self, new_choice_: str): self.users_choice_of_text = new_choice_

    def get_choice(self): return self.users_choice
    def get_text_gen_choice(self): return self.users_choice_of_text


class Main_Processes:
    def __init__(self):
        self.info: All_About_Encryption = All_About_Encryption()
        self.choice_: User_Choice = User_Choice()

    @staticmethod
    def Generate_random_string() -> str:
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for _ in range(6))
        return random_string

    @staticmethod
    def Generate_random_shift() -> int:
        shift = random.randint(0, 10)
        return shift

    @staticmethod
    def Quitting():
        exit()

    def Print_Menu(self):
        choice = input("1. Ввод строки и величины сдвига\n"
                       "2. Выполнить шифрование\n"
                       "3. Вывести результат\n"
                       "4. Завершить работу программы\n")
        self.choice_.change_choice(choice)

    def Getting_Mode(self):
        generate_choice = input("Как будем задавать параметры?\n"
                                "1. Автоматически\n"
                                "2. Вручную\n")
        self.choice_.change_text_gen_choice(generate_choice)

    def String_Work(self):
        self.info.set_encrypted_text("")
        self.Getting_Mode()

        mode: str = self.choice_.get_text_gen_choice()
        match mode:
            case "1":
                random_text_to_encrypt = self.Generate_random_string()
                random_shift_value = self.Generate_random_shift()

                self.info.change_text_to_encrypt(random_text_to_encrypt)
                self.info.change_shift_value(random_shift_value)
                input(f"Сгенерированная строка/величина сдвига: {random_text_to_encrypt}/{random_shift_value}\n"
                      f"Нажмите любую клавишу, чтобы продолжить...")
            case "2":
                new_text_to_encrypt = input("Введите вашу строку (только с англ. буквами): ")
                result_1 = self.info.set_text_to_encrypt(new_text_to_encrypt)
                if type(result_1) is str:
                    input(f"{result_1}\n"
                          f"Нажмите любую клавишу, чтобы продолжить...")
                    return

                new_shift = input("Введите величину сдвига: ")
                result_2 = self.info.set_shift(new_shift)
                if type(result_2) is str:
                    input(f"{result_2}\n"
                          f"Нажмите любую клавишу, чтобы продолжить...")
                    return

    def Encryption_Process(self):
        if self.info.show_text_to_encrypt() == "" or self.info.show_shift_value() == -1:
            input("Не хватает данных!\n"
                  "Нажмите любую клавишу, чтобы продолжить...")

        encrypted_text = ""

        my_key = self.info.show_key()
        my_text_to_encrypt = self.info.show_text_to_encrypt()
        my_shift_value = self.info.show_shift_value()
        key_length = len(my_key)

        for i, char in enumerate(my_text_to_encrypt):
            if char.isalpha():
                shift_amount = (ord(my_key[i % key_length].upper()) - ord('A') + my_shift_value) % 26
                encrypted_char = chr((ord(char.upper()) - ord('A') + shift_amount) % 26 + ord('A'))
                if char.islower():
                    encrypted_text += encrypted_char.lower()
                else:
                    encrypted_text += encrypted_char
            else:
                encrypted_text += char

        self.info.set_encrypted_text(encrypted_text)

    def Printing_A_Result(self) -> None:
        checking_results = self.info.show_encrypted_text()
        key = self.info.show_key()
        if checking_results == "":
            input("Вход в раздел запрещён.\n"
                  "Нажмите любую клавишу, чтобы продолжить...")
            return
        input(f"Зашифрованная строка: {checking_results}\n"
              f"Ключ: {key}\n"
              f"Нажмите любую клавишу, чтобы продолжить...")


if __name__ == "__main__":
    Body = Main_Processes()
    while True:
        os.system("cls")
        Body.Print_Menu()
        user_choice = Body.choice_.get_choice()
        match user_choice:
            case "1":
                Body.String_Work()
            case "2":
                Body.Encryption_Process()
            case "3":
                Body.Printing_A_Result()
            case "4":
                Body.Quitting()
