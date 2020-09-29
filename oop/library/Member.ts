import Account from "./Account";
import BookItem from "./BookItem";
import {BooksConstants} from "./contants";

export default class Member extends Account {
    private dateOfMembership: Date;
    private totalBooks: number;

    getTotalBooks(): number {
        return this.totalBooks;
    }

    reserveBookItem(book: BookItem): boolean {
        //todo: add more logic
        return true;
    }
    increateTotalBooks() {
        this.totalBooks += 1;
    }

    checkoutBookItem(book: BookItem): boolean {
        if(this.getTotalBooks() >= BooksConstants.MAX_BOOKS_TO_ONE_USER) {
            return false;
        }

        // todo: add more logic
        return true;
    }
}
