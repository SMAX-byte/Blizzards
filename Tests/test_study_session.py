from study_session import StudySession
import unittest
class TestStudySession(unittest.TestCase):
    def setUp(self):
        self.Alex = StudySession(proposer="Alex", time="Mon 10am", place="Library", topic="Algorithms")

    def test_study_session_creation(self):
        self.assertEqual(self.Alex.proposer, "Alex")
        self.assertEqual(self.Alex.time, "Mon 10am")
        self.assertEqual(self.Alex.place, "Library")
        self.assertEqual(self.Alex.topic, "Algorithms")
        self.assertEqual(self.Alex.status, "pending")

    def test_invite_method(self):
        # Capture the output of the invite method
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.Alex.invite("Sam")
        sys.stdout = sys.__stdout__

        self.assertIn("Inviting Sam to study session on Algorithms", captured_output.getvalue())

    def test_confirm_method(self):
        self.Alex.confirm()
        self.assertEqual(self.Alex.status, "confirmed")

    def test_cancel_method(self):
        self.Alex.cancel()
        self.assertEqual(self.Alex.status, "cancelled")