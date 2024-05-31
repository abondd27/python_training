from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Test2", header="Test2", footer="Test2"))
    app.session.logout()
