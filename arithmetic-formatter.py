def parse_expr(problem):
    num1, op, num2 = problem.split(' ')

    # error handling
    if not (num1.isnumeric() and num2.isnumeric()):
        return "Error: Numbers must only contain digits."
    if (len(num1) > 4 or len(num2) > 4):
        return "Error: Numbers cannot be more than four digits."
    if op not in ('+', '-'):
        return "Error: Operator must be '+' or '-'."

    # this method returns result regardless of show_answer variable
    n1, n2 = int(num1), int(num2)
    result = n1 + n2 if op == '+' else n1 - n2
    return num1,op,num2,str(result)
    

def format_output(arranged_problems):
    # transpose problems list to format lines from each problem as one row instead of multiple rows
    output = [[arranged_problems[j][i] for j in range(len(arranged_problems))] for i in range(len(arranged_problems[0]))]
    output = ['    '.join(row) for row in output]
    return '\n'.join(output)


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5: return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        # attempt to extract values needed in output
        values = parse_expr(problem)
        if "Error" in values:
            return values
        else:
            num1,op,num2,result = values

        # calculate number of dashes required, and format rows accordingly
        dashes_count = 2 + max(len(num1),len(num2))
        top_line = ' ' * (dashes_count - len(num1)) + num1
        bottom_line = op + " " * (dashes_count-1-len(num2)) + num2
        separator = '-' * dashes_count

        # result logic handled here
        rows = [top_line,bottom_line,separator]
        if show_answers:
            result = ' ' * (dashes_count - len(result)) + result
            rows.append(result)
        arranged_problems.append(rows)
    
    return format_output(arranged_problems)

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
