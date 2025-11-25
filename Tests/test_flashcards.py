from flashcards import FlashcardGenerator
import unittest
class TestFlashcardGenerator(unittest.TestCase):
    def setUp(self):
        self.syllabus = [
            {'date': '2024-09-01', 'flashcards': ['What is a variable?', 'Define function.']},
            {'date': '2024-09-05', 'flashcards': ['Explain loops.', 'What is recursion?']},
            {'date': '2024-09-10', 'flashcards': ['Describe OOP.', 'What is inheritance?']}
        ]
        self.generator = FlashcardGenerator(self.syllabus)

    def test_generate_flashcards_within_date_range(self):
        start_date = '2024-09-01'
        end_date = '2024-09-05'
        expected_flashcards = [
            'What is a variable?',
            'Define function.',
            'Explain loops.',
            'What is recursion?'
        ]
        generated_flashcards = self.generator.generate(start_date, end_date)
        self.assertEqual(generated_flashcards, expected_flashcards)

    def test_generate_flashcards_no_topics_in_range(self):
        start_date = '2024-08-01'
        end_date = '2024-08-31'
        expected_flashcards = []
        generated_flashcards = self.generator.generate(start_date, end_date)
        self.assertEqual(generated_flashcards, expected_flashcards)

if __name__ == "__main__":
    unittest.main()