# Use this makefile to run development procedures.

style: black flake8 isort pydocstyle mypy requirements
	@echo "🎉 style passed!"

black:
	black . --line-length=79
	@echo "✅ black done."

flake8:
	flake8
	@echo "✅ flake done."

isort:
	isort . --profile black
	@echo "✅ isort done."

pydocstyle:
	pydocstyle
	@echo "✅ pydocstyle done."

mypy:
	mypy
	@echo "✅ mypy done."

requirements:
	poetry export --without-hashes --output requirements.txt
	poetry export --dev --without-hashes --output requirements.dev.txt
	@echo "✅ requirements done."

clean:
	pyclean -v .
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .aws-sam
	@echo "♲ clean done."
