# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string
#from data.groups import constant as test_data

#@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    print("\n--- Debug Info ---")
    print("Created group:", group)
    print("Old groups (sorted):", sorted(old_groups, key=Group.id_or_max))
    print("New groups (sorted):", sorted(new_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=lambda g: Group.id_or_max(g)) == sorted(new_groups, key=lambda g: Group.id_or_max(g))


