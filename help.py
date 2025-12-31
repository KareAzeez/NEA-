import csv 
from TicketClass import TicketCategory, Topup

# Creates a topup 
mytopup = Topup("5209d259-0bd8-451d-93f3-d11c9366d98b", 
                "Academic Year tickets for school-college and university students", 
                "NTU Academic Year 2025/6", 
                29900, 
                "student"
                )

print(mytopup.title)
print(mytopup.getPriceinPoundsAndPence())

userName = input("What is your name? ")
# using a dict writer 
data = [
    {"TicketName": mytopup.title,
     "price": mytopup.getpriceinPoundsandPence,
     "userName": userName}
]
# purchased ticket csv is an empty file to save purchased tickets . create an empty csv file 
with open("PurchasedTickets.csv", "a") as csvfile:
    fieldNames = ["TicketName","price", "userName"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
    writer.writeheader()
    writer.writerows(data)





