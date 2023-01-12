from src.dialog_manager.actions import *
from src.dialog_manager.states import allowed_actions, allowed_rooms


def verify_intent(action_inp, object_inp, location_inp):
    if object_inp in allowed_actions.keys():
        if action_inp in allowed_actions[object_inp]:
            if location_inp in allowed_rooms[object_inp]:
                return True, {"action": action_inp, "object": object_inp, "location": location_inp}
            else:
                return False, "wrong room specification for '{} {}'".format(action_inp, object_inp)
        else:
            return False, "wrong action for object {}".format(object_inp)
    else:
        return False, "none of the defined objects"

def manage_dialog(current_intent, states):
    prev_state = states.copy()
    for val in states.keys():
        prev_state[val] = states[val].copy()
    prompt = []

    if current_intent["action"] == 'change language':
        states, prompt = change_language_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("language has been changed")
    elif current_intent["action"] == 'activate':
        states, prompt = activate_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("{}: activated".format(current_intent['object']))
    elif current_intent["action"] == 'deactivate':
        states, prompt = deactivate_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("{}: deactivated".format(current_intent['object']))
    elif current_intent["action"] == 'increase':
        states, prompt = increase_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("{}: increased".format(current_intent['object']))
    elif current_intent["action"] == 'decrease':
        states, prompt = decrease_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("{}: decreased".format(current_intent['object']))
    elif current_intent["action"] == 'bring':
        states, prompt = bring_act(current_intent["object"], current_intent["location"], states, prompt)
        prompt.append("{} is brought".format(current_intent['object']))

    return states, prompt, prev_state

# current_intent_test = {'action': 'increase', 'object': 'volume', 'location': 'none'}
# states_main, prompt_main = manage_dialog(current_intent_test, states)
