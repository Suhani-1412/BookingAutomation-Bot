# BookingAutomation-Bot

Booking Automation Bot 

A Python-based automation bot using Selenium that searches and filters hotels on Booking.com. Built as a learning project to practice OOP, Selenium automation, and dynamic interaction with websites.

📌 Features

Opens Booking.com and handles pop-ups automatically.

Changes currency to desired value (e.g., USD).

Searches for hotels in a specified location.

Selects check-in and check-out dates.

Configures number of adults for booking.

Applies filters like star rating and price sorting.

Demonstrates OOP-based structure for modular, reusable automation.

🛠️ Tech Stack

Python 3

Selenium – browser automation

WebDriverWait & Expected Conditions – dynamic element handling

📂 Project Structure
bot/
│── booking/
│    ├── booking.py          # main bot class (Chrome driver wrapper)
│    ├── booking_filter.py   # filtration methods
│    └── constant.py         # constants (e.g., BASE_URL)
│── run.py                   # script to run the bot
│── requirements.txt         # dependencies
│── README.md                # this documentation

⚡ How It Works

Instantiate the Booking class using a context manager:

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.handle_popup()
    bot.change_currency("USD")
    bot.place_to_go("California")
    bot.dates("2025-09-23", "2025-09-30")
    bot.select_adults(count=10)
    bot.clicksearch()
    bot.apply_filtration()


The bot performs all actions automatically, then exits and closes the browser (if teardown=True).

The filtration class (BookingFiltration) handles star ratings and price sorting using Selenium.


📝 Future Improvements

Add email notification for top hotels or filtered results.

Allow dynamic date calculation (e.g., 3 months from today).

Save results to a CSV or database for further analysis.
