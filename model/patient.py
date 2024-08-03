class Patient:
    def __init__(self, name: str, age: str, gender: str):
        super().__init__()
        self.__name = name 
        self.__age = age 
        self.__gender = gender

    def get_name(self) -> str: 
        return self.__name
    
    def get_age(self) -> str:
        return self.__age 
    
    def get_gender(self) -> str:
        return self.__gender