import Account from "./Account";
import BookItem from "./BookItem";
import {BooksConstants, BookStatus} from "./contants";
import {BookReservation} from "./BookReservation";
import {BookLending} from "./BookLending";
import {Fine} from "./Fine";

export default class Member extends Account {
    private _dateOfMembership: Date;
    private _totalBooks: number;


    get dateOfMembership(): Date {
        return this._dateOfMembership;
    }

    set dateOfMembership(value: Date) {
        this._dateOfMembership = value;
    }

    get totalBooks(): number {
        return this._totalBooks;
    }

    set totalBooks(value: number) {
        this._totalBooks = value;
    }

    getTotalBooks(): number {
        return this._totalBooks;
    }

    reserveBookItem(book: BookItem): boolean {
        //todo: add more logic
        return true;
    }
    increateTotalBooks() {
        this._totalBooks += 1;
    }

    checkoutBookItem(book: BookItem): boolean {
        if(this.getTotalBooks() >= BooksConstants.MAX_BOOKS_TO_ONE_USER) {
            return false;
        }

        // todo: add more logic
        return true;
    }

    returnBookItem(bookItem: BookItem) {
        const bookReservation = BookReservation.fetchReservationDetails(bookItem.barcode)
        if (bookReservation !== null) {
            bookItem.status = BookStatus.RESERVED
        }
        bookItem.status = BookStatus.AVAILABLE
    }

    checkForFine(bookItemBarcode: string) {
        const bookLending = BookLending.fetchLendingDetails(bookItemBarcode)
        const dueDate = bookLending.dueDate;
        const today = new Date();
        if(today > dueDate) {
            const diff = today.getDay() - dueDate.getDay()
            Fine.collectFine(this.id, diff);
        }
    }
}
