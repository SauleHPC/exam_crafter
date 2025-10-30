from llm_provider import get_chat_completion


def sql_queries_problem(theme:str):
    if theme == None or theme == "":
        theme = "Researchers and lab they are affiliated with"
    nbquestion = 3
        
    output = {}
    messages =         [
            {"role": "system", "content": "This is in the context of writing exam questions. If I ask  to give me something; just give me the thing. Don't put any fluff around it. If I ask for description of queries. Don't give me the queries, JUST the prompt that you would give a student. If I ask the same question multiple times, give me a different answer."},
            {"role": "user", "content": "Give me a set of relational tables on the theme of \"{}\". Make sure to include a small sample of data.".format(theme)},
        ]

    
    response = get_chat_completion(messages= messages)
    messages.append({"role": "assistant", "content":response.choices[0].message.content})
    #print (response.choices[0].message.content)

    output["tables"] = response.choices[0].message.content

    output["sql_basic"] = []
    
    for i in range (0,nbquestion):
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are basic SELECT FROM WHERE queries; no JOIN or GROUP BY."})

        response = get_chat_completion(messages= messages)
        messages.append({"role": "assistant", "content":response.choices[0].message.content})
                
        #print (response.choices[0].message.content)

        output["sql_basic"].append( response.choices[0].message.content)

    output["sql_join"] = []
    for i in range (0,nbquestion):
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are SELECT JOIN WHERE queries; no GROUP BY."})
        response = get_chat_completion(messages= messages)
        messages.append({"role": "assistant", "content":response.choices[0].message.content})

        #print (response.choices[0].message.content)
                
        output["sql_join"].append( response.choices[0].message.content)

    output["sql_groupby"] = []
    for i in range (0,nbquestion):
        messages.append({"role": "user", "content":"Give me the description of a query that could be made on these tables that are GROUP BY HAVING queries."})

        response = get_chat_completion(messages= messages)
        #print (response.choices[0].message.content)
        messages.append({"role": "assistant", "content":response.choices[0].message.content})

        output["sql_groupby"].append(response.choices[0].message.content)

    return output
    



if __name__ == "__main__":
    my_problem = sql_queries_problem("")

    print(my_problem)

    
