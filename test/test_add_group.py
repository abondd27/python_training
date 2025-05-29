# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string

def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(2)
    ]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
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


