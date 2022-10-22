files123 = ['1.txt', '2.txt', '3.txt']
# to solve the problems I created 3 ordered 
# lists (from the smallest amount of lines to biggest)
# open_files: the name of a file
# ordered_lines: the number of lines in the file
# contents: the content of the file
def unite_files(files):
    files_data = []
    n_lines = []
    ordered_lines = []
    open_files = []
    contents = []
    for file in files:
        # count the number of lines
        with open(file, 'r', encoding='utf-8') as f:
            n_line = len(f.readlines())
            n_lines.append(n_line)
            files_data.append({n_line: file})
    # creating the ordered list of counted lines
    # and the ordered list of file names
    while True: 
        for file_data in files_data:
            if n_lines:
                m = min(n_lines)
                if file_data.get(m) is not None:
                    open_files.append(file_data.get(m))     
            if file_data.get(m) is not None:
                ordered_lines.append(m)
                n_lines.remove(m)
        if not n_lines:
                break
    # saving the contents of the files in ordered list
    for open_file in open_files:
        with open(open_file, 'r', encoding='utf-8') as op_f:
            contents.append(op_f.read())
    # iterating each file and creating united file
    with open('new_file.txt', 'a', encoding='utf-8') as new_f:
        n = 0
        for open_file in open_files:
            new_f.write(f"{open_file}\n")
            new_f.write(f"{str(ordered_lines[n])}\n")
            new_f.write(f"{contents[n]}\n")
            n += 1

unite_files(files123)