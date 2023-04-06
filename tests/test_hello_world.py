from hello_world.hello_world import hello_world_function, goodbye_world


def test_hello_world():
    assert hello_world_function() == "Hello, World!"


def test_hello_world():
    assert goodbye_world() == "Goodbye, World!"
