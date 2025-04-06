# pytest prompt options (cmd line)


- pytest -v -s --runxfail test_TC1.py
	- s: report including the print statements
	- v: verbose mode
	- vv: additional verbosity (more info under the "short test summary info" section upon failure encounters)
	- runxfail: for running also the marked xfail
	- pytest -m (followed by tags): refer to below examples
	- pytest -k (followed by test keywords/names): refer to below examples
	- --disable-warnings: add it when having potential annoying typos warning 


## Omitting the test name results in running the entire test suite under the selected root folder:
- pytest -v


## Reading the content of any ASCII file:
- cat test_main.py


## Ability to run specific explicitly defined tests/function_calls (here: 'test_get_weather' & 'test_get_weather_skipped'):
- pytest -v test_TC2.py::test_get_weather test_TC2.py::test_get_weather_skipped



## Ability to run tests by keyword 'k' (TCs methods to contains WORD and to not contain another WORD):
- pytest -v  -k "divide and not type"
(only: "test_TC1.py::test_divide" is running)
I can utilize it for sanity tests or long and whatever :)


## providing a list of the 2 slowest tests
- pytest -vv --durations=2


## -m for running only the tests tagged (or not tagged) as defined in quotation below: example for marking TCs: @pytest.mark.nice, @pytest.mark.slow
## note: ignore the warning about potential typos... (you can ask pytest to ignore warning by adding to user prompt: --disable-warnings)
- pytest -m "nice and slow"
- pytest -m "nice or slow" (to run both tagged tests)


## The dependency package
>To scale up pytest and enhance dependency capabilities on multiple TCs (recommended), you can use the pytest-dependency:
- pip install pytest-dependency


-----------------


