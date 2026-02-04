from llm_provider import get_chat_completion


def theme_selector():
    output = {}
    messages =         [
            {"role": "system", "content": "This is in the context of writing exam questions. If I ask  to give me something; just give me the thing. Don't put any fluff around it."},
            {"role": "user", "content": "Give me a number of topics that could be good for an example of a database that students may work on. Get them to range from society topic, to entertainment, to business. Give me about 20 different ones."},
        ]

    
    response = get_chat_completion(messages= messages)
    messages.append({"role": "assistant", "content":response.choices[0].message.content})
    #print (response.choices[0].message.content)

    output = {}
    output['themes']=response.choices[0].message.content

    messages.append({"role": "user", "content":"Out of those, pick one randomly"})
    response = get_chat_completion(messages= messages)
    output['theme_selected']=response.choices[0].message.content
   

    return output
