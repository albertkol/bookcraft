.PHONY: craft craft-dark ra ra-dark

craft:
	poetry run python main.py craft

craft-dark:
	poetry run python main.py craft-dark

ra:
	poetry run python main.py ra

ra-dark:
	poetry run python main.py ra-dark
