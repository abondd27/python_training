from model.group import Group
import jsonpickle
import random
import string
import os.path
import getopt
import sys
from model.contact import Contact






try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "test/data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a




def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_1_to_30():
    return str(random.randint(1, 30))

def random_month():
    months = ["January", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return random.choice(months)

def random_year():
    return str(random.randint(1940, 2010))

def random_phone():
    symbols = '+7' + ''.join(random.choice(string.digits) for i in range(10))
    return symbols

def random_email():
    symbols = ''.join(random.choice(string.ascii_letters) for i in range(5)) + '@email.com'
    return symbols

test_data = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),nickname=random_string("nickname",5),
            title=random_string("title",10),company=random_string("company",15),
            home=random_phone(),mobile=random_phone(),
            work=random_phone(),fax=random_string("fax",5),
            email1=random_email(),email2=random_email(),
            email3=random_email(),bday=random_1_to_30(),
            month=random_month(),year=random_year(),note=random_string("note",15),
            address=random_string("address",20),address2=random_string("address2",20))
    for i in range(2)
    ]




file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))