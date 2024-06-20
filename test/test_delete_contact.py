from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(
            Contact(firstname="Andrey", middlename="Ivanovich", lastname="Petrov", nickname="andy",
                    title="Accountant", company="TestComPo", home="23456",
                    mobile="sdfgh", work="898783", fax="9000", email="test1@mail.com",
                    email2="test2@mail.com",
                    email3="test3@mail.com", bday="21", month="March", year="1980",
                    address2="Some Address 2 345,78",
                    note="Test note", address="Some Address 345,678"))
    app.contact.delete_first_contact()
