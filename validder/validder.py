"""
	Validation of the schema

	:licence: MIT
"""

class Validder(object):
	def __init__(self, schema):
		self.schema = schema
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


	def validate(self, schema):
		pass