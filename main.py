from openai import OpenAI
import requests
from fixture import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def curl_page(url: str) -> str:
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Return the text content of the response (HTML)
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None



def completion(html_code: str):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Provide a small summary of the terms and conditions from the HTML code below in simple, easy-to-understand language for university students. Highlight any unusual clauses: {html_code}"
            }
        ]
    )

    return completion



if __name__ == '__main__':
    page_html = curl_page("https://www.busbud.com/en-ca/bus-schedules-results/drceee/f244m6?outbound_date=2024-10-10&adults=1.html")
    completion = completion(page_html)
    print(completion.choices[0].message)


