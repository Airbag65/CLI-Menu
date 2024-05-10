import types
from menuoption import MenuOption
from error import IllegalArgumentError
from icecream import ic
class CLIMenu:
    def __init__(self):
        self.menu_options = {}

    def add_menu_option(self, menu_option: MenuOption, option_index: int) -> None:
        if not isinstance(menu_option, MenuOption):
            raise IllegalArgumentError("Argument must be of type 'CLIMenu'")
        self.menu_options[option_index] = menu_option

    def add_func(self, functionality, option_index: int):
        if not isinstance(functionality, types.FunctionType):
            raise IllegalArgumentError("Argument must be of type 'Function'")
        self.menu_options[option_index] = functionality

    def run(self) -> None:
        for key, val in self.menu_options.items():
            print(f"[{key}] {val.title}")
        choice = int(input(": "))
        if choice not in self.menu_options.keys():
            print("Not a valid option")
            return
        chosen_option = self.menu_options[choice]
        if isinstance(chosen_option, MenuOption):
            chosen_option.run()
        else:
            chosen_option()

