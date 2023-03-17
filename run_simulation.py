import datetime
import sys


from consumers import HomeAssistantET340Consumer
from producers import GridProducer



def main() -> int:
    print("ss")

    grid = GridProducer()
    house = HomeAssistantET340Consumer()
    
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=5)

    while end_time < datetime.datetime.now() + datetime.timedelta(minutes=10):
        consumed = house.getConsumption(start_time, end_time)
        imported = grid.getProduction(start_time, end_time, consumption=consumed)


        print(f"{start_time} -> {end_time}")
        print(f"Consumed: {consumed}")
        print(f"Imported from grid: {imported}")

        start_time = end_time
        end_time = end_time + datetime.timedelta(seconds=5)



if __name__ == '__main__':
    sys.exit(main())  # use to return the exitcode. Do not return strings as they are expected as string