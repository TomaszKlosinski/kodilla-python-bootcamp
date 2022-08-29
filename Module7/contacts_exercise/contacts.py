class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email_address = email_address

    def contact(self) -> str:
        return f"Dial {self.private_phone} to call {self.first_name} {self.last_name}"

    @property
    def label_length(self) -> int:
        full_name = self.first_name + " " + self.last_name
        return len(full_name)


class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.company_phone = company_phone

    def contact(self) -> str:
        return f"Dial {self.company_phone} to call {self.first_name} {self.last_name} from {self.company}"

