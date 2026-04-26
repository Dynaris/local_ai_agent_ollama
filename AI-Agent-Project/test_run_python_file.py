from functions.run_python_file import run_python_file

#Debug
result = run_python_file("calculator", "main.py")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
result3 = run_python_file("calculator", "tests.py")
result4 = run_python_file("calculator", "../main.py")
result5 = run_python_file("calculator", "nonexistent.py")
result6 = run_python_file("calculator", "lorem.txt")

print(f"The results from the debug tests are as follows:\n {result}\n, {result2}\n, {result3}\n, {result4}\n, {result5}\n, {result6}\n")