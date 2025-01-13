from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count_contacts() == 0:
        contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="vanya",
                          title="Manager", company="TestCo", home="23456",
                          mobile="sdfgh", work="898783", fax="9000", email="test1@mail.com",
                          email2="test2@mail.com",
                          email3="test3@mail.com", bday="21", month="March", year="1980",
                          address2="Some Address 2 345,78",
                          note="Test note", address="Some Address 345,678")
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
