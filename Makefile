version:
	@if [ -z "$(v)" ]; then \
		echo "\033[31mErro: Parâmetro de versão (v) não fornecido\033[0m"; \
		echo "Uso: make version v=patch|minor|major|X.Y.Z"; \
		exit 1; \
	fi
	@echo "\033[34mVerificando status do git...\033[0m"
	@if [ -n "$$(git status --porcelain)" ]; then \
		echo "\033[31mErro: Existem mudanças não commitadas no repositório\033[0m"; \
		git status; \
		exit 1; \
	fi
	@echo "\033[34mAtualizando versão para $(v)...\033[0m"
	@poetry version $(v)
	@echo "\033[34mCriando commit e tag da nova versão...\033[0m"
	@git add pyproject.toml
	@git commit -m "v$$(poetry version -s)"
	@git tag v$$(poetry version -s)
	@echo "\033[34mEnviando alterações para o repositório remoto...\033[0m"
	@git push
	@git push --tags
	@echo "\033[32mVersão atual: $$(poetry version -s)\033[0m"

.PHONY: version