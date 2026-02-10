import random

_db_sql_problem = {}

_debug = True

def add_sql_problem(my_id:str, my_pb:dict):
    global _db_sql_problem

    print (f"adding sql_problem {my_id}: {my_pb}")
    
    _db_sql_problem[my_id] = my_pb


def get_random_sql_problem() -> tuple[str, dict]:
    lk = list(_db_sql_problem.keys())

    if len(lk) == 0:
        return None
    
    draw = random.randint(0,len(lk)-1)
    k = lk[draw]
    return k, _db_sql_problem[k]
    
def get_sql_problem(my_id:str) -> tuple[str, dict]:
    if my_id not in _db_sql_problem:
        return None

    return my_id, _db_sql_problem[my_id]
