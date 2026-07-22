from app.domain.world_model import WorldModel
from app.domain.entity import Entity
from app.domain.entity_type import EntityType
from app.domain.value_objects.entity_id import EntityId
from app.domain.value_objects.version import Version


def make_entity() -> Entity:
    return Entity(
        id=EntityId.generate(),
        entity_type=EntityType.PERSON,
        version=Version(),
    )


def test_world_starts_empty():
    world = WorldModel()

    assert world.entity_count == 0


def test_add_entity():
    world = WorldModel()
    entity = make_entity()

    world.add_entity(entity)

    assert world.entity_count == 1


def test_get_entity():
    world = WorldModel()
    entity = make_entity()

    world.add_entity(entity)

    assert world.get_entity(entity.id) == entity


def test_has_entity():
    world = WorldModel()
    entity = make_entity()

    world.add_entity(entity)

    assert world.has_entity(entity.id)


def test_remove_entity():
    world = WorldModel()
    entity = make_entity()

    world.add_entity(entity)

    world.remove_entity(entity.id)

    assert world.entity_count == 0


def test_clear_world():
    world = WorldModel()

    world.add_entity(make_entity())
    world.add_entity(make_entity())

    world.clear()

    assert world.entity_count == 0


def test_unknown_entity_returns_none():
    world = WorldModel()

    assert world.get_entity(EntityId.generate()) is None

from app.domain.relationship import Relationship
from app.domain.predicate import Predicate
from app.domain.value_objects.relationship_id import RelationshipId
from app.domain.value_objects.confidence import Confidence


def make_relationship(source, target):
    return Relationship(
        id=RelationshipId.generate(),
        source_entity=source.id,
        predicate=Predicate.OWNS,
        target_entity=target.id,
        confidence=Confidence(1.0),
        version=Version(),
    )


def test_add_relationship():
    world = WorldModel()

    owner = make_entity()
    pet = make_entity()

    world.add_entity(owner)
    world.add_entity(pet)

    relationship = make_relationship(owner, pet)

    world.add_relationship(relationship)

    assert world.relationship_count == 1


def test_find_relationships():
    world = WorldModel()

    owner = make_entity()
    pet = make_entity()

    world.add_entity(owner)
    world.add_entity(pet)

    relationship = make_relationship(owner, pet)

    world.add_relationship(relationship)

    relationships = world.find_relationships(owner.id)

    assert len(relationships) == 1
    assert relationships[0] == relationship

def test_neighbors():
    world = WorldModel()

    owner = make_entity()
    pet = make_entity()

    world.add_entity(owner)
    world.add_entity(pet)

    world.add_relationship(
        make_relationship(owner, pet)
    )

    neighbors = world.neighbors(owner.id)

    assert neighbors == [pet]


def test_degree():
    world = WorldModel()

    owner = make_entity()
    pet = make_entity()

    world.add_entity(owner)
    world.add_entity(pet)

    world.add_relationship(
        make_relationship(owner, pet)
    )

    assert world.degree(owner.id) == 1


def test_contains():
    world = WorldModel()

    entity = make_entity()

    world.add_entity(entity)

    assert world.contains(entity.id)


def test_entities_property():
    world = WorldModel()

    entity = make_entity()

    world.add_entity(entity)

    assert entity in world.entities


def test_relationships_property():
    world = WorldModel()

    owner = make_entity()
    pet = make_entity()

    world.add_entity(owner)
    world.add_entity(pet)

    relationship = make_relationship(owner, pet)

    world.add_relationship(relationship)

    assert relationship in world.relationships
