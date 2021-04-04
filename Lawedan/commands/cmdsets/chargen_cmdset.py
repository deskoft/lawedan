from evennia import CmdSet
from commands.cmds import chargen_cmds as chargen

class ChargenCmdSet(CmdSet):
    """
    This is the CmdSet for all commands available in Chargen rooms.
    """
    key = "ChargenCmdSet"
    def at_cmdset_creation(self):
        self.add(chargen.CmdSetAge())
        self.add(chargen.CmdSetGender())
        self.add(chargen.CmdSetName())