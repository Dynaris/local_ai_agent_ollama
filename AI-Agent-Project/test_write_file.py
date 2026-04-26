from functions.write_file import write_file

#Debug
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

print(f"The results from the debug tests are as follows:\n {result}\n, {result2}\n, {result3}\n")