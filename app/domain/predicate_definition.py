from dataclasses import dataclass

from app.domain.value_type import ValueType


@dataclass(frozen=True, slots=True)
class PredicateDefinition:
    """
    Descreve as características de um predicado.

    Exemplos:
        name
        nickname
        weight
        birth_date
    """

    name: str

    value_type: ValueType

    multiple: bool

    keep_history: bool

    description: str = ""
