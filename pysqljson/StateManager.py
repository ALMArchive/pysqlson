from pysqljson import states, utilities, exceptions, regexs


class StateManager:
    state = states.STATE_START
    state_stack = []
    allowed_props = []

    def __init__(self, allowed_props):
        self.allowed_props = allowed_props

    def _start_transition(self, key):
        if regexs.regex_and(key):
            self.state = states.STATE_AND
        elif regexs.regex_or(key):
            self.state = states.STATE_OR
        elif utilities.includes(self.allowed_props, key):
            self.state = states.STATE_PROP
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_START_STATE

    def _and_transition(self, key):
        if utilities.includes(self.allowed_props, key):
            self.state = states.STATE_PROP
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_AND_STATE

    def _or_transition(self, key):
        if utilities.includes(self.allowed_props, key):
            self.state = states.STATE_PROP
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_OR_STATE

    def _prop_transition(self, key):
        if utilities.includes(self.operators, key):
            self.state = states.STATE_OPERATOR
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_PROP_STATE

    def _operator_transition(self, operator, key):
        if regexs.regex_eq(operator):
            if utilities.is_str(key) or utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_neq(operator):
            if utilities.is_str(key) or utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_le(operator):
            if utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_lt(operator):
            if utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_ge(operator):
            if utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_gt(operator):
            if utilities.is_num(key):
                self.state = states.STATE_VAL
        elif regexs.regex_bt(operator):
            if utilities.is_list(key):
                self.state = states.STATE_VAL
        elif regexs.regex_in(operator):
            if utilities.is_list(key):
                self.state = states.STATE_VAL
        elif regexs.regex_like(operator):
            if utilities.is_str(key):
                self.state = states.STATE_VAL
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_OPERATOR_STATE
        raise exceptions.ERROR_INVALID_VAL_FOR_OPERATOR

    def pop_state(self):
        if len(self.state_stack) == 0:
            raise exceptions.ERROR_NO_STATE_TO_POP
        self.state = self.state_stack.pop()

    def transition(self, key):
        self.state_stack.insert(0, key)
        if self.state == states.STATE_START:
            self._start_transition(key)
        elif self.state == states.STATE_AND:
            self._and_transition(key)
        elif self.state == states.STATE_OR:
            self._and_transition(key)
        elif self.state == states.STATE_PROP:
            self._prop_transition(key)
        else:
            raise exceptions.ERROR_INVALID_STATE
