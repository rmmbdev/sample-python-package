from classifier import Classifier


def run_demo():
    clf = Classifier()
    # clf = America("192.168.30.215:9000", "america")
    samples = [
        {"id": 1, "data": "It was great"},
        {"id": 2, "text": "I am totally dissatisfied with the services"},
    ]
    print(clf.classify(samples))


if __name__ == '__main__':
    run_demo()
