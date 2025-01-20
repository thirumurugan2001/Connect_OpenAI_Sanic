import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import requests

# Connect with OpenAI API and get the response.
def openai(req_body):
    try :
        Question=req_body['Question']
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.environ["GITHUB_TOKEN"],
        )
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {
                    "role": "user",
                    "content": Question,
                }
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )

        return(response.choices[0].message.content)
    except Exception as e:
         return {
                "Error":str(e),
                "statusCode":500
            } 


# Connect with Google Search API and get the response.
def get_google_serp_results(req_body):
    try:
        Question=req_body['Question']
        location="United States"
        language="en", 
        num_results=10
        api_key=os.getenv("SERP_API_KEY")
        url = "https://serpapi.com/search"
        params = {
            "q": Question,
            "location": location,
            "hl": language,
            "num": num_results,
            "api_key": api_key
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return {
                "Error":str(e),
                "statusCode":500
            }



