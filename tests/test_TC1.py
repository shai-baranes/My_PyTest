
# ---- to handle relative paths in my IDE --------
import os, sys, time
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")
# above mentioned steps will make 1 level up module available for import
# here Client, Server and Common all 3 can be imported.

# below mentioned import will be relative to root project
# ---------------------------------------------------



import pytest 
from src.TC1 import add, divide
# we shall have ["add", "divide", ...] functions...

# pytest prompt options:
# >> pytest -v -s --runxfail test_TC1.py
# -s: report including the print statements
# -v: verbose mode
# -runxfail: running also the marked xfail


def test_add():
	print(f"\nStarting bulk of add tests.")
	assert add(2, 3) == 5, "2+3 should be 5"
	assert add(-1, 1) == 0
	assert add(0, 0) == 0
	print(f"Ending bulk of add tests.")


def test_add_text():
	value = add("shai ", "baranes")
	assert value == "shai baranes"
	assert isinstance(value, str)


def test_divide():
	with pytest.raises(ValueError, match=r'Cannot Divide by \d+'):  # the match is an optional param
	# with pytest.raises(ZeroDivisionError, match=r'Cannot Divide by \d+'):
		divide(0, 0)
	assert divide(10,2)==5


@pytest.mark.nice
def test_add_in_range():
	# --- to support resulted value to fall within a given range
	flag = True if (0 < add(2, 3) < 10) else False
	assert flag == True, "2+3 should fall in range 0 to 10"


@pytest.mark.nice
@pytest.mark.slow
def test_divide_type():
	time.sleep(2)
	assert isinstance(divide(10, 2), float)



@pytest.mark.xfail(reason="we know that it is failing and not fixed yet!") # the reason and parenthesis test is optional
# @pytest.mark.xfail # the reason and parenthesis test is optional
def test_divide_type_known_failure():
	assert isinstance(divide(10, 2), int)



@pytest.mark.skip(reason="Skipped by default")
# @pytest.mark.skipif(False, reason="Skipping this test") # from ChatGPT
def test_divide_type_known_failure_2():
	assert isinstance(divide(5, 2), int)






#### another option: (note that the verbose mode shall result with each line instead of each method as following...)
# test_TC1.py::test_multiple_add[1-2-3] PASSED                                                                        [ 57%]
# test_TC1.py::test_multiple_add[2-5-7] PASSED                                                                        [ 71%]
# test_TC1.py::test_multiple_add[5--10--5] PASSED                                                                     [ 85%]
# test_TC1.py::test_multiple_add[-10-10-0] PASSED                                                                     [100%]
@pytest.mark.parametrize("a, b, result", [
	(1, 2, 3),
	(2, 5, 7),
	(5, -10, -5),
	(-10, 10, 0),
])



def test_multiple_add(a, b, result):
	assert add(a, b) == result

 

# --------------------------------------------------------------------------------------------------------
# ------------------------------------    Working w/ test dependencies    --------------------------------
# --------------------------------------------------------------------------------------------------------




from pytest_dependency import depends
# note that once you work w/ dependencies, the order is pre-selected by python and you cannot compromize it by re-ordering or by mistaking order values, e.g. '@pytest.mark.order(1)'



@pytest.mark.dependency(name="test_divide_type_fails_and_triggers_skip") # we can mark as many tests as we wish this way
@pytest.mark.order(1)  # Ensure this test runs first (requires: >>pip install pytest-order)
def test_divide_type_fails_and_triggers_skip():
	assert isinstance(divide(10, 2), int)
	# assert isinstance(divide(10, 2), float)


@pytest.mark.dependency(name="test_B")
def test_B():
	assert True


@pytest.mark.dependency(depends=["test_divide_type_fails_and_triggers_skip", "test_B"]) # can have a list of TCs here
@pytest.mark.order(2)  # Ensure this test runs second (requires: >>pip install pytest-order)
def test_pending_skip_upon_above_failure():
    assert add(2, 3) == 5, "2+3 should be 5"
    assert add(-1, 1) == 0
    assert add(0, 0) == 0




# # ----------------------------------Working Concept by PerPlexity - can be used for other future needs-----------------


# # Fixture to track the result of the dependent test
# @pytest.fixture(scope="session")
# def dependent_test_result():
#     return {"passed": True}  # Default to True; will be updated dynamically



# @pytest.mark.order(1)  # Ensure this test runs first (requires: >>pip install pytest-order)
# def test_divide_type_fails_and_triggers_skip(dependent_test_result):
# 	try:
# 		assert isinstance(divide(10, 2), int)
# 		dependent_test_result["passed"] = True
# 	except AssertionError:
# 		dependent_test_result["passed"] = False
# 		raise  # Re-raise exception to mark the test as failed



# @pytest.mark.order(2)  # Ensure this test runs second (requires: >>pip install pytest-order)
# def test_pending_skip_upon_above_failure(dependent_test_result):
#     if not dependent_test_result["passed"]:
#         pytest.skip("Skipping because 'test_divide_type_fails_and_triggers_skip' failed.")
#     # Proceed with this test if 'test_dependent' passed
#     assert add(2, 3) == 5, "2+3 should be 5"
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0


# # --------------------------------------------------------------------------------------------