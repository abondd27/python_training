from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Test2", header="Test2", footer="Test2"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New Header"))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="New Footer"))
