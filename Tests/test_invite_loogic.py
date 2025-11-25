from invite_logic import InviteLogic
from study_session import StudySession
import unittest
class TestInviteLogic(unittest.TestCase):
    def setUp(self):
        self.invite = InviteLogic(proposer="Alex", time="Mon 10am", place="Library", topic="Algorithms")

    def test_invite_logic_creation(self):
        self.assertEqual(self.invite.proposer, "Alex")
        self.assertEqual(self.invite.time, "Mon 10am")
        self.assertEqual(self.invite.place, "Library")
        self.assertEqual(self.invite.topic, "Algorithms")
        self.assertEqual(self.invite.status, "pending")
        self.assertFalse(self.invite.accepted)

    def test_accept_invite_method(self):
        # Capture the output of the accept_invite method
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.invite.accept_invite()
        sys.stdout = sys.__stdout__

        self.assertIn("Invite accepted by Alex", captured_output.getvalue())
        self.assertTrue(self.invite.accepted)

    def test_decline_invite_method(self):
        # Capture the output of the decline_invite method
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.invite.decline_invite()
        sys.stdout = sys.__stdout__

        self.assertIn("Invite declined by Alex", captured_output.getvalue())
        self.assertFalse(self.invite.accepted)

if __name__ == "__main__":
    unittest.main()