from typeclasses.objects import Object
from commands.cmdsets.terminal_cmdset import CitizenshipTerminalCmdSet

class CitizenshipTerminal(Object):
    locks = "get:perm(Builder)"
    def at_object_creation(self):
        self.cmdset.add(CitizenshipTerminalCmdSet)