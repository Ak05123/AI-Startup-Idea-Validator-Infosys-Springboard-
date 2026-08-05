from state.schema import StartupState


def update_state(

    state: StartupState,

    key: str,

    value

):

    state[key] = value

    return state


def get_state(

    state: StartupState,

    key: str

):

    return state.get(key, "")