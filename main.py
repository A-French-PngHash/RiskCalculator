# Computing : 

from classes import Configuration
from proba_calc.proba_calc import RiskProbaCalculator


configuration = Configuration([1, 0, 3],[0, 0, 0], False)
risk_prob = RiskProbaCalculator(configuration)
print(risk_prob.compute_all(10, 10))
