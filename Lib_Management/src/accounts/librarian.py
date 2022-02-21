from src.constants import AccountStatus
from src.accounts.account import IAccount

class Librarian(IAccount):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
    
    def add_book_item(self, book_item):
        pass

    def block_member(self, member):
        pass

    def un_block_member(self, member):
        pass

