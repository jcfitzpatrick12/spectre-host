from spectre.receivers.BaseCaptureMount import BaseCaptureMount
from spectre.receivers.mount_register import register_capture_mount

from spectre.receivers.library.Test.gr import cosine_signal_test_1
from spectre.receivers.library.Test.gr import dummy

@register_capture_mount("Test")
class CaptureMount(BaseCaptureMount):
    def __init__(self):
        super().__init__()


    def set_capture_methods(self) -> None:
        self.capture_methods = {
            "cosine-signal-test-1": self.cosine_signal_test_1,
            "key-value-test": self.dummy,

        }


    def cosine_signal_test_1(self, capture_configs: list) -> None:
        num_capture_configs = len(capture_configs)
        if num_capture_configs > 1:
            raise ValueError(f"Expected 1 capture config. Received {num_capture_configs}")
        # take the first (and now verified only) capture config in the list
        capture_config = capture_configs[0]
        cosine_signal_test_1.main(capture_config)
        return
    

    def dummy(self, capture_configs: list) -> None:
        num_capture_configs = len(capture_configs)
        if num_capture_configs > 1:
            raise ValueError(f"Expected 1 capture config. Received {num_capture_configs}")
        # take the first (and now verified only) capture config in the list
        capture_config = capture_configs[0]
        dummy.main(capture_config)
        return
