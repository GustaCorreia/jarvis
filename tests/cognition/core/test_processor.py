from app.cognition.core.processor import Processor


def test_processor_cannot_be_instantiated():
    try:
        Processor()
        assert False
    except TypeError:
        assert True
