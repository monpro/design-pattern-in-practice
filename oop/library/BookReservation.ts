import {ReservationStatus} from "./contants";

export class BookReservation {
    private creationDate: Date;
    private status: ReservationStatus;
    private bookItemBarcode: string;
    private memberId: string;

    static fetchReservationDetails(barcode: string): BookReservation {
        //todo add logic
        return null;
    }
}
