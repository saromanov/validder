"""
	Validation of the schema

	:licence: MIT
"""

class Validder(object):
	def __init__(self, schema):
		self.input_schema = schema
		if self._valid_input_schema(schema) is False:
			return False

	def _valid_input_schema(self, schema):
		''' providing validation of the input schema. It should be dict '''
		if isinstance(schema, dict) is False:
			return False

		# Check, if all of the types its a strings
		for key, value in schema.items():
			if isinstance(key, string) is False:
				return False

		return True

	def _check_type(self, properties):
		''' checking type of the input value.
		Allowed types: string, list, int, float, any
		'''
		allowed_types = ["string", "int", "float", "list"]
		current_type = properties["type"]
		return True if current_type in allowed_types else False

	def _check_type_value(self, typeItem, value):
		''' return True if value satisfied key properties
		'''
		if typeItem == "string":
			return True if isinstance(key, string) else False
		if typeItem == "int":
			return True if isinstance(key, int) else False
		if typeItem == "float":
			return True if isinstance(key, float) else False
		if typeItem == "list":
			return True if isinstance(key, list) else False
		return False


	def _check_properties(self, key, value):
		properties = self.input_schema[key]



	def validate(self, schema):
		if isinstance(schema, dict) is False:
			raise Exception("Unable to validate schema")

		# Counting required arguments
		required = []
		for key, value in schema.items():
			if 'required' in value:
				item = value['required']
				if item: required.append(item)

		for key, value in schema.items():
			if key not in self.input_schema:
				raise Exception("{0} is not exist at the input schema".format(key))
			properties = self.input_schema[key]
			value = self._check_type(properties)
			# at the last, check that elements is on required
			if key in required:
				required.remove(key)

		# checking, that required is empty
		if len(required) > 0:
			raise Exception("Required elements {0} is not exist".format(required))