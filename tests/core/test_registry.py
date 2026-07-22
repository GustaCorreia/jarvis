from app.core.registry import Registry


class StringRegistry(Registry[str]):

    def key_for(self, item: str) -> str:
        return item


def test_register_item():

    registry = StringRegistry()

    registry.register("hello")

    assert registry.get("hello") == "hello"


def test_exists():

    registry = StringRegistry()

    registry.register("abc")

    assert registry.exists("abc")


def test_contains():

    registry = StringRegistry()

    registry.register("abc")

    assert "abc" in registry


def test_length():

    registry = StringRegistry()

    registry.register("a")
    registry.register("b")

    assert len(registry) == 2


def test_iteration():

    registry = StringRegistry()

    registry.register("a")
    registry.register("b")

    assert tuple(registry) == ("a", "b")


def test_keys():

    registry = StringRegistry()

    registry.register("x")

    assert registry.keys() == ("x",)


def test_values():

    registry = StringRegistry()

    registry.register("x")

    assert registry.values() == ("x",)


def test_items():

    registry = StringRegistry()

    registry.register("x")

    assert registry.items() == (("x", "x"),)


def test_remove():

    registry = StringRegistry()

    registry.register("x")

    registry.remove("x")

    assert len(registry) == 0


def test_clear():

    registry = StringRegistry()

    registry.register("a")
    registry.register("b")

    registry.clear()

    assert len(registry) == 0
