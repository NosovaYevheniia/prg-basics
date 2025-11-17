def time_string(hours, minutes, time_format):
    if time_format == "24":
        return(f"{hours:02d}:{minutes:02d}")
    elif time_format == "12":
        if hours == 0:
            return(f"{time_format}:{minutes:02d} pm")
        elif hours < 12:
            return(f"{hours:02d}:{minutes:02d} am")
        else:
            return(f"{hours:02d}:{minutes:02d} pm")

print(time_string(12, 46, "12"))
print(time_string(0, 7, "12"))
print(time_string(8, 3, "24"))
