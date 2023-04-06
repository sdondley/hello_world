from hello_world.hello_world import hello_world_function


def test_hello_world():
    assert hello_world_function() == "Hello, World!"
