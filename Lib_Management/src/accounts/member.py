from datetime import datetime
from src.constants import AccountStatus, BookStatus, Constants, ReservationStatus
from src.accounts.account import IAccount
from src.book_reservation import BookReservation
from src.book_lending import BookLending

class Member(IAccount):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
        self.__date_of_membership = datetime.date.today()
        self.__total_books_checkedout = 0
        self.__total_fine = 0

    @property
    def total_books_checkedout(self):
        return self.__total_books_checkedout
    
    def reserve_book_item(self, book_item):
        pass

    def increment_total_books_checkedout(self):
        self.__total_books_checkedout += 1

    def get_id(self):
        return self.__id

    def checkout_book_item(self, book_item) -> bool:
        if self.total_books_checkedout >= Constants.MAX_BOOKS_ISSUES_TO_A_MEMBER:
            print('The member has already checked-out maximum number of books.')
            return False
        book_reservation = BookReservation.fetch_reservation(book_item.get_barcode())
        if book_reservation != None and book_reservation.get_memeber_id() != self.get_id():
            print('book is reserved by another member')
            return False
        elif book_reservation != None:
            book_reservation.update_status(ReservationStatus.COMPLETED)
        
        if not book_item.checkout(self.get_id()):
            return False
        book_item.update_status(BookStatus.LOANED)
        self.increment_total_books_checkedout()
        return True
    
    def get_total_fine(self):
        return self.__total_fine
    
    def do_fine_calculations(self, book_item):
        book_lending = BookLending.fetch_lending_details(book_item.get_barcode())
        due_date = book_lending.due_date
        today = datetime.date.today()
        if today > due_date:
            diff_days = (today - due_date).days
            self.__total_fine += diff_days
    
    def return_book_item(self, book_item):
        self.do_fine_calculations(book_item)
        book_reservation = BookReservation.fetch_reservation(book_item.get_barcode())
        if book_reservation:
            book_item.update_status(BookStatus.RESERVED)
            book_item.send_book_available_notification()
        else:
            book_item.update_status(BookStatus.AVAILABLE)

    def renew_book_item(self, book_item):
        pass
