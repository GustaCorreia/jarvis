from app.cognition.location.location_type import LocationType


def test_location_type_values():
    assert LocationType.PLACE.value == "place"
    assert LocationType.ORGANIZATION.value == "organization"
    assert LocationType.UNKNOWN.value == "unknown"
