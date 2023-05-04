import pandas as pd
import json

with open('data/criterias.json','r') as f:
  CRITERIAS = json.load(f)

class Product:
  def __init__(self,data:pd.DataFrame):
    self.reviewerID = data[0]
    self.asin = data[1]
    self.reviewerName = data[2]
    self.helpful = data[3]
    self.reviewText = data[4]
    self.overall = data[5]
    self.summary = data[6]
    self.unixReviewTime = data[7]
    self.reviewTime = data[8]

    self.ratings = {criteria:0 for criteria in CRITERIAS}


  def __str__(self):
    return ",".join(list(map(str,[
      self.reviewerID,
      self.asin,
      self.reviewerName,
      self.helpful,
      self.reviewText,
      self.overall,
      self.summary,
      self.unixReviewTime,
      self.reviewTime]))) \
      + '\nRatings:\n' \
      + '\n'.join([f'{criteria}: {rating}' for criteria,rating in self.ratings.items()])

if __name__ == "__main__":
  test_data = r"""AHMEG9CAAT2KF,B0002CZVWS,Bon,"[0, 0]","I've only been playing ukulele for about 3 years, so I'm new to using a capo.  It seems to hold tight.",4,I'm new to a capo,1380844800,"10 4, 2013","""
  processed_data = test_data.split(',')

