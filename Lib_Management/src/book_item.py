from src.book_lending import BookLending
from src.constants import IBook, BookStatus

class BookItem(IBook):
    def __init__(
        self, ISBN, title, authors, subject, publisher, language, barcode,
    ) -> None:
        super().__init__(ISBN, title, authors, subject, publisher, language)
        self.__barcode = barcode
        self.__status = BookStatus.AVAILABLE

    def get_barcode(self):
        return self.__barcode

    def update_status(self, status):
        self.__status = status
    
    def checkout(self, member_id) -> bool:
        if not BookLending.lend_book(self.__barcode, member_id):
            return False
        self.update_status(BookStatus.LOANED)
        return True
    
    def send_book_available_notification(self):
        pass