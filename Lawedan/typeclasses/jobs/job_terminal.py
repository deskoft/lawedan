from typeclasses.objects import Object
from evennia.utils import evtable
from commands.cmdsets import jobs_cmdset
from evennia.commands.default import syscommands

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
        if self.ndb.terminal_text is None:
            self.ndb.terminal_text = ["JOB TERMINAL initiatied...", f"This terminal belongs to %s..." % (self.get_organization_name().upper(),)]

        if len(self.ndb.terminal_text) > 20:
            terminal_to_print =  self.ndb.terminal_text[-20:]
        else:
            terminal_to_print = self.ndb.terminal_text

        return '|/'.join(terminal_to_print)

    def get_terminal(self):
        terminal_text = self.get_terminal_text()
        output = "[  ----  ]  JOB TERMINAL  [  ----  ]|/"+ terminal_text
        return output

    def print_welcome(self):
        self.print_terminal_text(f"JOB TERMINAL owned by {self.get_organization_name()}...")

    def receive_input(self, raw_input, **kwargs):
        administrator = False
        if kwargs.get("administrator"):
            administrator = True

        user = False
        if kwargs.get("user"):
            user = kwargs.get("user")

        self.print_terminal_text(">> " + raw_input)
        cmd = raw_input.split(' ')

        if len(cmd) == 1:
            if cmd[0].lower() == "info":
                self.location.msg_contents(f"* {self.name} emits a |bblue UV light|n as it scans {user.name}.")
                if not user:
                    self.print_terminal_text("Failed to identify citizen...", error=True)
                    return
                self.print_terminal_text(f"Identified citizen {user.name.upper()}...")
                return
        if len(cmd) >= 4:
            if cmd[0].lower() == "set":
                if cmd[1].lower() == "org_name":
                    if not administrator:
                        self.print_terminal_text("You are not authorized to use this command.", error=True)
                        return
                    self.set_organization_name(' '.join(cmd[2:]))
                    self.print_terminal_text(f"Set |cORG NAME|n to |G{' '.join(cmd[2:])}|n.")
                    return

    def print_terminal_text(self, line, **kwargs):
        if self.ndb.terminal_text == None:
            self.ndb.terminal_text = []

        self.ndb.terminal_text.append(line)

        beep_type = '|yelectronic beep|n'
        if kwargs.get("error"):
            beep_type = '|relectronic buzz|n'

        self.location.msg_contents(f"* {self.name} emits an {beep_type}.")

    def return_appearance(self, looker):
        terminal = self.get_terminal()
        return f"|cOn the terminal, you see...|n|/|/" \
               "%s" % (terminal,)