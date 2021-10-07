import csv
from collections import defaultdict

def process_log(csv_file):

    try:
        with open(csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # stores a dictionary with key: date and value: dictionary of key: cookie and value: number of occurences of that cookie
            cookie_logs = defaultdict(dict)

            for entry in reader:

                # takes the time only up until the 9th index since we just need the exact day of the cookie
                entry_time = entry[1][:10]
                cookie = entry[0]
                
                # increments the number of occurences from zero or from the current value 
                cookie_logs[entry_time][cookie] = cookie_logs[entry_time].get(cookie, 0) + 1 
        return(cookie_logs)
        
    except FileNotFoundError:
        return "You have entered an invalid file. Please try again..."
