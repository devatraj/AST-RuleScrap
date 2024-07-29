from .models import Node

def parse_expression(expression):
    left, op, right = expression.partition(' ')
    return Node("operand", value=(left.strip(), op.strip(), right.strip()))

def create_rule(rule_string):
    tokens = rule_string.split()
    stack = []

    for token in tokens:
        if token in ("AND", "OR"):
            node = Node("operator", value=token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        elif token.startswith("("):
            token = token[1:]  # Remove '('
            stack.append(parse_expression(token))
        elif token.endswith(")"):
            token = token[:-1]  # Remove ')'
            stack.append(parse_expression(token))
        else:
            stack.append(parse_expression(token))

    return stack[0] if stack else None

def combine_rules(rules):
    combined_node = Node("operator", value="AND")
    combined_node.left = create_rule(rules[0])
    current_node = combined_node.left

    for rule in rules[1:]:
        new_node = Node("operator", value="AND")
        new_node.left = current_node
        new_node.right = create_rule(rule)
        current_node = new_node

    combined_node.right = current_node
    return combined_node
