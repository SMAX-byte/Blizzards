from auto_cancel import AutoCancelJob
import unittest
from datetime import datetime, timedelta
from study_session import StudySession
class TestAutoCancelJob(unittest.TestCase):
    def setUp(self):
        self.auto_cancel_job = AutoCancelJob(proposer="Alex", time="Mon 10am", place="Library", topic="Algorithms", cancel_after_hours=1)

    def test_auto_cancel_job_creation(self):
        self.assertEqual(self.auto_cancel_job.proposer, "Alex")
        self.assertEqual(self.auto_cancel_job.time, "Mon 10am")
        self.assertEqual(self.auto_cancel_job.place, "Library")
        self.assertEqual(self.auto_cancel_job.topic, "Algorithms")
        self.assertEqual(self.auto_cancel_job.status, "pending")
        self.assertEqual(self.auto_cancel_job.cancel_after_hours, 1)

    def test_auto_cancel_method(self):
        # Capture the output of the auto_cancel method
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.auto_cancel_job.auto_cancel()
        sys.stdout = sys.__stdout__

        self.assertIn("Auto-cancelling study session on Algorithms after 1 hours", captured_output.getvalue())
        self.assertIn("Notifying buddies of cancellation for study session on Algorithms", captured_output.getvalue())
        self.assertEqual(self.auto_cancel_job.status, "cancelled")

if __name__ == "__main__":
    unittest.main()