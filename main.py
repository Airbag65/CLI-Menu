import CLImenu

menu = CLImenu.CLIMenu()

item = CLImenu.MenuOption("test1")
def fn():
    print("internal func")
item.add_func(fn, "internal func")

menu.add_menu_option(item)

def f():
    print("func1")

def g():
    print("func2")

menu.add_func(f, "func1") 
menu.add_func(g, "func2")
menu.run()
