class BaseAgentFactory:
    def name(self) -> str:
        pass

    def build(self, file: str):
        pass

    def generate(self) -> str:
        pass
