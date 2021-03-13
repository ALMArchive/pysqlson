import json
from pysqljson import states, utilities, exceptions, StateManager, consts


class Parser:
    operators = consts.OPERATORS
    manager = StateManager.StateManager([], operators)
    current_operator = None
    query = None

    def parse(self, query, json_str, allowed_props):
        if not utilities.is_str(json_str):
            raise exceptions.ERROR_PASS_PARSE_STRING
        if not utilities.is_list(allowed_props):
            raise exceptions.ERROR_PASS_PARSE_LIST
        for prop in allowed_props:
            if not utilities.is_str(prop):
                raise exceptions.ERROR_ALLOWED_PROPS_MUST_BE_STRING

        self.manager = StateManager.StateManager(allowed_props, self.operators)
        jsn = json.loads(json_str)
        self._parse(jsn)

    def _process_operator(self, jsn, key):
        self.current_operator = key
        self._parse(jsn[key])

    def _process_val(self, jsn, key):
        print('process_val')
        print(jsn)
        print(key)
        if self.current_operator is None:
            raise exceptions.ERROR_INVALID_CURRENT_OPERATOR

    def _process_key(self, jsn, key):
        current_state = self.manager.get_state()
        if current_state == states.STATE_START:
            return;
        elif current_state == states.STATE_AND:
            self._parse(jsn[key])
        elif current_state == states.STATE_OR:
            self._parse(jsn[key])
        elif current_state == states.STATE_PROP:
            self._parse(jsn[key])
        elif current_state == states.STATE_OPERATOR:
            self._process_operator(jsn, key)
        elif current_state == states.STATE_VAL:
            self._process_val(jsn, key)
        else:
            raise exceptions.ERROR_INVALID_STATE

    def _parse(self, jsn):
        if utilities.is_dict(jsn):
            keys = list(jsn.keys())
        else:
            keys = [jsn]
        while len(keys) > 0:
            key = keys.pop()
            self.manager.transition(key)
            self._process_key(jsn, key)
