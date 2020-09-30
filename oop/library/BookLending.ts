export class BookLending {
    private _creationDate: Date;
    private _dueDate: Date;
    private _returnDate: Date;
    private _bookItemBarcode: string;
    private _memberId: string;


    get creationDate(): Date {
        return this._creationDate;
    }

    set creationDate(value: Date) {
        this._creationDate = value;
    }

    get dueDate(): Date {
        return this._dueDate;
    }

    set dueDate(value: Date) {
        this._dueDate = value;
    }

    get returnDate(): Date {
        return this._returnDate;
    }

    set returnDate(value: Date) {
        this._returnDate = value;
    }

    get bookItemBarcode(): string {
        return this._bookItemBarcode;
    }

    set bookItemBarcode(value: string) {
        this._bookItemBarcode = value;
    }

    get memberId(): string {
        return this._memberId;
    }

    set memberId(value: string) {
        this._memberId = value;
    }

    static lendbook(barcode: string, memberId: string) {
        //todo: add logic
        return;
    }

    static fetchLendingDetails(barcode: string): BookLending {
        //todo: add logic
        return null;
    }
}
