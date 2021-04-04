from evennia import Command

class CmdConfigureJobTerminal(Command):
    """
    This is the command to configure job terminals, available to both the owner as well as builders

    Usage:
        configure-job-terminal <terminal>
    """
    key = "configure-job-terminal"
    help_category = "job terminal"
    locks = "cmd:perm(Builders)"

    def func(self):
        syntax_err = "Please refer to |lchelp configure-job-terminal|lthelp configure-job-terminal|le for more information on how to use this command."

        caller = self.caller
        terminal = self.obj

        if not self.args:
            caller.msg(syntax_err)
            return
        args = self.args.split(' ')

        target = self.args.strip()

        target = caller.search(target)

        if not target:
            caller.msg("Cannot find job terminal.")
            caller.msg(syntax_err)
            return

        if not "job-terminal" in target.tags.all():
            caller.msg("This is not a job terminal.")
            caller.msg(syntax_err)
            return


        caller.execute_cmd("walks up to the %s and types on it.", (target.name,))