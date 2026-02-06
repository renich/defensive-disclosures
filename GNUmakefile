# Orchestrator for Defensive Disclosure Pipeline (Hardened)

# Detect virtual environment
VENV=venv
VENV_BIN=$(VENV)/bin/python3
PYTHON=$(shell if [ -f $(VENV_BIN) ]; then echo $(VENV_BIN); else echo python3; fi)

BIN_DIR=bin
BUILD_DIR=build
IDEAS_DIR=ideas

BLUE=\033[94m
RESET=\033[0m

.PHONY: all generate index pdf clean

all: generate index pdf

generate:
	@echo "$(BLUE)Starting LLM generation...$(RESET)"
	@$(PYTHON) $(BIN_DIR)/generator.py

index:
	@echo "$(BLUE)Rebuilding indices...$(RESET)"
	@$(PYTHON) $(BIN_DIR)/update_index.py

# Fix shell loop vulnerability and whitespace handling
pdf:
	@echo "$(BLUE)Compiling PDFs (Secure Mode)...$(RESET)"
	@mkdir -p $(BUILD_DIR)/en $(BUILD_DIR)/es
	@find $(IDEAS_DIR)/en -name "*.rst" ! -name "index.rst" -exec sh -c 'pandoc "$$1" -o "$(BUILD_DIR)/en/$$(basename "$$1" .rst).pdf" --pdf-engine=xelatex' _ {} \;
	@find $(IDEAS_DIR)/es -name "*.rst" ! -name "index.rst" -exec sh -c 'pandoc "$$1" -o "$(BUILD_DIR)/es/$$(basename "$$1" .rst).pdf" --pdf-engine=xelatex' _ {} \;

clean:
	@echo "$(BLUE)Cleaning build directory...$(RESET)"
	@rm -rf $(BUILD_DIR)
