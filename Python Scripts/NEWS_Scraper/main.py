import feedparser
import time

def get_news(source):
    rss_feeds = {
        'BBC': 'http://feeds.bbci.co.uk/news/rss.xml',
        'CNN': 'http://rss.cnn.com/rss/edition.rss',
        'Al Jazeera': 'http://www.aljazeera.com/xml/rss/all.xml'
    }

    feed_url = rss_feeds.get(source)
    if feed_url:
        feed = feedparser.parse(feed_url)

        print(f"Updates from {source}:")
        for entry in feed.entries[:5]:  # Displaying top 5 news items
            print(f"{entry.title}: {entry.link}")
    else:
        print(f"Invalid news source: {source}")

def main():
    while True:
        print("Select a news source:")
        print("1. BBC")
        print("2. CNN")
        print("3. Al Jazeera")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            get_news('BBC')
        elif choice == '2':
            get_news('CNN')
        elif choice == '3':
            get_news('Al Jazeera')
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        # Sleep for 15 minutes (900 seconds)
        time.sleep(900)

if __name__ == "__main__":
    main()
