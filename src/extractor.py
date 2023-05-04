import pandas as pd
from product import Product

class Extractor:
  DATATYPE = 'csv'

  def _extract_csv(self, filepath:str) -> pd.DataFrame:
      return pd.read_csv(filepath)

  def extract_data(self, filepath:str) -> list[Product]:
      if self.DATATYPE == 'csv':
        raw_data = self._extract_csv(filepath)
        return list(map(lambda x: Product(x), raw_data.values))
      else:
        raise ValueError(f'Invalid data type, the datatype must be {self.DATATYPE}')

if __name__ == "__main__":
  extractor = Extractor()
  products = extractor.extract_data('data/data.csv')
  print(len(products))
  print(products[0].ratings)
  # print('\n'.join(list(map(lambda x: x.reviewText, products))))

