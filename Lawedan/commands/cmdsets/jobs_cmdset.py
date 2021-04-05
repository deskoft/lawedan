from evennia import CmdSet
from commands.cmds import job_cmds as jobs

class JobTerminalCmdSet(CmdSet):
    """
    This is the CmdSet for all commands available with job terminals.
    """
    key = "JobTerminalCmdSet"
    def at_cmdset_creation(self):
        self.add(jobs.CmdConfigureJobTerminal())
        self.add(jobs.CmdUseJobTerminal())