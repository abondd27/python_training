# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="vanya",
                      title="Manager", company="TestCo", home="23456",
                      mobile="sdfgh", work="898783", fax="9000", email="test1@mail.com",
                      email2="test2@mail.com",
                      email3="test3@mail.com", bday="21", month="March", year="1980",
                      address2="Some Address 2 345,78",
                      note="Test note", address="Some Address 345,678")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                      title="", company="", home="",
                      mobile="", work="", fax="", email="", email2="",
                      email3="", bday="", month="-", year="", address2="",
                      note="", address="")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
