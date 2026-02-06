from llm_provider import get_chat_completion, get_chat_completion_JSON
import json

debug = False

def format_relations(tables):
    strout=""
    for t in tables:
        strout += t['relationname']+" = ("
        for f in t['fields']:
            strout+=f+", "
        strout= strout[:-2]
        strout += ")\n"
    return strout

def sql_queries_problem(theme:str):
    if theme == None or theme == "":
        theme = "Researchers and lab they are affiliated with"
    nbquestion = 3
        
    output = {}
    output['theme'] = theme
    tabletemplate = [
        {
            "relationname": "Exhibits",
            "fields": [ "ExhibitID", "Title", "Description", "DateAcquired", "ArtistID"    ],
            "data": [
                ["E001", "The Starry Night", "Van Gogh's masterpiece", "1923-10-15", "A001"],
                ["E002", "Mona Lisa", "Famous smile of Mona Lisa", "1947-06-21", "A002"]
            ]
        },
        {
            "relationname": "Artists",
            "fields": ["ArtistID", "FirstName", "LastName","BirthDate", "Nationality"    ],
            "data": [
                ["A001", "Vincent", "Van Gogh", "1853-03-30", "Dutch"],
                ["A002", "Leonardo", "Da Vinci", "1452-04-15", "Italian"]
            ]
        }
    ]
    
    base_messages =         [
            {"role": "system", "content": "This is in the context of writing exam questions. If I ask to give me something; just give me the thing. Don't put any fluff around it. If I ask the same question multiple times, give me a different answer."},
            {"role": "user", "content": "Give me a set of relational tables on the theme of \"{}\". Make sure to include a small sample of data. No more than 4 tables.".format(theme)},
        ]

    
#    response = get_chat_completion(messages= base_messages)
    response = get_chat_completion_JSON(messages= base_messages, template = tabletemplate)
    if response == None:
        return None
    
    output["tables"] = response

    #print (format_relations(output["tables"]))
    base_messages.append({"role": "assistant", "content":format_relations(output["tables"])})

    
    output["sql_basic"] = []

    template = {"prompt":" Write the SQL query that returns the artifact identifier and its name of more than 3 pounds.", "sql": "SELECT artifactID, name FROM artifacts WHERE weight < 3;"}
    
    for i in range (0,nbquestion):
        messages = base_messages.copy() 
        messages.append({"role": "user", "content":"Give me the prompt of a query that could be made on these tables that are basic SELECT FROM WHERE queries; no JOIN or GROUP BY."},
 )
        response = get_chat_completion_JSON(messages= messages, template=template)
        if response == None:
            continue
        
        messages.append({"role": "user", "content":f"Give me something else than: {response['prompt']}"})
                
        if debug:
            print(response)
        output["sql_basic"].append( response)

        
    output["sql_join"] = []
    for i in range (0,nbquestion):
        messages = base_messages.copy()
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are SELECT JOIN WHERE queries; no GROUP BY."})

        response = get_chat_completion_JSON(messages= messages, template=template)
        if response == None:
            continue
        messages.append({"role": "assistant", "content":f"Give me something else than:{response['prompt']}"})
                
        if debug:
            print(response)
        output["sql_join"].append( response)

    output["sql_groupby"] = []
    for i in range (0,nbquestion):
        messages = base_messages.copy()
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are GROUP BY HAVING queries."})

        response = get_chat_completion_JSON(messages= messages, template=template)
        if response == None:
            continue
        messages.append({"role": "assistant", "content":f"Give me something else than:{response['prompt']}"})
                
        if debug:
            print(response)

        output["sql_groupby"].append(response)

    return output
    

if __name__ == "__main__":
    my_problem = sql_queries_problem("Museum and artifacts")

    print(json.dumps(my_problem, indent=2))

    
