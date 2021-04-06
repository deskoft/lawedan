from typeclasses.objects import Object
from commands.cmdsets.terminal_cmdset import CitizenshipTerminalCmdSet

class CitizenshipTerminal(Object):
    def at_object_creation(self):
        self.locks.add("get:perm(Builder)")
        self.cmdset.add(CitizenshipTerminalCmdSet, permanent=True)