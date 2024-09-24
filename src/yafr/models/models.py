from pydantic import BaseModel


class Series(BaseModel):
    fred_id: str
    realtime_start: str
    realtime_end: str
    title: str
    observation_start: str
    observation_end: str
    frequency: str
    frequency_short: str
    units: str
    units_short: str
    seasonal_adjustment: str
    seasonal_adjustment_short: str
    last_updated: str
    popularity: int
    notes: str
