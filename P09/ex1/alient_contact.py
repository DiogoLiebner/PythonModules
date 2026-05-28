from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime


class ContactType(Enum):
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    SIGNAL = "signal"
    RADIO = "radio"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=1, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=0, le=100)
    messsage_recieved: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_model(self) -> "AlienContact":
        if self.contact_type == ContactType.SIGNAL and self.signal_strength <= 0:
            raise ValueError("Signal strength must be greater than 0 for signal contacts.")
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.PHYSICAL and
                not self.is_verified):
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if (self.signal_strength > 7.0 and
                self.messsage_recieved is None):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    print("Valid contact created:")
    contact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        messsage_recieved="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    print(f"Contact ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal Strength: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.messsage_recieved}'")

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            contact_type=ContactType.TELEPATHIC,
            location="Unknown",
            signal_strength=8.0,
            duration_minutes=30,
            witness_count=0,
            is_verified=False,
        )
        print(f"Contact ID: {invalid_contact.contact_id}")
    except ValidationError as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    main()
