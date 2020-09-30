import { AccountStatus, Person } from "./contants";

export default abstract class Account {
    private _id: string;
    private _password: string;
    private _status: AccountStatus;
    private _person: Person;

    get id(): string {
        return this._id;
    }

    set id(value: string) {
        this._id = value;
    }

    get password(): string {
        return this._password;
    }

    set password(value: string) {
        this._password = value;
    }

    get status(): AccountStatus {
        return this._status;
    }

    set status(value: AccountStatus) {
        this._status = value;
    }

    get person(): Person {
        return this._person;
    }

    set person(value: Person) {
        this._person = value;
    }

    resetPassword = () => {
        this._password = '';
    };
}
