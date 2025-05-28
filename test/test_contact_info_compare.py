import re
from operator import index
from random import randrange


def test_contact_info_compare_home_and_edit_page(app):
    contact_list_on_home_page = app.contact.get_contact_list()
    index = randrange(len(contact_list_on_home_page))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "", map(lambda x: clear(x),filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))