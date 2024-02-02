import pytest
from main import sequence_parentheses


@pytest.mark.parametrize(
    'expected, sequence',
    (
        ['Сбалансированно', '(((([{}]))))'],
        ['Сбалансированно', '[([])((([[[]]])))]{()}'],
        ['Сбалансированно', '{{[()]}}'],
        ['Несбалансированно', '}{}'],
        ['Несбалансированно', '{{[(])]}}'],
        ['Несбалансированно', '[[{())}]']
    )
)
def test_sequence_parentheses(expected, sequence):
    actual = sequence_parentheses(sequence)
    assert expected == actual
