from evennia import Command

class CmdSetAge(Command):
    """
    This command allows you define the age of your character. Allowed ages start from 16 to 80 years old.
    Please note that aging through the passage of time will be implemented.
    
    Usage:
        age <age>
    """
    key = "age"
    help_category = "chargen"
    
    syntax_err = "Type |lchelp age|lthelp age|le for more information on the syntax of this command."
    
    def func(self):
        caller = self.caller
        if not self.args:
            caller.msg("You need to define an age for your character.")
            caller.msg(self.syntax_err)
            return
        try:
            age = int(self.args.strip())
        except Exception:
            caller.msg("Please type the age in numbers (for example |yage 20|n).")
            caller.msg(self.syntax_err)
            return
        
        if age < 16 or age > 80:
            caller.msg("Your age has to be between 16 and 80 years old.")
            caller.msg(self.syntax_err)
            return
        
        caller.db.age = int(self.args.strip())
        caller.msg("You have set your |cage|n to |g%s|n." % (str(caller.db.age),))

class CmdSetGender(Command):
    """
    This command allows you define the gender of your character. Allowed genders are |lcgender male|ltmale|le, |lcgender female|ltfemale|le and |lcgender androgynous|ltandrogynous|le.

    Usage:
        gender <male/female/androgynous>
    """
    key = "gender"
    help_category = "chargen"
    
    syntax_err = "Type |lchelp gender|lthelp gender|le for more information on the syntax of this command."
    
    def func(self):
        caller = self.caller
        if not self.args:
            caller.msg("You need to define a gender for your character.")
            caller.msg(self.syntax_err)
            return
        
        if not self.args.lower().strip() in ["male", "female", "androgynous"]:
            caller.msg("You need to pick one of the listed genders that our codebase supports.")
            caller.msg(self.syntax_err)
            return
        
        caller.db.gender = self.args.lower().strip()
        caller.msg("You have set your |cgender|n to |g%s|n." % (caller.db.gender,))


class CmdSetName(Command):
    """
    This command allows you to set a name. Please not that it has to be a realistic name, without numbers, and without spaces.
    For example: John, Lara, Raymond.

    Usage:
        setname <name>
    """
    key = "setname"
    help_category = "chargen"
    
    syntax_err = "Type |lchelp setname|lthelp setname|le for more information on the syntax of this command."
    
    def func(self):
        caller = self.caller
        if not self.args:
            caller.msg("You need to define a name for your character.")
            caller.msg(self.syntax_err)
            return
        
        raw_name = str(self.args).strip()
        
        if not raw_name.isalpha():
            caller.msg("You have to write a name that respects our naming convention.")
            caller.msg(self.syntax_err)
            return
        
        caller.key = raw_name
        caller.msg("You have set your |cname|n to |g%s|n." % (caller.key,))