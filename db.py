import random

_db_sql_problem = {}

_db_sql_problem_access = {}

_debug = True

def _log_access_sql_problem(id):
    global _db_sql_problem_access
    if id in _db_sql_problem_access:
        _db_sql_problem_access[id] = _db_sql_problem_access[id]+1
    else:
        _db_sql_problem_access[id] = 1

def sql_problem_db_status():
    count = {}
    for k in _db_sql_problem_access:
        c = _db_sql_problem_access[k]
        if c in count:
            count[c] = count[c]+1
        else:
            count[c] = 1
    
    return {"size": len (_db_sql_problem),
            "access_count": count}

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
    _log_access_sql_problem(k)
    return k, _db_sql_problem[k]
    
def get_sql_problem(my_id:str) -> tuple[str, dict]:
    if my_id not in _db_sql_problem:
        return None

    _log_access_sql_problem(my_id)
    return my_id, _db_sql_problem[my_id]
