# Midterm Exam: Extract program elements.

Your submission must satisfy the following requirements:

* R1. Shall initialize your assignment repository from https://classroom.github.com/a/q0t9KYdR
* R2. Write your `design_extractor.py` in the repository.
* R3. Test your `design_extractor.py` by using `pytest`.
* R4. You need to let your TA know your repository URL and your student ID together via Slack.
* R5. Check out `test_extractor1.py` to figure out the output format.
* R6. Assume that there are no nested classes and anonymous classes.
* R7. Assume that the source code may contain a nested function.
* R8. The function `collectProgramDesign` takes a path of a Python files, and produce a pair of (1) list of functions at the module root level, which are not included in any class, and (2) a map of member variables and member functions for each root-level class as follows (type hint: `(List[str], Dict[str, Dict[str,List[str]]])` ):
```
(['func1', 'func2', ...], {'class1': {'attrs': {'member_var1', 'member_var2', 'member_var3', ...}, 'funcs': ['member_func1', 'member_func1', ...], ...},
```
* R9: If no member variable is available in a class, the corresponding value of `attrs` should be an empty set.
* R10: If no member functions is available in a class, the corresponding value of `funcs` should be an empty list.



## Note:

* N1. `pytest` (based on `test_extractor1.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS or any other means are not accepted.
* N3. DO NOT change files in this repository except for `design_extractor.py`. Adding new files are allowed.
* N4. Late submissions after 4:15pm are *NOT* allowed.
