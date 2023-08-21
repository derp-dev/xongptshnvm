class Prompt(object):
    def __init__(self, **kwargs):
        self._data = kwargs

    def __str__(self) -> str:
        # Returns: A string representation of the prompt.
        return str(json.dumps(self._data))

    def __getattr__(self, attr: str) -> Any:
        """ Get an attribute of the prompt.
        Args:
            attr: The name of the attribute to get.
        Returns:
            The value of the attribute. """
        if attr == 'json':
            return json.loads(str(self))
        else:
            return getattr(self._data, attr)

    def __setattr__(self, attr: str, value: Any) -> None:
        """ Set an attribute of the prompt.
        Args:
            attr: The name of the attribute to set.
            value: The value to set the attribute to. """
        self._data[attr] = value


async def test_prompt() -> None:
    """Test the prompt class.
    Returns: None."""
    p = Prompt(name="gpt", version=4)
    assert len(p.json) > 0
    assert p.json != {}

test_prompt()