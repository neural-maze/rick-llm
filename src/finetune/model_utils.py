from unsloth import FastLanguageModel
from finetune.constants import MAX_SEQ_LENGTH, MODEL_CONFIG, PEFT_CONFIG


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


def prepare_model_for_inference(model):
    """Prepare the model for inference."""
    return FastLanguageModel.for_inference(model)
