NOT_CAPITALIZE = {'a', 'and', 'by', 'in', 'of', 'on', 'or', 'the', 'to', 'under', 'upon', 'with', 'within'}
IMPORTS = {
    'heapq': 'import heapq',
    'math': 'import math',
}
FROMS = {
    'collections': ['defaultdict', 'deque', 'Counter'],
    'functools': ['cache']
}

def create_file():
    problem_number = input("Problem Number: ")
    url = input("URL: ")
    print("Enter/Paste your code. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    code = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        code.append(line)

    if 'description' in url:
        url = url.split('description')[0]
    
    file_name_num = f'{int(problem_number):04d}'
    file_name_url = url.split('/problems/')[1].replace('/', '').replace('-', '_')
    file_name = file_name_num + '_' + file_name_url + '.py'

    title_tokens = []
    for token in file_name_url.split('_'):
        if token in NOT_CAPITALIZE:
            title_tokens.append(token)
        else:
            title_tokens.append(token.capitalize())
    title = problem_number + '. ' + ' '.join(title_tokens)

    imports = []
    code_str = " ".join(code)
    for key, text in IMPORTS.items():
        if key in code_str:
            imports.append(text)
    for lib, modules in FROMS.items():
        matched_module = [module for module in modules if module in code_str]
        if matched_module:
            text = 'from ' + lib + ' import ' + ', '.join(matched_module)
            imports.append(text)

    with open(file_name, 'w+') as f:
        f.write("'''\n")
        f.write(title + "\n")
        f.write(url + "\n")
        f.write("'''\n")
        f.write("\n\n")
        if imports:
            f.writelines("%s\n" % line for line in imports)
            f.write("\n\n")
        if code:
            f.writelines("%s\n" % line for line in code)


if __name__ == '__main__':
    create_file()