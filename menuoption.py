from error import IllegalArgumentError
import types

class MenuOption:
    pass

class MenuOption:
    def __init__(self, title: str):
        self.title = title
        self.menu_options = {}

    def add_menu_option(self, menu_option: MenuOption) -> None:
        if not isinstance(menu_option, MenuOption):
            raise IllegalArgumentError("Argument must be of type 'CLIMenu'")
        self.menu_options[len(self.menu_options) + 1] = menu_option

    def add_func(self, functionality, title: str):
        if not isinstance(functionality, types.FunctionType):
            raise IllegalArgumentError("Argument must be of type 'Function'")
        self.menu_options[len(self.menu_options) + 1] = [title, functionality]

    def run(self):
        for key, val in self.menu_options.items():
            if isinstance(val, MenuOption):
                print(f"[{key}] {val.title}")
            else:
                print(f"[{key}] {val[0]}")
        choice = int(input(": "))
 
