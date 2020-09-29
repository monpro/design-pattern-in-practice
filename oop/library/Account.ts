import { AccountStatus, Person } from "./contants";

export default abstract class Account {
    private id: string;
    private password: string;
    private status: AccountStatus;
    private person: Person;

    public resetPassword = () => {
        this.password = '';
    };
}
