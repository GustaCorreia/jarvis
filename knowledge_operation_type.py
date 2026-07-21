from enum import StrEnum


class KnowledgeOperationType(StrEnum):
    CREATE_NODE = "create_node"
    UPDATE_NODE = "update_node"
    CREATE_RELATIONSHIP = "create_relationship"
    UPDATE_RELATIONSHIP = "update_relationship"
