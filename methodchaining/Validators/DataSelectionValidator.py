class DataSelectionValidator:

    def entry_is_exist(self, data_selector):
        if data_selector is None:
            #raise ValueError(f"{self.name} should be positive")
            raise ValueError(f" data entry should be added first ")

