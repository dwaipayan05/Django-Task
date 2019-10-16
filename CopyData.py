import csv
from friends.models import Names

with open('friends.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_counter = 0
    for row in csv_reader:
        a= Names()
        a.friend_name= row["name"]
        a.user_id = int(row["user_id"])
        a.longitude = float(row["longitude"])
        a.latitude = float(row["latitude"])
        a.save()


