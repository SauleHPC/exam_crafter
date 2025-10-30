import aisuite as ai
import httpx

BASE_URL = "https://cci-llm.charlotte.edu/api/v1"
API_KEY="dummy"


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

if __name__ == "__main__":
    response = get_chat_completion(
        [
            {"role": "system", "content": "Respond in Pirate English."},
            {"role": "user", "content": "Tell me a joke."},
        ]
    )

    print (response.choices[0].message.content)
