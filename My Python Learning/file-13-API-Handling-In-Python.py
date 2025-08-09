# used https://api.freeapi.app/ for radnom API's

import requests
import random

# 1.----------------------------------------------------------------------------------------------------
def fetch_random_qoute():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response = requests.get(url)
    data = response.json()

    if data["success"] and 'data' in data:
        quotes_list = data["data"]["data"]
        random_index = random.randint(0, len(quotes_list) - 1)
        qoute_data = quotes_list[random_index]
        qoute = qoute_data["content"]
        return random_index, qoute
    else:
        raise Exception("Failed to fetch")

def main():
    try:
        index, qoute = fetch_random_qoute()
        print(f"Today's Quote (Index {index}): {qoute} \n")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

# 2.----------------------------------------------------------------------------------------------------
def fetch_quote_with_tags():
    random_id = random.randint(1, 300) 
    url = f"https://api.freeapi.app/api/v1/public/quotes/{random_id}"
    response = requests.get(url)
    data = response.json()

    if data["success"] and 'data' in data:
        quote = data["data"]["content"]
        quote_tags = data["data"]["tags"]
        
        formatted_tags = ", ".join(quote_tags)
        print(f"\nQuote: {quote}")
        print(f"The quote is about {{{formatted_tags}}}\n")
    else:
        print(f"Failed to fetch quote with ID {random_id}.")

fetch_quote_with_tags()