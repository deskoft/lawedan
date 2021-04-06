from evennia import Command
from evennia.utils import evmenu

def citizenship_terminal_start(caller, raw_string, **kwargs):
    "This is the start of the citizenship terminal."

    def set_last_name(caller, prompt, user_input):
        caller.set_last_name = user_input.strip()

    def register_citizenship(caller):
        last_name = get_input(caller, "Write your last name:", set_last_name)

    text = "You approach the citizenship terminal. It presents you with several options."

    options = {}

    if not caller.has_citizenship():
        options.append({
            "key":("register", "r"),
            "desc":"Register as a citizen.",
            "goto":"citizenship_terminal_start",
            "exec":register_citizenship
        })


class CmdUseCitizenshipTerminal(Command):
    """
    This command allows you to use a citizenship terminal.

    Usage:
        use-citizenship_terminal
    """
    key = "use-citizenship-terminal"
    help_category = "terminals"
    def func(self):
        menu_tree = {
            "start":citizenship_terminal_start
        }
        evmenu.EvMenu(self.caller, menu_tree, start_node="citizenship_terminal_start")