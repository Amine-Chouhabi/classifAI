from model.processors.Processor import Processor

class SplitProcessor(Processor):
    def __init__(self, test_size=0.2, random_state=42):
        super().__init__()
        self.test_size = test_size
        self.random_state = random_state
