from flask import request, jsonify
from app import app
from app.rule_parser import create_rule, combine_rules
from app.rule_evaluator import evaluate_rule
from app.models import Node

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    try:
        rule_string = request.json['rule']
        rule_ast = create_rule(rule_string)
        return jsonify(ast=rule_ast.__dict__)
    except Exception as e:
        app.logger.error(f"Error in create_rule: {str(e)}")
        return jsonify(error=str(e)), 400

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    try:
        rules = request.json['rules']
        app.logger.info(f"Received rules for combination: {rules}")
        combined_ast = combine_rules(rules)
        app.logger.info(f"Combined AST: {combined_ast.__dict__}")
        return jsonify(ast=combined_ast.__dict__)
    except Exception as e:
        app.logger.error(f"Error in combine_rules: {str(e)}")
        return jsonify(error=str(e)), 400

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    try:
        ast_dict = request.json['ast']
        data = request.json['data']
        ast_node = Node(ast_dict['node_type'], value=ast_dict['value'])
        result = evaluate_rule(ast_node, data)
        return jsonify(result=result)
    except Exception as e:
        app.logger.error(f"Error in evaluate_rule: {str(e)}")
        return jsonify(error=str(e)), 400
