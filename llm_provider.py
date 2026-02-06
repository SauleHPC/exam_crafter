import aisuite as ai
import httpx
import json
import traceback

#BASE_URL = "https://cci-llm.charlotte.edu/api/v1"
BASE_URL = "http://localhost:1234/v1"
API_KEY="dummy"

debug = False

def get_chat_completion(messages):
    provider_configs = {
        "openai": {
            "base_url": BASE_URL,
            "api_key": API_KEY,
            "http_client": httpx.Client(verify=False) 
        }
    }
    client = ai.Client( provider_configs =provider_configs )

    real_model = "Llama-3.3-70B-Instruct"
    modelparam = "openai:"+real_model

    response = client.chat.completions.create(
        model=modelparam,
        messages=messages
    )
    return response

def _validate(content_str, template):
    try:
        obj = json.loads(content_str)

        if isinstance(template, dict):
            for x in template:
                obj[x] #tried to generate an exception if malformed
        if isinstance(template, list):
            #checking each object like the first one
            for a in obj:
                #print (a)
                for x in template[0]:
                    a[x] #tried to generate an exception if malformed            
    except Exception as e:
        print (f"cant parse as JSON {content_str}")
        #traceback.print_exc()
        obj = None
    return obj


def get_chat_completion_JSON(messages, template) -> dict:
    #This returns the object decoded from the answer or None if it can't do that
    #This does basic checks that the generated JSON follows the structure provided
    format_message = {"role": "system", "content": f"Provide the answer as a JSON object that follows the following format. Use the exact same fields: {json.dumps(template)}"}
    local_message = [*messages, format_message]

    nbtry = 3
    obj = None
    response = get_chat_completion(local_message)

    content_str = response.choices[0].message.content
    if debug:
        print (f"Received: {content_str}")    
        
    obj = _validate(content_str, template)
            
    if obj == None: #validation failed
        if debug:
            print ("Trying to cleanup")
        reformat_message = [
            {"role": "system", "content": f"You are about to receive a message. Reformat it as a JSON object that follows this format: {json.dumps(template)}"},
            {"role": "system", "content": content_str}
        ]
        response = get_chat_completion(local_message)

        content_str = response.choices[0].message.content
        if debug:
            print (f"Received: {content_str}")    
            
        obj = _validate(content_str, template)
        if debug:
            if obj == None:
                print ('cleanup failed')
            else:
                print ('cleanup success')
    
    return obj

if __name__ == "__main__":
    response = get_chat_completion(
        [
            {"role": "system", "content": "Respond in Pirate English."},
            {"role": "user", "content": "Tell me a joke."},
        ]
    )

    print (response.choices[0].message.content)
