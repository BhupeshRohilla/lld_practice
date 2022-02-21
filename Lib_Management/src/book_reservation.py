class BookReservation:
    def __init__(self, creation_date, status, book_item_barcode, member_id) -> None:
        self.__creation_date = creation_date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    @staticmethod
    def fetch_reservation(book_item_barcode): pass