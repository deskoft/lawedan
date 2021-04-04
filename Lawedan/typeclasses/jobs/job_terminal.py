from typeclasses.objects import Object
from evennia.utils import evtable

class JobTerminal(Object):
    """
    This class represents a job terminal, which will be able to record employees.
    """


    def modify_rank_name(self, rank_num, new_name):
        if self.db.ranks is None:
            self.db.ranks = {}
            
        if self.db.ranks[rank_num] is None:
            self.db.ranks[rank_num] = {}
        
        self.db.ranks[rank_num]["name"] = new_name

    def return_appearance(self, looker):
        if self.db.terminal_text is None:
            self.db.terminal_text = "Welcome to the Job Terminal v.0.1."
        table = evtable.EvTable("JOB TERMINAL", table=[[self.db.terminal_text]], border="cells")
        return "Test."