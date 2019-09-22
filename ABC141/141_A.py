def main():

    weather_tuple = ("Sunny", "Cloudy", "Rainy")

    S = input()

    for i, weather in enumerate(weather_tuple):
        if S == weather:
            print(weather_tuple[(i + 1) % 3])

if __name__ == "__main__":
    main()