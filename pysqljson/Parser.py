import json
from pysqljson import states, utilities, exceptions


class Parser:
    state = states.STATE_START
    allowed_props = []

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
