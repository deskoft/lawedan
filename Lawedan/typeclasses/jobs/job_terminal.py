from typeclasses.objects import Object
from evennia.utils import evtable
from commands.cmdsets import jobs_cmdset

class JobTerminal(Object):
    """
    This class represents a job terminal, which will be able to record employees.
    """

    def at_object_creation(self):
        self.tags.add("job-terminal")
        self.cmdset.add(jobs_cmdset.JobTerminalCmdSet, permanent=True)

    def get_organization_name(self):
        if self.db.org_name is None:
            self.db.org_name = "Undefined"
        return self.db.org_name

    def set_organization_name(self, name:str):
        self.db.org_name = name

    def get_terminal_text(self):
        if self.db.terminal_text is None:
            self.db.terminal_text = ["JOB TERMINAL initiatied...", f"This terminal belongs to %s..." % (self.get_organization_name().upper(),)]

        terminal_to_print = self.db.terminal_text

        if len(terminal_to_print) > 10:
            terminal_to_print = terminal_to_print[-20:]

        return '|/'.join(terminal_to_print)

    def get_terminal(self):
        terminal_text = self.get_terminal_text()
        table = evtable.EvTable("JOB TERMINAL", table=[[terminal_text]], border="cells")
        return str(table)

    def receive_input(self, raw_input, **kwargs):
        administrator = False
        if kwargs.get("administrator"):
            administrator = True

        cmd = raw_input.split(' ')

        if len(raw_input) >= 3:
            if cmd[0].lower() == "set":
                if cmd[1].lower() == "org_name":
                    self.set_organization_name(' '.join(cmd[2:]))
                    self.print_terminal_text(f"Set |cORG NAME|n to |G{' '.join(cmd[2:])}|n.")


        self.print_terminal_text(">> " + raw_input)

    def print_terminal_text(self, line):
        if self.db.terminal_text == None:
            self.db.terminal_text = []

        self.db.terminal_text.append(line)

    def return_appearance(self, looker):
        terminal = self.get_terminal()
        return f"|cOn the terminal, you see...|n|/|/" \
               "%s" % (terminal,)