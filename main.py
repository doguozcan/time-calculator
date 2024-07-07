def add_time(start, duration, starting_day=""):
    # add the days of the week array
    day_names = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    # get star time and format
    start_time, start_format = start.split(" ")

    # get start hour and start minute
    start_hour, start_minute = map(int, start_time.split(":"))

    # get the duration hour and minute
    duration_hour, duration_minute = map(int, duration.split(":"))

    # 3PM -> 15:00
    # 9PM -> 21:00
    if start_format == "PM":
        start_hour += 12

    # calculate total hours
    hours = start_hour + duration_hour

    # calculate total minutes
    minutes = start_minute + duration_minute

    # variable for the final format AM or PM
    format = ""

    # if the minute variable is more than 60, add it as an hour and turn it into a form less than 60
    hours += minutes // 60
    minutes = minutes % 60

    # calculate how many days passed
    days = hours // 24

    # if hour if greater than 24 return it to its original form
    hours = hours % 24

    # if hour is more than 12 its format is going to be pm else am
    if hours >= 12:
        format = "PM"
        # if hour is not 12 subtract 12
        if hours != 12:
            hours -= 12
    else:
        format = "AM"
        # if hour is 0 make it 12
        if hours == 0:
            hours = 12

    # 1:1 -> 1:01
    if minutes < 10:
        minutes = "0" + str(minutes)

    # add time
    message = str(hours) + ":" + str(minutes) + " " + format

    # get the starting day and make it all lowercase
    starting_day = starting_day.lower()

    # if starting day is present
    if starting_day:
        # add the day name
        message += (
            ", " + day_names[(day_names.index(starting_day) + days) % 7].capitalize()
        )

    # if only one day is passed declare it as next day
    if days == 1:
        message += " (next day)"
    # if more than one day is passed declare it as the day count
    elif days > 1:
        message += f" ({days} days later)"

    # finally return the message
    return message
