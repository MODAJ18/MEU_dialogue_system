from src.dialog_manager.states import allowed_states

def change_language_act(object_, location_, states, prompt):
    if location_ != "none":
        prompt.append("specifying location for language change is not necessary")
        location_ = "none"
    if object_ == "none" or object_ == "English":
        states["chinese"][location_] = "off"
        states["korean"][location_] = "off"
        states["german"][location_] = "off"
        states["english"][location_] = "on"
    elif object_ == "Chinese":
        states["chinese"][location_] = "on"
        states["korean"][location_] = "off"
        states["german"][location_] = "off"
        states["english"][location_] = "off"
    elif object_ == "Korean":
        states["chinese"][location_] = "off"
        states["korean"][location_] = "on"
        states["german"][location_] = "off"
        states["english"][location_] = "off"
    elif object_ == "German":
        states["chinese"][location_] = "off"
        states["korean"][location_] = "off"
        states["german"][location_] = "on"
        states["english"][location_] = "off"
    else:
        prompt.append("wrong prompt! please clarify which language are you referring to, \
        {} language is not available".format(object_))
    return states, prompt


def activate_act(object_, location_, states, prompt):
    if object_ == "music":
        if location_ != "none":
            prompt.append("specifying location for music activation is not necessary")
            location_ = "none"
        states[object_][location_] = "on"
    elif object_ == "lights":
        if location_ in states[object_].keys():
            states[object_][location_] = "on"
        else:
            prompt.append("you specified a wrong location, please try again")
    elif object_ == "lamp":
        if location_ != "none":
            prompt.append("specifying location for lamp activation is not necessary")
            location_ = "none"
        states[object_][location_] = "on"
    else:
        prompt.append("wrong prompt! please clarify which object are you referring to, \
        {} object is not available".format(object_))
    return states, prompt


def deactivate_act(object_, location_, states, prompt):
    if object_ == "music":
        if location_ != "none":
            prompt.append("specifying location for music activation is not necessary")
            location_ = "none"
        states[object_][location_] = "off"
    elif object_ == "lights":
        if location_ in states[object_].keys():
            states[object_][location_] = "off"
        else:
            prompt.append("you specified a wrong location, please try again")
    elif object_ == "lamp":
        if location_ != "none":
            prompt.append("specifying location for lamp activation is not necessary")
            location_ = "none"
        states[object_][location_] = "off"
    else:
        prompt.append(
            "wrong prompt! please clarify which object are you referring to, {} object is not available".format(
                object_))
    return states, prompt


def increase_act(object_, location_, states, prompt):
    if object_ == "volume":
        if location_ != "none":
            prompt.append("specifying location for volume is not necessary")
            location_ = "none"
        loc_state = allowed_states[object_].index(states[object_][location_])
        increase = min(loc_state + 1, len(allowed_states[object_]) - 1)
        states[object_][location_] = str(increase)
    elif object_ == "heat":
        if location_ in states[object_].keys():
            loc_state = allowed_states[object_].index(states[object_][location_])
            increase = min(loc_state + 1, len(allowed_states[object_]) - 1)
            states[object_][location_] = str(increase)
        else:
            prompt.append("you specified a wrong location, please try again")
    return states, prompt


def decrease_act(object_, location_, states, prompt):
    if object_ == "volume":
        if location_ != "none":
            prompt.append("specifying location for volume is not necessary")
            location_ = "none"

        loc_state = allowed_states[object_].index(states[object_][location_])
        decrease = max(loc_state - 1, 0)
        states[object_][location_] = str(decrease)
    elif object_ == "heat":
        if location_ in states[object_].keys():
            loc_state = allowed_states[object_].index(states[object_][location_])
            decrease = max(loc_state - 1, 0)
            states[object_][location_] = str(decrease)
        else:
            prompt.append("you specified a wrong location, please try again")
    return states, prompt


def bring_act(object_, location_, states, prompt):
    newspaper, juice, socks, shoes
    if object_ == "newspaper":
        if location_ != "none":
            prompt.append("specifying location for bringing newspaper is not necessary")
            location_ = "none"
        states[object_][location_] = "brought"
    elif object_ == "juice":
        if location_ != "none":
            prompt.append("specifying location for bringing juice is not necessary")
            location_ = "none"
        states[object_][location_] = "brought"
    elif object_ == "socks":
        if location_ != "none":
            prompt.append("specifying location for bringing socks is not necessary")
            location_ = "none"
        states[object_][location_] = "brought"
    elif object_ == "shoes":
        if location_ != "none":
            prompt.append("specifying location for bringing shoes is not necessary")
            location_ = "none"
        states[object_][location_] = "brought"
    else:
        prompt.append("wrong prompt! please clarify which object are you referring to, \
        {} object is not available".format(object_))
    return states, prompt