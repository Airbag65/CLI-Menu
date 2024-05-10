import CLImenu

menu = CLImenu.CLIMenu()

item = CLImenu.MenuOption("test1")
# item.add_menu_option(CLImenu.MenuOption(), 1)

menu.add_menu_option(item, 1)
menu.add_menu_option(CLImenu.MenuOption("test2"), 2)
menu.add_menu_option(CLImenu.MenuOption("test3"), 3)

menu.run()
