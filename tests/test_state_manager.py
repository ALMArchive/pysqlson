import unittest
from pysqljson import StateManager, states, exceptions


class TestStateManager(unittest.TestCase):
    def test_start_state(self):
        sm = StateManager.StateManager([])
        self.assertEqual(sm.state, states.STATE_START)

    # Start State Tests
    def test_start_state_and_transition(self):
        sm = StateManager.StateManager([])
        sm.transition('&&')
        self.assertEqual(sm.state, states.STATE_AND)

    def test_start_state_or_transition(self):
        sm = StateManager.StateManager([])
        sm.transition('||')
        self.assertEqual(sm.state, states.STATE_OR)

    def test_start_state_prop_transition(self):
        sm = StateManager.StateManager(['a'])
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    def test_start_state_prop_transition(self):
        sm = StateManager.StateManager(['a'])
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    # And State Tests
    def test_and_state_prop_transition(self):
        sm = StateManager.StateManager(['a'])
        sm.transition('&&')
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)

    # Or State Tests
    def test_or_state_prop_transition(self):
        sm = StateManager.StateManager(['a'])
        sm.transition('||')
        sm.transition('a')
        self.assertEqual(sm.state, states.STATE_PROP)


if __name__ == '__main__':
    unittest.main()
