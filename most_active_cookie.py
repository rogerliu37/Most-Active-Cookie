import sys
from process.process_log import * 
from process.calculate_most_frequent import *


"""
Main function that gets the processed cookie logs and calculates the most frequent cookies.
"""
if __name__ == "__main__":
    cookie_logs = process_log(sys.argv[1])

    # only calculates most frequent if its a valid log
    if isinstance(cookie_logs,dict):
        most_frequent_cookies = calculate_most_frequent(cookie_logs, sys.argv[-1])
        
        # only prints the result if no error
        if isinstance(most_frequent_cookies, list):
            for cookie in most_frequent_cookies:
                print(cookie)
        else:
            print(most_frequent_cookies)
    else:
        print(cookie_logs)
    

