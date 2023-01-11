from src.dialog_manager.actions import *

def manage_dialog(current_intent, states):
    prev_state = states.copy()
    for val in states.keys():
        prev_state[val] = states[val].copy()
    prompt = []

    if current_intent["action"] == 'change language':
        states, prompt = change_language_act(current_intent["object"], current_intent["location"], states, prompt)
    elif current_intent["action"] == 'activate':
        states, prompt = activate_act(current_intent["object"], current_intent["location"], states, prompt)
    elif current_intent["action"] == 'deactivate':
        states, prompt = deactivate_act(current_intent["object"], current_intent["location"], states, prompt)
    elif current_intent["action"] == 'increase':
        states, prompt = increase_act(current_intent["object"], current_intent["location"], states, prompt)
    elif current_intent["action"] == 'decrease':
        states, prompt = decrease_act(current_intent["object"], current_intent["location"], states, prompt)
    elif current_intent["action"] == 'bring':
        states, prompt = bring_act(current_intent["object"], current_intent["location"], states, prompt)

    return states, prompt, prev_state

# current_intent_test = {'action': 'increase', 'object': 'volume', 'location': 'none'}
# states_main, prompt_main = manage_dialog(current_intent_test, states)
