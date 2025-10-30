from llm_provider import get_chat_completion

def table_format_html(table:str):
    output = {}
    messages =         [
            {"role": "system", "content": "I am going to give you stuff I need HTML formatted. When you respond do not give me any fluff, JUST the HTML"},
            {"role": "user", "content": "Here is a set of table. give them to me in HTML."},
            {"role": "user", "content": str(table)},
        ]
    
    response = get_chat_completion(messages= messages)
    #print (response.choices[0].message.content)
    return response.choices[0].message.content

def question_format_html(questions:str):
    output = {}
    messages =         [
            {"role": "system", "content": "I am going to give you stuff I need HTML formatted. When you respond do not give me any fluff, JUST the HTML"},
            {"role": "user", "content": "Here is a set of questions. give them to me in HTML."},
            {"role": "user", "content": str(questions)},
        ]
    
    response = get_chat_completion(messages= messages)
    #print (response.choices[0].message.content)
    return response.choices[0].message.content
