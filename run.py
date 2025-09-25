from booking.booking import Booking
import time

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.handle_popup()
    bot.change_currency(currency="USD")
    bot.place_to_go("California")
    bot.dates(checkin="2025-09-23",checkout="2025-09-30")
    bot.select_adults(count=10)
    bot.clicksearch()
    bot.apply_filtration()
    time.sleep(8)   
 
