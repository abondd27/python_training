from model.contact import Contact


def test_modify_first_contact(app):

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
    contact = Contact(firstname="Ivan2", middlename="Ivanovich2", lastname="Ivanov888", nickname="vanya2",
                title="Manager2", company="TestCo2", home="234562",
                mobile="sdfgh2", work="8987832", fax="90002", email="test1@mail.com2",
                email2="test2@mail.com2",
                email3="test3@mail.com2", bday="21", month="March", year="1980",
                address2="Some Address 2 345,782",
                note="Test note2", address="Some Address 345,6782")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
