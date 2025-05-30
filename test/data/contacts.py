from model.contact import Contact

test_data = [Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="vanya",
                  title="Manager", company="TestCo", home="23456",
                  mobile="sdfgh", work="898783", fax="9000", email1="test1@mail.com",
                  email2="test2@mail.com",
                  email3="test3@mail.com", bday="21", month="March", year="1980",
                  address2="Some Address 2 345,78",
                  note="Test note", address="Some Address 345,678")
             ]



#def random_string(prefix, max_len):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])



#test_data = [
#    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#            lastname=random_string("lastname", 10),nickname=random_string("nickname",5),
#            title=random_string("title",10),company=random_string("company",15),
#            home=random_phone(),mobile=random_phone(),
#            work=random_phone(),fax=random_string("fax",5),
#            email1=random_email(),email2=random_email(),
#            email3=random_email(),bday=random_1_to_30(),More actions
#            month=random_month(),year=random_year(),note=random_string("note",15),
#            address=random_string("address",20),address2=random_string("address2",20))
#    for i in range(2)
#    ]