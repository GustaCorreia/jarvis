from app.cognition.location.location_mention import LocationMention
from app.cognition.location.location_type import LocationType


def test_create_location():
    mention = LocationMention(
        text="hospital",
        start=0,
        end=8,
        location_type=LocationType.PLACE,
    )

    assert mention.text == "hospital"
    assert mention.location_type == LocationType.PLACE
    assert mention.confidence == 1.0
