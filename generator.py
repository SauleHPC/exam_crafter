from config import config
import sql_crafter
import theme
import uuid
import requests

if __name__ == "__main__":
    my_theme = theme.theme_selector()
    
    my_problem = sql_crafter.sql_queries_problem(my_theme["theme_selected"])

    if my_problem == None:
        print ("could not gen")
        exit (-1)
        
    
    my_uuid = uuid.uuid4().hex

    payload = {my_uuid: my_problem}

    data = {"meta":{"secret": config["remote_backend"]["secret"]},
            "payload": payload}
    
    ret = requests.post(config["remote_backend"]["url"]+"/api/upload_sql_query", json=data)
    
    print (ret)
    
