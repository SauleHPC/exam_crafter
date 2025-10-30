from llm_provider import get_chat_completion


def sql_queries_problem(topic):
    output = {}
    messages =         [
            {"role": "system", "content": "This is in the context of writing exam questions. If I ask  to give me something; just give me the thing. Don't put any fluff around it. If I ask for description of queries. Don't give me the queries, JUST the description."},
            {"role": "user", "content": "Give me a set of 3 relational tables on the topic researchers and labs they are affiliated with. Make sure to include a small sample of data."},
        ]

    
    response = get_chat_completion(messages= messages)
    print (response.choices[0].message.content)

    output["tables"] = response.choices[0].message.content
    
    messages.append({"role": "assistant", "content":response.choices[0].message.content})
    messages.append({"role": "user", "content":"Give me the description of three queries that could be made on these tables that are basic SELECT FROM WHERE queries."})

    response = get_chat_completion(messages= messages)
    print (response.choices[0].message.content)

    output["sql_basic"] = response.choices[0].message.content
    
    messages.append({"role": "assistant", "content":response.choices[0].message.content})
    messages.append({"role": "user", "content":"Give me the description of three queries that could be made on these tables that are SELECT JOIN WHERE queries."})

    response = get_chat_completion(messages= messages)
    print (response.choices[0].message.content)

    output["sql_join"] = response.choices[0].message.content

    messages.append({"role": "assistant", "content":response.choices[0].message.content})
    messages.append({"role": "user", "content":"Give me the description of three queries that could be made on these tables that are GROUP BY HAVING queries."})

    response = get_chat_completion(messages= messages)
    print (response.choices[0].message.content)

    output["sql_groupby"] = response.choices[0].message.content

    return output
    
    

if __name__ == "__main__":
    my_problem = sql_queries_problem("")
    print(my_problem)
