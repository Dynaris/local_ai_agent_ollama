from functions.get_file_content import get_file_content

#Debug
result = get_file_content("calculator", "lorem.txt")
result2 =get_file_content("calculator", "main.py")
result3 =get_file_content("calculator", "pkg/calculator.py")
result4 =get_file_content("calculator", "/bin/cat")
result5 =get_file_content("calculator", "pkg/does_not_exist.py")

print(f"The results from the debug tests are as follows:\n {result}\n, {result2}\n, {result3}\n, {result4}\n, {result5}\n")