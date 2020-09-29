import Book from "./Book";

export default class BookItem extends Book {
    private barcode: string;
    private referenceOnly: boolean;


    checkout(memberId: string): boolean {
        if (this.referenceOnly) {
            return false;
        }
        // TO ADD LOGIC

        return true;
    }
}
