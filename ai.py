import requests

def get_news_details(api_key, topic, language='en', max_results=10):
    url = f'https://newsapi.org/v2/everything?q={topic}&language={language}&apiKey={api_key}'

    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data['status'] == 'ok':
            articles = news_data['articles']

            # Displaying detailed news for the given topic (limit to 10 titles)
            print(f"Top {min(max_results, len(articles))} News Titles Related to '{topic}':")
            print("="*80)

            for i, article in enumerate(articles[:max_results], 1):
                title = article['title']
                print(f"{i}. {title}")

        else:
            print("No news found for the given topic.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YOUR_ACTUAL_API_KEY' with your real News API key
api_key = 'a88d4c58d1e14c5a9bc03ea4c9c954b1'

# Get user input for the topic
user_topic = input("Enter the topic for detailed news: ")

get_news_details(api_key, user_topic)


