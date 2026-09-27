# Scorer
def judge(question, expects, answer, results):
    expected = expects.lower()
    for result in results:
        if expected in result.text.lower():
            return True
    return False