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
	sudo apt install curl libcurl4-openssl-dev -y && \
	pip install -r requirements_lambda.txt

finetune:
	echo "Finetuning Rick LLM"
	python src/rick_llm/finetune.py
