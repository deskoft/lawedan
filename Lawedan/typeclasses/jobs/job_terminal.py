from typeclasses.objects import Object

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
