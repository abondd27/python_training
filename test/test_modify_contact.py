from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Ivan2", middlename="Ivanovich2", lastname="Ivanov2", nickname="vanya2",
                title="Manager2", company="TestCo2", home="234562",
                mobile="sdfgh2", work="8987832", fax="90002", email="test1@mail.com2",
                email2="test2@mail.com2",
                email3="test3@mail.com2", bday="21", month="March", year="1980",
                address2="Some Address 2 345,782",
                note="Test note2", address="Some Address 345,6782"))
