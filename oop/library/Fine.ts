export class Fine {
    private _creationDate: Date;
    private _bookItemBarcode: number;
    private _memberId: string;


    get creationDate(): Date {
        return this._creationDate;
    }

    set creationDate(value: Date) {
        this._creationDate = value;
    }

    get bookItemBarcode(): number {
        return this._bookItemBarcode;
    }

    set bookItemBarcode(value: number) {
        this._bookItemBarcode = value;
    }

    get memberId(): string {
        return this._memberId;
    }

    set memberId(value: string) {
        this._memberId = value;
    }

    static collectFine(memberId: string, days: number) {
        return;
    }
}
