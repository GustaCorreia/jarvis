from app.cognition.models.entity import Entity
from app.cognition.models.fact import Fact
from app.cognition.models.understanding import Understanding

thor = Entity(
    type="pet",
    value="Thor"
)

pet_category = Entity(
    type="category",
    value="pet"
)

fact = Fact(
    subject=thor,
    relation="is",
    object=pet_category
)

understanding = Understanding(
    intent="inform",
    entities=[thor, pet_category],
    facts=[fact],
    confidence=0.98
)

print(understanding)
