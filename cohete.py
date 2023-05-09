def rocket_parts():
    print("payload, propellant, structure")


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


def days_to_complete(distance, speed):
    hours = distance / speed
    return hours / 24


days = days_to_complete(238855, 120)
print(days)
