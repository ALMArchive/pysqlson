import unittest
from pysqljson import StateManager, states, exceptions
from pysqljson import consts


class TestStateManager(unittest.TestCase):
    def test_start_state(self):
        sm = StateManager.StateManager([], consts.OPERATORS)
        self.assertEqual(sm.state, states.STATE_START)

    # Start State Tests
    def test_start_state_and_transition(self):
        sm = StateManager.StateManager([], consts.OPERATORS)
        sm.transition('&&')
        self.assertEqual(sm.state, states.STATE_AND)

    def test_start_state_or_transition(self):
        sm = StateManager.StateManager([], consts.OPERATORS)
        sm.transition('||')
        self.assertEqual(sm.state, states.STATE_OR)

    def test_start_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    def test_start_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    # And State Tests
    def test_and_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('&&')
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    # Or State Tests
    def test_or_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('||')
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    # Operator State Tests
    def test_or_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('||')
        sm.transition('a')
        sm.transition('=')
        self.assertEqual(sm.state, states.STATE_OPERATOR)

    # Val State Tests
    def test_or_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('||')
        sm.transition('a')
        sm.transition('=')
        sm.transition('1')
        self.assertEqual(sm.state, states.STATE_VAL)

    # Pop State Tests
    def test_or_state_prop_transition(self):
        sm = StateManager.StateManager(['a'], consts.OPERATORS)
        sm.transition('||')
        sm.transition('a')
        sm.transition('=')
        sm.transition('1')
        self.assertEqual(sm.state, states.STATE_VAL)
        sm.pop_state()
        self.assertEqual(sm.state, states.STATE_OPERATOR)
        sm.pop_state()
        self.assertEqual(sm.state, states.STATE_PROP)
        sm.pop_state()
        self.assertEqual(sm.state, states.STATE_OR)
        sm.pop_state()
        self.assertEqual(sm.state, states.STATE_START)


if __name__ == '__main__':
    unittest.main()
