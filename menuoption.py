from error import IllegalArgumentError
import types

class MenuOption:
    pass

class MenuOption:
    def __init__(self):
        self.menu_options = []

    def add_menu_option(self, menu_option: MenuOption, option_index: int) -> None:
        if not isinstance(menu_option, MenuOption):
            raise IllegalArgumentError("Argument must be of type 'CLIMenu'")
        print("good job")
        self.menu_options[option_index] = menu_option

    def add_func(self, functionality, option_index: int):
        if not isinstance(functionality, types.FunctionType):
            raise IllegalArgumentError("Argument must be of type 'Function'")
        print("good job")
        self.menu_options[option_index] = functionality
