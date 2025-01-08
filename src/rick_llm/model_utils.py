from exceptions import UnslothNotInstalledError
from constants import MAX_SEQ_LENGTH, MODEL_CONFIG, PEFT_CONFIG

try:
    from unsloth import FastLanguageModel  # type: ignore
except ImportError:
    raise UnslothNotInstalledError


def initialize_model():
    """Initialize and return the base model and tokenizer."""
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL_CONFIG["model_name"],
        max_seq_length=MAX_SEQ_LENGTH,
        load_in_4bit=MODEL_CONFIG["load_in_4bit"],
        dtype=MODEL_CONFIG["dtype"],
    )
    return model, tokenizer


def setup_peft_model(model):
    """Apply PEFT configuration to the model."""
    return FastLanguageModel.get_peft_model(model, **PEFT_CONFIG)
