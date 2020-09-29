import Account from "./Account";
import BookItem from "./BookItem";
import Member from "./Member";

export default class Librarian extends Account{
    addBookItem(book: BookItem): boolean {
        // todo: add logic
        return true
    }

    blockItem(member: Member): boolean {
        // todo: add logic
        return true;
    }

    unBlockMember(member: Member): boolean {
        // todo: add logic
        return true;
    }
}
