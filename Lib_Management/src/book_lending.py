class BookLending:
    def __init__(self, creation_date, due_date, book_item_barcode, member_id) -> None:
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id
        self.__return_date = None

    @staticmethod
    def lend_book(book_item_barcode, member_id): pass

    @staticmethod
    def fetch_lending_details(book_item_barcode):
        raise NotImplementedError()