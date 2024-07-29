def evaluate_operand(value, data):
    left, op, right = value
    left_val = data.get(left)
    right_val = int(right) if right.isdigit() else data.get(right)

    if op == ">":
        return left_val > right_val
    elif op == "<":
        return left_val < right_val
    elif op == "=":
        return left_val == right_val
    return False

def evaluate_rule(ast_node, data):
    if ast_node.node_type == "operand":
        return evaluate_operand(ast_node.value, data)
    
    left_val = evaluate_rule(ast_node.left, data)
    right_val = evaluate_rule(ast_node.right, data)

    if ast_node.value == "AND":
        return left_val and right_val
    elif ast_node.value == "OR":
        return left_val or right_val

    return False
