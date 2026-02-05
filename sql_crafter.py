from llm_provider import get_chat_completion, get_chat_completion_JSON
import json

debug = True

def sql_queries_problem(theme:str):
    if theme == None or theme == "":
        theme = "Researchers and lab they are affiliated with"
    nbquestion = 3
        
    output = {}
    output['theme'] = theme
    base_messages =         [
            {"role": "system", "content": "This is in the context of writing exam questions. If I ask to give me something; just give me the thing. Don't put any fluff around it. If I ask the same question multiple times, give me a different answer."},
            {"role": "user", "content": "Give me a set of relational tables on the theme of \"{}\". Make sure to include a small sample of data. No more than 4 tables.".format(theme)},
        ]

    
    response = get_chat_completion(messages= base_messages)
    base_messages.append({"role": "assistant", "content":response.choices[0].message.content})

    output["tables"] = response.choices[0].message.content

    output["sql_basic"] = []
    
    for i in range (0,nbquestion):
        messages = base_messages.copy()
        messages.append({"role": "user", "content":"Give me the prompt of a query that could be made on these tables that are basic SELECT FROM WHERE queries; no JOIN or GROUP BY."},
 )
        response = get_chat_completion_JSON(messages= messages, template={"prompt":" Write the SQL query that returns the artifact identifier and its name of more than 3 pounds.", "sql": "SELECT artifactID, name FROM artifacts WHERE weight < 3;"})
        if response == None:
            continue
        
        messages.append({"role": "assistant", "content":json.dumps(response)})
                
        if debug:
            print(response)
        output["sql_basic"].append( response)

        
    output["sql_join"] = []
    for i in range (0,nbquestion):
        messages = base_messages.copy()
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are SELECT JOIN WHERE queries; no GROUP BY."})

        response = get_chat_completion_JSON(messages= messages, template={"prompt":" Write the SQL query that returns the artifact identifier and its name of more than 3 pounds.", "sql": "SELECT artifactID, name FROM artifacts WHERE weight < 3;"})
        if response == None:
            continue
        messages.append({"role": "assistant", "content":json.dumps(response)})
                
        if debug:
            print(response)
        output["sql_join"].append( response)

    output["sql_groupby"] = []
    for i in range (0,nbquestion):
        messages = base_messages.copy()
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are GROUP BY HAVING queries."})

        response = get_chat_completion_JSON(messages= messages, template={"prompt":" Write the SQL query that returns the artifact identifier and its name of more than 3 pounds.", "sql": "SELECT artifactID, name FROM artifacts WHERE weight < 3;"})
        if response == None:
            continue
        messages.append({"role": "assistant", "content":json.dumps(response)})
                
        if debug:
            print(response)

        output["sql_groupby"].append(response)

    return output
    

if __name__ == "__main__":
    my_problem = sql_queries_problem("")

    print(json.dumps(my_problem, indent=2))

    
