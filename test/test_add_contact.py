# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest




#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app,db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key= lambda g: Contact.id_or_max(g)) == sorted(new_contacts, key=lambda g: Contact.id_or_max(g))





