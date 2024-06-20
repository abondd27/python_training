from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(
            Contact(firstname="Andrey", middlename="Ivanovich", lastname="Petrov4", nickname="andy",
                    title="Accountant", company="TestComPo", home="23456",
                    mobile="sdfgh", work="898783", fax="9000", email="test1@mail.com",
                    email2="test2@mail.com",
                    email3="test3@mail.com", bday="21", month="March", year="1980",
                    address2="Some Address 2 345,78",
                    note="Test note", address="Some Address 345,678"))
    app.contact.modify_first_contact(Contact(firstname="Ivan2", middlename="Ivanovich2", lastname="Ivanov888", nickname="vanya2",
                title="Manager2", company="TestCo2", home="234562",
                mobile="sdfgh2", work="8987832", fax="90002", email="test1@mail.com2",
                email2="test2@mail.com2",
                email3="test3@mail.com2", bday="21", month="March", year="1980",
                address2="Some Address 2 345,782",
                note="Test note2", address="Some Address 345,6782"))
