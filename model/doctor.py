class Doctor:
    def __init__(self, name: str, speciality: str, address: str, logo: str):
        self.__name = name
        self.__speciality = speciality
        self.__address = address
        self.__logo = logo 

    def get_name(self) -> str:
        return self.__name
    
    def get_speciality(self) -> str: 
        return self.__speciality 
    
    def get_address(self) -> str:
        return self.__address 
    
    def get_logo(self) -> str: 
        return self.__logo
