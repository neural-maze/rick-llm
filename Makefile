.PHONY: lambda-commands

create-hf-dataset:
	echo "Creating HF dataset"
	python src/dataset.py

generate-ssh-key:
	python src/lambda/commands.py generate-ssh-key

list-ssh-keys:
	python src/lambda/commands.py list-ssh-keys

list-instances:
	python src/lambda/commands.py list-instances

list-instance-types:
	python src/lambda/commands.py list-types

get-lambda-ip:
	python src/lambda/commands.py get-ip

launch-lambda-instance:
	python src/lambda/commands.py launch

lambda-help:
	python src/lambda/commands.py

lambda-setup:
	echo "Installing dependencies"
	sudo apt update && sudo apt upgrade -y
	sudo apt install curl libcurl4-openssl-dev -y 
	pip install -r requirements_lambda.txt -q
	pip install torchvision@https://download.pytorch.org/whl/cu121/torchvision-0.20.1%2Bcu121-cp310-cp310-linux_x86_64.whl
	pip install transformers==4.47.1

finetune:
	echo "Finetuning Rick LLM"
	python src/rick_llm/finetune.py

terminate-instance:
	python src/lambda/commands.py terminate

download-model:
	echo "Downloading model files"
	python src/download_model.py
