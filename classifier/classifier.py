from classifier.default_config import default_config


class Classifier:
    def __int__(self):
        # TODO here you should initialize your model and related resources
        #  like loading tf model and related weights which have been trained previously
        #  you may need to reference some parameters from "default_config"
        ...

    def classify(
        self,
        inputs: list[dict],
    ) -> list[dict]:
        # TODO here you should implement infer logics
        #  like forward pass in tf or pytorch models

        raise NotImplementedError
