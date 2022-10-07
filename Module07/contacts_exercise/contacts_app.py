from faker import Faker
from contacts import BaseContact, BusinessContact


def create_contacts() -> list[BaseContact]:
    fake = Faker()
    contacts = []
    for _ in range(10):
        private_contact = BaseContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            private_phone=fake.phone_number(),
            email_address=fake.free_email(),
        )
        contacts.append(private_contact)

        company_contact = BusinessContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            private_phone=fake.phone_number(),
            email_address=fake.company_email(),
            position=fake.job(),
            company=fake.company(),
            company_phone=fake.phone_number(),
        )
        contacts.append(company_contact)

    return contacts


def main() -> None:
    contacts = create_contacts()

    for contact in contacts:
        print(contact.contact())
        print(f"Name length {contact.label_length}")


if __name__ == "__main__":
    main()