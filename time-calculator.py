def add_time(start, duration, start_day=None):
    if duration == "0:00":
        return start

    # extract parts from inputs to use for calculations
    start_parts = start.replace(" ", ":").split(":")
    start_h, start_m = int(start_parts[0]), int(start_parts[1])
    ending = start_parts[-1]
    dur_h, dur_m = map(int, duration.split(":"))

    # hours and minutes before time logic
    new_h = start_h + dur_h
    new_m = start_m + dur_m

    if new_m > 60:
        new_h += (new_m // 60)
        new_m = "{:02d}".format(new_m % 60)

    days_count = new_h // 24
    new_h = new_h % 24
    
    if new_h >= 12:
        if ending == 'PM':
            ending = 'AM'
            days_count += 1
        else:
            ending = 'PM'
        
        # avoid using 0 for hours (12 hour format)
        if new_h > 12: new_h -= 12

    new_time = f"{new_h}:{new_m} {ending}"
    if start_day:
        new_time += get_weekday(start_day,days_count)
    
    if days_count == 1:
        new_time += " (next day)"
    elif days_count > 1:
        new_time += f" ({days_count} days later)"

    return new_time

def get_weekday(start_day,increment):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_i = [w.lower() for w in weekdays].index(start_day.lower())
    new_i = (current_i + increment) % 7
    return f", {weekdays[new_i]}"

add_time('11:59 PM', '24:05')
add_time('11:59 PM', '24:05', 'Wednesday')
