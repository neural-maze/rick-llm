import os

import dotenv

from model_utils import initialize_model, setup_peft_model
from trainer import ModelTrainer

dotenv.load_dotenv()


def main():
    # Initialize model
    model, tokenizer = initialize_model()
    model = setup_peft_model(model)

    # Train model
    trainer = ModelTrainer(model, tokenizer)
    trainer_instance = trainer.setup_trainer()
    trainer_instance.train()

    # Push to hub
    model.push_to_hub_gguf(
        "theneuralmaze/RickLLama-3.1-8B",
        tokenizer,
        token=os.getenv("HUGGINGFACE_TOKEN"),
    )


if __name__ == "__main__":
    main()
