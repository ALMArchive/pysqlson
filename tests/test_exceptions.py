import unittest

from pysqljson import StateManager, exceptions


class TestExceptions(unittest.TestCase):
    # Start State Tests
    def test_invalid_key_for_start_state(self):
        sm = StateManager.StateManager([])
        with self.assertRaises(Exception) as cm:
            sm.transition('a')
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_INVALID_KEY_FOR_START_STATE.args[0])

    def test_no_state_to_pop(self):
        sm = StateManager.StateManager([])
        with self.assertRaises(Exception) as cm:
            sm.pop_state()
            sm.pop_state()
            sm.pop_state()
            sm.pop_state()
            sm.pop_state()
            sm.pop_state()
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_NO_STATE_TO_POP.args[0])

    def test_invalid_key_for_and_state(self):
        sm = StateManager.StateManager([])
        sm.state = 'STATE_AND'
        with self.assertRaises(Exception) as cm:
            sm.transition('a')
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_INVALID_KEY_FOR_AND_STATE.args[0])

    def test_invalid_key_for_or_state(self):
        sm = StateManager.StateManager([])
        sm.state = 'STATE_OR'
        with self.assertRaises(Exception) as cm:
            sm.transition('a')
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_INVALID_KEY_FOR_OR_STATE.args[0])

    def test_invalid_key_for_prop_state(self):
        sm = StateManager.StateManager([])
        sm.state = 'STATE_PROP'
        with self.assertRaises(Exception) as cm:
            sm.transition('a')
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_INVALID_KEY_FOR_PROP_STATE.args[0])

    def test_invalid_key_for_operator_state(self):
        sm = StateManager.StateManager([])
        sm.state = 'STATE_OPERATOR'
        with self.assertRaises(Exception) as cm:
            sm.transition('=')
            sm.transition('a')
        expt = cm.exception
        self.assertEqual(expt.args[0], exceptions.ERROR_INVALID_KEY_FOR_OPERATOR_STATE.args[0])


if __name__ == '__main__':
    unittest.main()