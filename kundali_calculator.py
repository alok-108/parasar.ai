from pyswisseph import swe_set_ephe_path, swe_calc_ut, SEFLG_SWIEPH
import datetime

def generate_kundali(dob, time, place):
    # Combine date and time
    birth_datetime = datetime.datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")
    julian_day = birth_datetime.toordinal() + 1721425.5  # Julian day formula

    # Placeholder for ephemeris calculations
    planets = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    positions = {planet: swe_calc_ut(julian_day, idx, SEFLG_SWIEPH)[0] for idx, planet in enumerate(planets)}

    return {"date": dob, "time": time, "location": place, "positions": positions}
