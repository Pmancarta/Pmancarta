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


def generate_report(internal_tank, external_tank, hidrogen):
    output = f"""Fuel report
    Internal Tank = {internal_tank}
    External Tank = {external_tank}
    Hidrogen      = {hidrogen}"""
    print(output)


generate_report(50, 30, 70)

from datetime import timedelta, datetime


def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")


gatos = arrival_time()
print(gatos)
import datetime

# Obtener la fecha actual
date = datetime.datetime.now()

# Formatear la fecha en el formato deseado
date_formatted = date.strftime("%a %d %b %Y, %I:%M%p")

# Imprimir la fecha formateada
print(date_formatted)


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


crew_members(
    captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"
)


def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")


fuel_report(main=50, external=100, emergency=60)
