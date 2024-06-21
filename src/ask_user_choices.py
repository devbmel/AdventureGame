from typing import List

from pyfsm_tool import StateBehaviour


class AskUserChoices(StateBehaviour):
    def __init__(self, intro_choice: str, user_choices: List[str]) -> None:
        super().__init__()
        self._intro_choice: str = intro_choice
        self._user_choices: List[str] = user_choices
        self._response_user: str = ""

    def action(self) -> None:
        print(self._intro_choice)
        print(
            f"{index_choice}) {user_choice}"
            for index_choice, user_choice in enumerate(self._user_choices, 1)
        )
        self._response_user = input("Your choice: ")

    def next_transition_id(self) -> str:
        if (
            not self._response_user.isnumeric() or
            int(self._response_user) not in range(
                1, len(self._user_choices) + 1
            )
        ):
            return "Error choice"
        return f"{int(self._response_user)}"
