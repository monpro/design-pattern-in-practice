export enum BookFormat {
    HARDCOVER,
    PAPERBACK,
    EBOOK,
    NEWSPAPER
}

export enum BookStatus {
    AVAILABLE,
    RESERVED,
    LOANED,
    LOST
}

export enum ReservationStatus {
    WAITING,
    PENDING,
    CANCELED,
    NONE
}

export enum AccountStatus {
    ACTIVE,
    CLOSED,
    CANCELED,
    NONE
}


export class Address {
    private streetAddress: string;
    private city: string;
    private state: string;
    private zipCode: string;
    private country: string;
}

export class Person {
    private name: string;
    private address: Address;
    private email: string;
    private phone: string;
}

export class BooksConstants {
    static readonly MAX_BOOKS_TO_ONE_USER =10;
    static readonly MAX_LENDING_DAYS = 10;
}

export class Author extends Person {
    private title:string;
}


