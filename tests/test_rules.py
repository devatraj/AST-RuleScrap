import unittest
import json
from tests import RuleEngineTestCase

class TestRuleEngine(RuleEngineTestCase):

    def test_create_rule(self):
        rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        response = self.create_rule(rule1)
        self.assertEqual(response.status_code, 200)
        self.assertIn('ast', response.json)

    def test_combine_rules(self):
        rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        response = self.combine_rules([rule1, rule2])
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertIn('ast', response.json)
        combined_ast = response.json['ast']
        print("Combined AST:", json.dumps(combined_ast, indent=2))

    def test_evaluate_rule(self):
        rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        combined_response = self.combine_rules([rule1, rule2])
        self.assertEqual(combined_response.status_code, 200, msg=combined_response.get_data(as_text=True))
        combined_ast = combined_response.json.get('ast')
        self.assertIsNotNone(combined_ast)

        data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        response = self.evaluate_rule(combined_ast, data1)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertTrue(response.json['result'])

        data2 = {"age": 22, "department": "Marketing", "salary": 40000, "experience": 6}
        response = self.evaluate_rule(combined_ast, data2)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertTrue(response.json['result'])

        data3 = {"age": 40, "department": "Marketing", "salary": 25000, "experience": 7}
        response = self.evaluate_rule(combined_ast, data3)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertTrue(response.json['result'])

        data4 = {"age": 29, "department": "IT", "salary": 30000, "experience": 2}
        response = self.evaluate_rule(combined_ast, data4)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertFalse(response.json['result'])

        rule3 = "(age > 40 AND department = 'HR') AND (salary > 60000 OR experience > 10)"
        combined_response2 = self.combine_rules([rule1, rule2, rule3])
        self.assertEqual(combined_response2.status_code, 200, msg=combined_response2.get_data(as_text=True))
        combined_ast2 = combined_response2.json.get('ast')
        self.assertIsNotNone(combined_ast2)

        data5 = {"age": 45, "department": "HR", "salary": 65000, "experience": 11}
        response = self.evaluate_rule(combined_ast2, data5)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertTrue(response.json['result'])

        data6 = {"age": 35, "department": "HR", "salary": 55000, "experience": 9}
        response = self.evaluate_rule(combined_ast2, data6)
        self.assertEqual(response.status_code, 200, msg=response.get_data(as_text=True))
        self.assertFalse(response.json['result'])

if __name__ == '__main__':
    unittest.main()
