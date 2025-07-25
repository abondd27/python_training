import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self,host, name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)



    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname,address, email, email2, email3, home, mobile, work) = row
                list.append(Contact(id=str(id),firstname=firstname,lastname=lastname,address=address, email1=email, email2=email2,email3=email3, home=home, mobile=mobile, work=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()




