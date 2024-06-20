from pyfsm_tool import StateBehaviour


class Story(StateBehaviour):
    def __init__(self, story: str) -> None:
        super().__init__()
        self._story: str = story

    def action(self) -> None:
        print(self._story)
