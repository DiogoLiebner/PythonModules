from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "Cadet"
    OFFICER = "Officer"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    COMMANDER = "Commander"


class SpaceCrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[SpaceCrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_model(self) -> "SpaceMission":
        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission ID must start with 'M'")
        if self.crew and len(self.crew) > 0:
            for member in self.crew:
                if member.is_active is False:
                    raise ValueError(
                        f"Crew member {member.name} is not active and cannot be assigned to a mission"
                    )
        if self.crew[0].rank != Rank.COMMANDER and \
                self.crew[0].rank != Rank.CAPTAIN:
            raise ValueError(
                "The crew must have a Commander or Captain"
            )
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience < 5:
                    raise ValueError(
                        f"Missions longer than 1 year require crew "
                        f"with 5+ years experience. "
                        f"{member.name} has {member.years_experience} years."
                    )
        return self


def main() -> None:
    print("Space Crew and Mission Validation")
    print("========================================")
    print("Valid crew member created:")
    sarah_connor = SpaceCrewMember(
        member_id="SC001",
        name="John Doe",
        rank=Rank.COMMANDER,
        age=35,
        specialization="Mission Command",
        years_experience=10,
        is_active=True
    )
    john_smith = SpaceCrewMember(
        member_id="SC002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=40,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )
    alice_johnson = SpaceCrewMember(
        member_id="SC003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=38,
        specialization="Engineering",
        years_experience=12,
        is_active=True
    )
    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2025, 7, 20),
        duration_days=900,
        crew=[sarah_connor, john_smith, alice_johnson],
        mission_status="planned",
        budget_millions=2500.0
    )
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Crew Size: {len(space_mission.crew)}")
    print(f"Crew Members: \n{[member.name for member in space_mission.crew]}")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_crew_member = SpaceCrewMember(
            member_id="SC002",
            name="Jane Smith",
            rank=Rank.CADET,
            age=25,
            specialization="Engineer",
            years_experience=2,
            is_active=False
        )
        print(f"Crew Rank: {invalid_crew_member.rank}")
    except ValidationError as e:
        print(f"Expected validation error: {e}\nMission must have atleast \
one Commander or Captain")


if __name__ == "__main__":
    main()
