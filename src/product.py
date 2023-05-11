import pandas as pd
import json

with open('data/criterias.json','r') as f:
  CRITERIAS = json.load(f)

class Product:
  def __init__(self,data:pd.DataFrame):
    self.ratingId = data[0]
    self.stars = data[1]
    self.content = data[2]

    self.ratings = {criteria:0 for criteria in CRITERIAS}


  def __str__(self):
    return ",".join(list(map(str,[
      self.ratingId,
      self.stars,
      self.content])))\
      + '\nRatings:\n' \
      + '\n'.join([f'{criteria}: {rating}' for criteria,rating in self.ratings.items()])
