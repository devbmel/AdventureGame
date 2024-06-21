from pyfsm_tool import FiniteStateMachine

from .src.ask_user_choices import AskUserChoices
from .data.data_variables import data_story, parameters_user_choices
from .src.story import Story


fsm: FiniteStateMachine = FiniteStateMachine()

for state_id, text in data_story[0].items():
    fsm.register_state(Story(text), state_id)

for state_id, parameters in parameters_user_choices.items():
    fsm.register_state(AskUserChoices(*parameters), state_id)

fsm.run()
