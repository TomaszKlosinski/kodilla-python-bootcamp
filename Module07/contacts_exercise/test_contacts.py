import unittest
from contacts import BaseContact, BusinessContact

contact = BaseContact(
    first_name="Tomasz",
    last_name="Klosinski",
    private_phone="+41 123 132 123",
    email_address="tomasz.klosinski@example.com",
)

business_contact = BusinessContact(
    first_name="John",
    last_name="Doe",
    private_phone="+41 999 999 999",
    email_address="joe.doe@example.com",
    position="DevOps Engineer",
    company="XYZ AG",
    company_phone="+41 321 321 321",
)

class TestContacts(unittest.TestCase):
    def test_base_contact(self) -> None:
        self.assertEqual(contact.first_name, "Tomasz")
        self.assertEqual(contact.last_name, "Klosinski")
        self.assertEqual(contact.private_phone, "+41 123 132 123")
        self.assertEqual(contact.email_address, "tomasz.klosinski@example.com")


    def test_business_contact(self) -> None:
        self.assertEqual(business_contact.first_name, "John")
        self.assertEqual(business_contact.last_name, "Doe")
        self.assertEqual(business_contact.private_phone, "+41 999 999 999")
        self.assertEqual(business_contact.email_address, "joe.doe@example.com")
        self.assertEqual(business_contact.position, "DevOps Engineer")


    def test_contact_function(self) -> None:
        self.assertEqual(contact.contact(), "Dial +41 123 132 123 to call Tomasz Klosinski")
        self.assertEqual(business_contact.contact(), "Dial +41 321 321 321 to call John Doe from XYZ AG")


    def test_label_length_property(self) -> None:
        self.assertEqual(contact.label_length, 16)
        self.assertEqual(business_contact.label_length, 8)


if __name__ == "__main__":
    unittest.main()
