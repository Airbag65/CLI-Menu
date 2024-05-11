import CLImenu

menu = CLImenu.CLIMenu()

item = CLImenu.MenuOption("test1")
item.add_menu_option(CLImenu.MenuOption("test"))

menu.add_menu_option(item)
menu.add_menu_option(CLImenu.MenuOption("test2"))
menu.add_menu_option(CLImenu.MenuOption("test3"))

def test_f():
    print("this do be working tho")

menu.add_func(test_f, "Test Func") 

menu.run()
