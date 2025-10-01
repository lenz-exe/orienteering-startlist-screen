from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum


class EventType(str, Enum):
    INDIVIDUAL = "individual_event"
    MULTI_RACE = "multi-race_event"
    RELAY = "relay_event"
    TEAM = "team_event"


@dataclass
class Event:
    type: EventType


@dataclass
class Participant:
    last_name: str
    start_time: datetime
    class_name: str
    class_name_short: Optional[str] = None
    club_name_short: Optional[str] = None
    first_name: Optional[str] = None
    control_card: Optional[str] = None
    club_name: Optional[str] = None
    country: Optional[str] = None
    country_short: Optional[str] = None
    bib_number: Optional[str] = None
