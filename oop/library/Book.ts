import { Author } from "./contants";

export default abstract class Book {
    private _ISBN: string;
    private _title: string;
    private _subject: string;
    private _publisher: string;
    private _language: string;
    private _numberOfPages: number;
    private _authors: Author[];


    get ISBN(): string {
        return this._ISBN;
    }

    set ISBN(value: string) {
        this._ISBN = value;
    }

    get title(): string {
        return this._title;
    }

    set title(value: string) {
        this._title = value;
    }

    get subject(): string {
        return this._subject;
    }

    set subject(value: string) {
        this._subject = value;
    }

    get publisher(): string {
        return this._publisher;
    }

    set publisher(value: string) {
        this._publisher = value;
    }

    get language(): string {
        return this._language;
    }

    set language(value: string) {
        this._language = value;
    }

    get numberOfPages(): number {
        return this._numberOfPages;
    }

    set numberOfPages(value: number) {
        this._numberOfPages = value;
    }

    get authors(): Author[] {
        return this._authors;
    }

    set authors(value: Author[]) {
        this._authors = value;
    }
}
