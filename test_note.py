class KerasRegressor():
	def __init__(self, params):
		self.params = params

	def score(self):
		print(self.model)
		print(self.params)


class SklearnRegressor(KerasRegressor):
	def __init__(self, params):
		super(SklearnRegressor, self).__init__(params=params)

	def fit(self, model):
		self.model = model

m = SklearnRegressor("dummy_params")
m.fit(model="dummy_model")
m.score()
m.fit