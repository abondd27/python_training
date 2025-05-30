# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest




#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app,json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
