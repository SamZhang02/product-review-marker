from collections import defaultdict
import os
from extractor import Extractor
from rater import Rater
from multiprocessing import Pool
import time

FILEPATH = os.path.join('data','data.csv')
OUTPATH = os.path.join('out','result.csv')
PRODUCT_LABELS = ['reviewerID',
                  'asin',
                  'reviewerName',
                  'helpful',
                  'reviewText',
                  'overall',
                  'summary',
                  'unixReviewTime',
                  'reviewTime']

RATING_CRITERIAS = ["Product quality",
                  "Difficulty using the product",
                  "Affordability",
                  "Cable / accessories quality",
                  "Sound quality",
                  "On-time delivery",
                  "Ease to return product",
                  "Returning customer satisfaction",
                  "Product appearance",
                  "Ease to reach customer service",
                  "Will purchase again",
                  "Adjustability",
                  "Good quality for the price",
                  "Package integrity"]

def main():
  extractor = Extractor()
  rater = Rater()

  products = extractor.extract_data(FILEPATH)
  ratings = defaultdict(list)

  t0 = time.time()

  with Pool(10) as p:
    ratings = p.map(rater.rate_product, products)

  t1 = time.time()

  print(f'Finished benchmarking {len(products)} reviews in {t1-t0} seconds')

  result  = defaultdict(list)
  for rating in ratings:
    for k,v in rating.items():
      result[k] = v

  print(f'Writing result to {OUTPATH}')
  with open(FILEPATH,"r") as fobj:
    with open(OUTPATH,"w+") as outfile:
      outfile.write(",".join(PRODUCT_LABELS) + "," + ",".join(RATING_CRITERIAS) + ",\n")
      for line in fobj:
        if line.split(',')[0] == PRODUCT_LABELS[0]:
          continue
        if not result or line.split(',')[0] not in result:
          continue

        outfile.write(line.strip() + ",".join(
          list(map(str,result[line.split(',')[0]]))
          ) + ",\n")

if __name__ == "__main__":
  main()
