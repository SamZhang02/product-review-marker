import os
from extractor import Extractor
from rater import Rater

FILEPATH = os.path.join('data','data.csv')
PRODUCT_LABELS = ['reviewerID',
                  'asin',
                  'reviewerName',
                  'helpful',
                  'reviewText',
                  'overall',
                  'summary',
                  'unixReviewTime',
                  'reviewTime']

def main():
  extractor = Extractor()
  rater = Rater(product_data)

  products = extractor.extract_data(FILEPATH)
  rater.rate_product()
  ratings = rater.get_ratings()
  print(ratings)

if __name__ == "__main__":
  main()
