from pyfsm_tool import FiniteStateMachine
# from lib import Opponent
# from lib_states import (
#     AskUserName, AskUserChoice1, AskUserRiddleWhisperingForest,
#     FightProcessWhisperingForest, AskUserGameRestart
# )

from data import data_story
from lib_states_story import Story

fsm: FiniteStateMachine = FiniteStateMachine()



# fsm.register_first_state(AskUserName(), "ask username")
for state_id, text in data_story[0].items():
    fsm.register_state(Story(text), state_id)


# fsm.register_state(AskUserChoice1(), "ask user choice 1")
# fsm.register_state(AskUserRiddleWhisperingForest(), "ask riddle wispering forest")
# fsm.register_state(FightProcessWhisperingForest(), "fight process")
# fsm.register_state(AskUserGameRestart(), "ask user game restart")



fsm.run()
