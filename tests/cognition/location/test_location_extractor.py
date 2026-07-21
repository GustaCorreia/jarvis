from app.cognition.location.location_extractor import LocationExtractor
from app.cognition.location.location_type import LocationType


def test_process_place():
    extractor = LocationExtractor()

    mentions = extractor.process("Estou em casa.")

    assert len(mentions) == 1
    assert mentions[0].text.lower() == "casa"
    assert mentions[0].location_type == LocationType.PLACE


def test_process_organization():
    extractor = LocationExtractor()

    mentions = extractor.process("Estudo na UNINOVE.")

    assert len(mentions) == 1
    assert mentions[0].text.lower() == "uninove"
    assert mentions[0].location_type == LocationType.ORGANIZATION


def test_process_none():
    extractor = LocationExtractor()

    mentions = extractor.process("Hoje está chovendo.")

    assert mentions == []
