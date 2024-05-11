import types
from menuoption import MenuOption
from error import IllegalArgumentError

class CLIMenu:
    def __init__(self):
        self.menu_options = {}

    def add_menu_option(self, menu_option: MenuOption) -> None:
        if not isinstance(menu_option, MenuOption):
            raise IllegalArgumentError("Argument must be of type 'CLIMenu'")
        self.menu_options[len(self.menu_options) + 1] = menu_option

    def add_func(self, functionality, title: str):
        if not isinstance(functionality, types.FunctionType):
            raise IllegalArgumentError("Argument must be of type 'Function'")
        self.menu_options[len(self.menu_options) + 1] = [title, functionality]

    def run(self) -> None:
        for key, val in self.menu_options.items():
            if isinstance(val, MenuOption):
                print(f"[{key}] {val.title}")
            else:
                print(f"[{key}] {val[0]}")
        choice = int(input(": "))
        if choice not in self.menu_options.keys():
            print("Not a valid option")
            return
        chosen_option = self.menu_options[choice]
        if isinstance(chosen_option, MenuOption):
            chosen_option.run()
        else:
            chosen_option[1]()

