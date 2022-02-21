from src.constants import IAddress

class Address(IAddress):
    def get_address(self) -> str:
        return f"{self.__line_1}, {self.__line_2}, {self.__city}, {self.__state}, PINCODE: {self.__pincode}"
