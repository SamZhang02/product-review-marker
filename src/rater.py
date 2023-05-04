import openai
from product import Product


class Rater:
  MIN_RATING = -5
  MAX_RATING = 5
  START_PROMPT = f"""
  You are GPT, a large language model trained by OpenAI.
  You will be given texts of consumer reviews of specific products purchased on Amazon.
  You will be given 1 review at a time, for each review, You must translate the verbal review into a rating ranging from {MIN_RATING} to {MAX_RATING} on each of the following criterias.
  1. Product quality
  2. Difficulty using the product
  3. Affordability
  4. Cable / accessories quality
  5. Sound quality
  6. On-time delivery
  7. Ease to return product
  8. Returning customer satisfaction
  9. Product appearance
  10. Ease to reach customer service
  11. Will purchase again
  12. Adjustability
  13. Good quality for the price
  14. Package integrity
  You will give me the rating in this exact format:
  1. Product quality: <rating>
  2. Difficulty using the product: <rating>
  3. Affordability: <rating>
  4. Cable / accessories quality: <rating>
  5. Sound quality: <rating>
  6. On-time delivery: <rating>
  7. Ease to return product: <rating>
  8. Returning customer satisfaction: <rating>
  9. Product appearance: <rating>
  10. Ease to reach customer service: <rating>
  11. Will purchase again: <rating>
  12. Adjustability: <rating>
  13. Good quality for the price: <rating>
  14. Package integrity: <rating>
  """

  def __init__(self,product_data:Product):
    openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": self.START_PROMPT}]
      )

    self.product_data = product_data

  def rate_product(product:Product):
    rating = 0
    return rating
