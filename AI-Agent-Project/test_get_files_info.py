from functions.get_files_info import get_files_info

#Debug
result = get_files_info("calculator", ".")
result2 = get_files_info("calculator", "pkg")
result3 = get_files_info("calculator", "/bin")
result4 = get_files_info("calculator", "../")


print(f"The results from the debug tests are as follows:\n {result}\n, {result2}\n, {result3}\n, {result4}\n")