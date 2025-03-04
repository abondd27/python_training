from model.group import Group
from random import randrange


#def test_modify_first_group(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test277", header="Test277", footer="Test277"))
#    app.group.modify_first_group(Group(name="Test2", header="Test2", footer="Test2"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)


def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test234"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New Header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_first_group_footer(app):
#   old_groups = app.group.get_group_list()
#   app.group.modify_first_group(Group(footer="New Footer"))
#   new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
