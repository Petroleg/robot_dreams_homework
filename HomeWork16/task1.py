import requests
import time
from threading import Thread
from multiprocessing import Process, Queue

dict_of_cities = {
    "Vyshhorod": {
        "latitude": 50.58,
        "longitude": 30.49
    },
    "Kyiv": {
        "latitude": 50.45,
        "longitude": 30.52
    },
    "Dubai": {
        "latitude": 25.08,
        "longitude": 55.31
    },
    "London": {
        "latitude": 51.51,
        "longitude": -0.13
    },
    "Katowice": {
        "latitude": 50.26,
        "longitude": 19.03
    }
}


def get_weather(city, latitude, longitude, result_queue):
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
        }
    )
    temperature = response.json()["hourly"]["temperature_2m"]
    average_temperature = round(sum(temperature) / len(temperature))
    result_queue.put((city, average_temperature))
    print(f"The weather in {city} is {average_temperature}")


def threading_function():
    result_queue_threading = Queue()
    threads = []
    start_time_threading = time.time()

    for city, coordinates in dict_of_cities.items():
        thread = Thread(target=get_weather,
                        args=(city, coordinates["latitude"], coordinates["longitude"], result_queue_threading))
        print(f">>>>>>>>>>>>>>>>>>>>>>>>> Start threading for {city}.")
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    exec_time_threading = time.time() - start_time_threading
    highest_avg_temp_threading = 0
    city_with_highest_temp_threading = ""

    while not result_queue_threading.empty():
        city, average_temperature = result_queue_threading.get()
        if average_temperature > highest_avg_temp_threading:
            highest_avg_temp_threading = average_temperature
            city_with_highest_temp_threading = city

    print(
        f"The city with the highest average temperature in threading mode is {city_with_highest_temp_threading} with a "
        f"temperature of {highest_avg_temp_threading}")
    print(f"Total execution time in threading mode: {exec_time_threading} seconds")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Threading ends here.\n")

    return exec_time_threading


def multiprocessing_function():
    result_queue_multiprocessing = Queue()
    processes = []
    start_time_multiprocessing = time.time()

    for city, coordinates in dict_of_cities.items():
        process = Process(target=get_weather,
                          args=(city, coordinates["latitude"], coordinates["longitude"], result_queue_multiprocessing))
        print(f">>>>>>>>>>>>>>>>>>>>>>>>> Start multiprocessing for {city}.")
        process.start()
        processes.append(process)


    for process in processes:
        process.join()

    exec_time_multiprocessing = time.time() - start_time_multiprocessing
    highest_avg_temp_multiprocessing = 0
    city_with_highest_temp_multiprocessing = ""

    while not result_queue_multiprocessing.empty():
        city, average_temperature = result_queue_multiprocessing.get()
        if average_temperature > highest_avg_temp_multiprocessing:
            highest_avg_temp_multiprocessing = average_temperature
            city_with_highest_temp_multiprocessing = city

    print(
        f"The city with the highest average temperature in multiprocessing mode is "
        f"{city_with_highest_temp_multiprocessing} with a temperature of {highest_avg_temp_multiprocessing}")
    print(f"Total execution time in multiprocessing mode: {exec_time_multiprocessing} seconds")
    print(">>>>>>>>>>>>>>>>>>>>>>>>> Multiprocessing ends here.\n")

    return exec_time_multiprocessing


if __name__ == '__main__':
    exec_time_threading = threading_function()
    exec_time_multiprocessing = multiprocessing_function()
    if exec_time_threading < exec_time_multiprocessing:
        print(f"Threading is {exec_time_multiprocessing - exec_time_threading} seconds faster than multiprocessing.")
    elif exec_time_threading > exec_time_multiprocessing:
        print(f"Multiprocessing is {exec_time_threading - exec_time_multiprocessing} seconds faster than threading.")
    else:
        print("Threading and multiprocessing have the same execution time.")
