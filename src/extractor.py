import pandas as pd
from product import Product

class Extractor:
  DATATYPE = 'csv'

  def _extract_csv(self, filepath:str) -> pd.DataFrame:
      return pd.read_csv(filepath)

  def extract_data(self, filepath:str) -> list[Product]:
      raw_data = self._extract_csv(filepath)
      return list(map(lambda x: Product(x), raw_data.values))
