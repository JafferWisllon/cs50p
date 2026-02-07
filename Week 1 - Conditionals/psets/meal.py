def main():
    time = input("Give a hour: ").strip()
    meal_time = convert(time)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("breakfast time")

def convert(time):
    hour, minutes = time.split(":")
    return float(hour) + int(minutes) / 60

if __name__ == "__main__":
    main()