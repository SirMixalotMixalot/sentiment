from sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def help_me_test(self, prompt, expectedSentiment):
        self.assertEqual(sentiment_analyzer(prompt)['label'], expectedSentiment)
    def test_sentiment_analyzer(self):
        self.help_me_test("I love working with Python", "SENT_POSITIVE")
        self.help_me_test("I hate working with Python", "SENT_NEGATIVE")
        self.help_me_test("I am neutral on Python", "SENT_NEUTRAL")



if __name__ == "__main__":
    unittest.main()

