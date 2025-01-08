class UnslothNotInstalledError(ImportError):
    """Exception raised when Unsloth is not installed.

    This exception should be raised when attempting to use Unsloth-dependent
    functionality without having Unsloth installed in the environment.
    """

    def __init__(
        self,
        message="Unsloth is required but not installed. Remember finetune should be run in a Lambda Labs instance",
    ):
        self.message = message
        super().__init__(self.message)
