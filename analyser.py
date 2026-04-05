from textblob import TextBlob

class TechAnalyser:
    
    def __init__(self, threshold=0.1):
        self.name="Tech Pulse Sentiment Engine"
        self.threshold=threshold

    def get_sentiment(self, text):
        sentiment=TextBlob(text).sentiment.polarity
        return sentiment
    
    def categorize_sentiment(self,score):
        if score>self.threshold:
            res="Positive"
        elif score<-self.threshold:
            res="Negative"
        else:
            res="Neutral"
        return res

    def analyze_all(self, headlines_list):
        all_sentiment=[]
        for headline in headlines_list:
            score_each=self.get_sentiment(headline)
            label_each=self.categorize_sentiment(score_each)
            all_sentiment.append({
                "title": headline,
                "score": score_each,
                "label": label_each
            })
        return all_sentiment