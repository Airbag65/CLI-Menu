import CLImenu

menu = CLImenu.CLIMenu()

item = CLImenu.MenuOption()
item.add_menu_option(CLImenu.MenuOption(), 1)

menu.add_menu_option(item, 1)
menu.add_menu_option(CLImenu.MenuOption(), 2)
menu.add_menu_option(CLImenu.MenuOption(), 3)

menu.run()
