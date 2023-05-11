from collections import defaultdict
import os
from extractor import Extractor
from rater import Rater
from multiprocessing import Pool
import time
import json

FILEPATH = os.path.join('data','data.example.csv')
OUTPATH = os.path.join('out','result.csv')

with open(FILEPATH,'r') as data:
  PRODUCT_LABELS = data.readline().strip().split(',')

with open(os.path.join('data','criterias.json'),'r') as criterias:
  RATING_CRITERIAS = json.load(criterias)

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

  result = defaultdict(list)
  for rating in ratings:
    for k,v in rating.items():
      result[str(k)] = v

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
