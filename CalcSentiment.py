
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def polarity_scores(self, text):
        return self.analyzer.polarity_scores(text)

