months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        prompt = input("Date: ").strip()

        if "/" in prompt:
            month, day, year = prompt.split("/")
            month = int(month)
            day = int(day)
        else:
            month_str, day, year = prompt.replace(",", "").split(" ")
            month = months.index(month_str) + 1
            day = int(day)
        
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
        
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass