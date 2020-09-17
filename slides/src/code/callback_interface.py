class Callback:
    def on_train_begin(self, logs: dict): ...
    def on_train_end(self, logs: dict): ...

    def on_epoch_begin(self, epoch_number: int, logs: dict): ...
    def on_epoch_end(self, epoch_number: int, logs: dict): ...

    def on_train_batch_begin(self, batch_number: int, logs: dict): ...
    def on_train_batch_end(self, batch_number: int, logs: dict): ...

    def on_backward_end(self, batch_number: int): ...

    def on_test_batch_begin(self, batch_number: int, logs: dict): ...
    def on_test_batch_end(self, batch_number: int, logs: dict): ...

    def on_test_begin(self, logs: dict): ...
    def on_test_end(self, logs: dict): ...

    self.params = {...} # Contains 'epochs' and 'steps_per_epoch'
    self.model = ... # Poutyne Model