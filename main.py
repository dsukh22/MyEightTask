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
        

class User_Choice:
    def __init__(self):
        self.users_choice: str = ""
        self.users_choice_of_text: str = ""


class Main_Processes:
    def __init__(self):
        self.info: All_About_Encryption = All_About_Encryption()
        self.choice_: User_Choice = User_Choice()

    def Print_Menu(self):
        pass

    def String_Work(self):
        pass

    def Encryption_Process(self):
        pass

    def Printing_A_Result(self) -> None:
        pass