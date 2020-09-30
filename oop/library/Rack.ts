export default class Rack {
    private _number: number;
    private _locationIdentifier: string;


    get number(): number {
        return this._number;
    }

    set number(value: number) {
        this._number = value;
    }

    get locationIdentifier(): string {
        return this._locationIdentifier;
    }

    set locationIdentifier(value: string) {
        this._locationIdentifier = value;
    }
}
