import Book from "./Book";
import {BookStatus} from "./contants";

export default class BookItem extends Book {
    private _barcode: string;
    private _referenceOnly: boolean;
    private _status: BookStatus;

    get status(): BookStatus {
        return this._status;
    }

    set status(value: BookStatus) {
        this._status = value;
    }

    get barcode(): string {
        return this._barcode;
    }

    set barcode(value: string) {
        this._barcode = value;
    }

    get referenceOnly(): boolean {
        return this._referenceOnly;
    }

    set referenceOnly(value: boolean) {
        this._referenceOnly = value;
    }

    checkout(memberId: string): boolean {
        if (this._referenceOnly) {
            return false;
        }
        // TO ADD LOGIC

        return true;
    }

}
