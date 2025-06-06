# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string
#from data.groups import constant as test_data

#@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=lambda g: Group.id_or_max(g)) == sorted(new_groups, key=lambda g: Group.id_or_max(g))


