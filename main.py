import random
import schedule
import time
from plyer import notification
# quotes = ["I am a progammer, I have a life", "There are times when a man feels emotional, and when he should embrace it or to let it go", "it is frustating when you ask the right questions with no answers", ]


quotes = {
    "motivation": [
                    "Stay convicted to your beliefs, and never let anyone tell you otherwise", "When everything seems to crumbling down around you, that is the moment of opportunity to pivot and build yourself up on new foundation",
                    "When you lose your precious friends, you will find new ones that will be more valuable than the ones you lost"
                  ],

    "life":       [
                    "Life is a journey, and you are the driver of your own destiny", "Life is a game, and you are the player, play it well", "Life is a gift, and you are the recipient, cherish it"
                  ],

    "programming": [
                    "Programming is a skill, and you are the master of your own craft", "Programming is a language, and you are the speaker of your own words", "Programming is a tool, and you are the creator of your own world"
                   ],

    "love":
                   [
                    "Loving with all your heart is never a mistake, but showing too much love can be a disaster and unrequited", "Love is a feeling, and you are the one who feels it and not the other", "Love is a gift, and you are the one who gives it but the timing is crucial"
                   ]

    
}

# while True:
#     category = input("what category do you want to hear from (Motivation, life, Programming, Love):\n").lower()
#     if category in quotes:
#         print(random.choice(quotes[category]))
#     else:
#         print("Invalid category, please try again\n")
#         print(random.choice(random.choice(list(quotes.values()))))
#         break
# Function to display a daily quote
# Function to display a daily quote as a notification
def show_daily_quote():
    quote = random.choice(quotes["motivation"])
    notification.notify(
        title="🌟 Daily Motivation 🌟",
        message=quote,
        app_name="Motivation Quotes",
        timeout=10  # Notification stays for 10 seconds
    )

# Schedule the notification
schedule.every().day.at("08:00").do(show_daily_quote)


# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
