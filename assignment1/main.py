from singlelist import SingleList as sl

###Main
slist = sl()

slist.create_head()

slist.node_append("park")
slist.node_append("choi")
slist.node_append("lee")
slist.node_insert("choi", "hwang")

slist.all_print()

slist.node_modifi("choi","siwo")
slist.all_print()
slist.node_del("park")
slist.all_print()
slist.node_find("hwang")
slist.all_print()