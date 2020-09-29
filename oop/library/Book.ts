import { Author } from "./contants";

export default abstract class Book {
    private ISBN: string;
    private title: string;
    private subject: string;
    private publisher: string;
    private language: string;
    private numberOfPages: number;
    private authors: Author[];
}
