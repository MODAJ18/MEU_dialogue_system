from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class IntentRecognizer:
    def __init__(self):
        # LogReg_model = LogisticRegression()
        self.model = LogisticRegression()
        self.intent_models = {}
        self.acc_scores = {}


    def evaluate(self, X_test, y_test, intent):
        y_pred = self.intent_models[intent].predict(X_test)
        self.acc_scores[intent] = accuracy_score(y_test, y_pred)
        print('accuracy %s' % self.acc_scores[intent])
        return self.acc_scores[intent]

    def learn_intents(self, X, y, intent):
        self.intent_models[intent] = LogisticRegression()
        self.intent_models[intent].fit(X, y)

    def get_intents(self, transcript, les, tfidfV):
        transcript = tfidfV.transform([transcript])
        action_pred = les["action"].inverse_transform(self.intent_models["action"].predict(transcript))[0]
        object_pred = les["object"].inverse_transform(self.intent_models["object"].predict(transcript))[0]
        location_pred = les["location"].inverse_transform(self.intent_models["location"].predict(transcript))[0]

        return {"action": action_pred, "object": object_pred, "location": location_pred}

