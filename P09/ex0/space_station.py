from pydantic import BaseModel, Field, ValidationError
import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    location: str = Field(min_length=1, max_length=100)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime.datetime = Field(
        default_factory=datetime.datetime.now
    )
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=100)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        location="Low Earth Orbit",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational=True
    )
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Location: {station.location}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last Maintenance: {station.last_maintenance}")
    if station.is_operational is True:
        print("Status: Operational")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            location="Low Earth Orbit",
            crew_size=50,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True
        )
        print(f"ID: {invalid_station.station_id}")
    except ValidationError as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    main()
