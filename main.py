from stack import Stack


def sequence_parentheses(braked_str):
    stack = Stack()
    open_braked = '([{'
    close_braked = ')]}'
    braked_dict = {'(': ')', '[': ']', '{': '}'}
    for parenthesis in braked_str:
        if parenthesis in open_braked:
            stack.push(parenthesis)
        elif parenthesis in close_braked:
            if stack.size() > 0 and parenthesis == braked_dict[stack.peek()]:
                stack.pop()
            else:
                return 'Несбалансированно'

    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    sequence = input('Введите последовательность скобок: ')
    print(sequence_parentheses(sequence))
