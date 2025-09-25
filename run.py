from booking.booking import Booking
import time
# 1 way to instantiate the class
# bot=Booking()
# bot.land_first_page()


#2 way to instantiate it butwith exit method
# jese hi indentation s bhr aega exit apne aap chl jaega
#her ethe bot is treated as context manager in which exit is run automatically after the indentation ends
with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.handle_popup()
    bot.change_currency(currency="USD")
    bot.place_to_go("California")
    bot.dates(checkin="2025-09-23",checkout="2025-09-30")
    bot.select_adults(count=10)
    bot.clicksearch()
    bot.apply_filtration()
    time.sleep(8)   #8 sec rukega close hone s pehle
 