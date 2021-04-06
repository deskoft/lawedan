from evennia import CmdSet
from commands.cmds import terminal_cmds as terminal

class CitizenshipTerminalCmdSet(CmdSet):
    """
    This is the CmdSet for all commands available in Citizenship Terminals.
    """
    key = "CitizenshipTerminalCmdSet"
    def at_cmdset_creation(self):
        self.add(terminal.CmdUseCitizenshipTerminal())