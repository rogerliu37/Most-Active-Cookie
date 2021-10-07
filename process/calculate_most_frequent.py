def calculate_most_frequent(cookie_logs, day):

    try:
        max_value = max(cookie_logs[day].values())
        cookies = [] 
        
        # uses for loop to take account or the possibility of multiple cookies having the same frequency
        for cookie, frequency in cookie_logs[day].items():
            if frequency == max_value:
                cookies.append(cookie)
        return cookies

    except ValueError:
        return "You have entered an invalid date. Please try again..."