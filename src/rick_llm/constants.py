MAX_SEQ_LENGTH = 2048

MODEL_CONFIG = {
    "model_name": "unsloth/Meta-Llama-3.1-8B-bnb-4bit",
    "load_in_4bit": False,
    "dtype": None,
}

PEFT_CONFIG = {
    "r": 32,
    "lora_alpha": 64,
    "lora_dropout": 0,
    "target_modules": [
        "q_proj",
        "k_proj",
        "v_proj",
        "up_proj",
        "down_proj",
        "o_proj",
        "gate_proj",
    ],
    "use_rslora": True,
    "use_gradient_checkpointing": "unsloth",
}

TRAINING_ARGS = {
    "learning_rate": 2e-4,
    "lr_scheduler_type": "linear",
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 4,
    "num_train_epochs": 5,
    "logging_steps": 1,
    "optim": "adamw_8bit",
    "weight_decay": 0.01,
    "warmup_steps": 5,
    "output_dir": "output",
    "seed": 0,
    "report_to": "none",
}
