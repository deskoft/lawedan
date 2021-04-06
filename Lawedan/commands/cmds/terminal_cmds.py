from evennia import Command

class CmdUseCitizenshipTerminal(Command):
    """
    This command allows you to use a citizenship terminal.

    Usage:
        use-citizenship_terminal
    """
    key = "use-citizenship-terminal"
    help_category = "terminals"
    def func(self):
        self.caller.msg("WORK IN PROGRESS.")