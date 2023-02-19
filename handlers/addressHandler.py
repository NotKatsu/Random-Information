import random 
import handlers.informationHandler as informationHandler

def randomAddress(amount: int) -> list[str]: 
    addresses = []
    for i in range(amount):
        position = random.randint(1, len(informationHandler.addressList))
        houseNum = random.randint(1, 600)

        addresses.append(f"{houseNum} {informationHandler.addressList[position]}")

    return addresses

