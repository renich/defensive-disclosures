# Orchestrator for Defensive Disclosure Pipeline (Zero-Dependency)

# Default local API settings (can be overridden)
export OPENAI_BASE_URL ?= http://localhost:11434/v1
export OPENAI_API_KEY ?= sk-antigravity
export OPENAI_MODEL ?= google/antigravity-gemini-3-flash

BIN_DIR=bin
BUILD_DIR=build
IDEAS_DIR=ideas

BLUE=\033[94m
RED=\033[91m
RESET=\033[0m

.PHONY: all generate index pdf publish clean

all: index pdf

generate:
	@echo "$(BLUE) [Agent] Generating missing disclosures...$(RESET)"
	@python3 $(BIN_DIR)/generate_native.py

index:
	@echo "$(BLUE)Rebuilding indices...$(RESET)"
	@python3 $(BIN_DIR)/update_index.py

pdf:
	@echo "$(BLUE)Compiling PDFs (Secure Mode)...$(RESET)"
	@mkdir -p $(BUILD_DIR)/en $(BUILD_DIR)/es
	@find $(IDEAS_DIR)/en -name "*.rst" ! -name "index.rst" -exec sh -c 'pandoc "$$1" -o "$(BUILD_DIR)/en/$$(basename "$$1" .rst).pdf" --pdf-engine=xelatex' _ {} \;
	@find $(IDEAS_DIR)/es -name "*.rst" ! -name "index.rst" -exec sh -c 'pandoc "$$1" -o "$(BUILD_DIR)/es/$$(basename "$$1" .rst).pdf" --pdf-engine=xelatex' _ {} \;

publish: generate index
	@echo "$(BLUE) [Git] Committing and Pushing...$(RESET)"
	@git add $(IDEAS_DIR)/
	@git diff-index --quiet HEAD || git commit -m "feat: automated defensive disclosure release $(shell date +%Y-%m-%d)"
	@git push origin master
	@echo "$(BLUE) [Done] Release triggered.$(RESET)"

clean:
	@echo "$(BLUE)Cleaning build directory...$(RESET)"
	@rm -rf $(BUILD_DIR)
