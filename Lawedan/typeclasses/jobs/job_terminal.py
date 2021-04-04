from typeclasses.objects import Object
from evennia.utils import evtable
from commands.cmdsets import jobs_cmdset

class JobTerminal(Object):
    """
    This class represents a job terminal, which will be able to record employees.
    """

    def at_object_creation(self):
        self.tags.add("job-terminal")
        self.cmdset.add(jobs_cmdset.JobTerminalCmdSet)

    def get_organization_name(self):
        if self.db.org_name is None:
            self.db.org_name = "Undefined"
        return self.db.org_name

    def set_organization_name(self, name:str):
        self.db.org_name = name

    def get_terminal_text(self):
        if self.db.terminal_text is None or not isinstance(self.db.terminal_text, list):
            self.db.terminal_text = ["JOB TERMINAL initiatied...", f"This terminal belongs to %s..." % (self.get_organization_name().upper(),)]
        return '|/'.join(self.db.terminal_text)

    def get_terminal(self):
        terminal_text = self.get_terminal_text()
        table = evtable.EvTable("JOB TERMINAL", table=[[terminal_text]], border="cells")
        return str(table)


    def print_terminal_text(self, line):
        self.db.terminal_text.append(line)

    def return_appearance(self, looker):
        terminal = self.get_terminal()
        return f"|cOn the terminal, you see...|n|/|/" \
               "%s" % (terminal,)