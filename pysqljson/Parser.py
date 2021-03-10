import states
import json
import regexs
import utilities
import exceptions


class Parser:
    state = states.STATE_START
    allowed_props = []
    operators = ['=', '<', '<=', '>', '>=', '!=', '..', 'in', 'like']

    # def parse_combinators(self, combs):

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
                return ''
        elif regexs.regex_neq(operator):
            if utilities.is_str(key) or utilities.is_num(key):
                return ''
        elif regexs.regex_le(operator):
            if utilities.is_num(key):
                return ''
        elif regexs.regex_lt(operator):
            if utilities.is_num(key):
                return ''
        elif regexs.regex_ge(operator):
            if utilities.is_num(key):
                return ''
        elif regexs.regex_gt(operator):
            if utilities.is_num(key):
                return ''
        elif regexs.regex_bt(operator):
            if utilities.is_list(key):
                return ''
        elif regexs.regex_in(operator):
            if utilities.is_list(key):
                return ''
        elif regexs.regex_like(operator):
            if utilities.is_str(key):
                return ''
        else:
            raise exceptions.ERROR_INVALID_KEY_FOR_OPERATOR_STATE
        raise exceptions.ERROR_INVALID_VAL_FOR_OPERATOR

    def _state_transition(self, key):
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

    def parse(self, json_str, allowed_props):
        if not utilities.is_str(json_str):
            raise exceptions.ERROR_PASS_PARSE_STRING
        if not utilities.is_list(allowed_props):
            raise exceptions.ERROR_PASS_PARSE_LIST
        for prop in allowed_props:
            if not utilities.is_str(prop):
                raise exceptions.ERROR_ALLOWED_PROPS_MUST_BE_STRING

        self.allowed_props = allowed_props
        jsn = json.loads(json_str)
        self._parse(jsn)

    def _parse(self, jsn):
        keys = list(jsn.keys())
        while len(keys) > 0:
            key = keys.pop()
            self._state_transition(key)
