test:
	pytest --tb=short

watch-tests:
	ls *.py | entr pytest --tb=short

black:
	black -l 86 $$(find * -name '*.py')

clean:
		find . | grep -E ".pytest_cache" | xargs rm -rf	
		find . | grep -E "__pycache__" | xargs rm -rf
		