import re
from operator import index
from random import randrange
from model.contact import Contact

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


def test_contact_info_compare_homepage_with_db(app, db):
    def normalize_string(s):
        return ' '.join(s.split()) if s else s

    # Функция для нормализации телефонов (удаление лишних символов)
    def normalize_phone(phone):
        return phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '') if phone else phone

    # Получаем контакты с главной страницы
    contacts_from_homepage = app.contact.get_contact_list()
    # Получаем контакты из базы данных
    contacts_from_db = db.get_contact_list()

    assert len(contacts_from_homepage) == len(contacts_from_db)

    contacts_from_homepage_sorted = sorted(contacts_from_homepage, key=Contact.id_or_max)
    contacts_from_db_sorted = sorted(contacts_from_db, key=Contact.id_or_max)

    for contact_hp, contact_db in zip(contacts_from_homepage_sorted, contacts_from_db_sorted):
        assert contact_hp.firstname == contact_db.firstname
        assert contact_hp.lastname == contact_db.lastname

        # Нормализуем адреса перед сравнением
        db_address = normalize_string(contact_db.address) if contact_db.address is not None else ""
        hp_address = normalize_string(contact_hp.address) if contact_hp.address is not None else ""
        assert hp_address == db_address

        assert contact_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)
        assert contact_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)