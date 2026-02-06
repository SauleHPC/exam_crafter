from llm_provider import get_chat_completion, get_chat_completion_JSON
import random

def theme_selector():
    output = {}
    messages =         [
        {"role": "user", "content": "Give me a number of topics that could be good for an example of a database that students may work on. Get them froma  wide range of themes. Give me about 20 different ones."},
        ]

    template=[{"topic":"museums and artifacts"}, {"topic":"movies and actors"}]
    
    response = get_chat_completion_JSON(messages= messages, template=template)

    if response == None:
        return None
    
    output['themes']=response

    th = output['themes'][random.randint(0,len(output['themes']))]
    
    output['theme_selected']=th["topic"]
   

    return output


if __name__ == "__main__":
    print (theme_selector())
