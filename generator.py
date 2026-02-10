from config import config
import sql_crafter
import theme
import uuid
import requests

def generate_one():
    my_theme = theme.theme_selector()
    
    my_problem = sql_crafter.sql_queries_problem(my_theme["theme_selected"])

    if my_problem == None:
        print ("could not gen")
        return
        
    my_uuid = uuid.uuid4().hex

    payload = {my_uuid: my_problem}

    data = {"meta":{"secret": config["remote_backend"]["secret"]},
            "payload": payload}
    
    ret = requests.post(config["remote_backend"]["url"]+"/api/upload_sql_query", json=data)
    
    print (ret)
    

def how_many_you_want():
    ret = requests.get(config["remote_backend"]["url"]+"/api/sql_problem_db_status")
    ret.raise_for_status()
    return ret.json()['want']
    
if __name__ == "__main__":
    atmost = 10
    wanted = how_many_you_want()

    howmany = min(atmost, wanted)
    howmany = max(howmany,0)
    
    for i in range (howmany):
        try:
            generate_one()
        except Exception as e: #all kind of bad things can happen in normal operations
            print ('==========exception=============')
            print(e)
            traceback.print_exc()
            print ('================================')
            
