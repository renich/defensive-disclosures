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

.PHONY: all generate index pdf publish lint clean

all: index pdf

lint:
	@echo "$(BLUE)Running rstcheck...$(RESET)"
	@rstcheck -r .

generate:
	@echo "$(BLUE) [Agent] Triggering opencode generation...$(RESET)"
	@opencode run --model google/gemini-3-flash-preview --agent build "Follow the SOP in instructions.rst to process ideas.jsonc and generate missing disclosures in ideas/en/ and ideas/es/. EXECUTE IMMEDIATELY."

index:
	@echo "$(BLUE)Rebuilding indices...$(RESET)"
	@python3 $(BIN_DIR)/update_index.py

pdf:
	@echo "$(BLUE)Compiling PDFs (Secure Mode)...$(RESET)"
	@mkdir -p $(BUILD_DIR)/en $(BUILD_DIR)/es
	@find $(IDEAS_DIR)/en -name "*.rst" ! -name "index.rst" -print0 | xargs -0 -P 4 -I {} sh -c 'pandoc "{}" -o "$(BUILD_DIR)/en/$$(basename "{}" .rst).pdf" --pdf-engine=xelatex'
	@find $(IDEAS_DIR)/es -name "*.rst" ! -name "index.rst" -print0 | xargs -0 -P 4 -I {} sh -c 'pandoc "{}" -o "$(BUILD_DIR)/es/$$(basename "{}" .rst).pdf" --pdf-engine=xelatex'

publish: generate index
	@echo "$(BLUE) [Git] Committing and Pushing...$(RESET)"
	@git add $(IDEAS_DIR)/ ideas.jsonc
	@git diff-index --quiet HEAD || git commit -m "feat: automated defensive disclosure release $(shell date +%Y-%m-%d)"
	@git push origin master
	@echo "$(BLUE) [Done] Release triggered.$(RESET)"

clean:
	@echo "$(BLUE)Cleaning build directory...$(RESET)"
	@rm -rf $(BUILD_DIR)
