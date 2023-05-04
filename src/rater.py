import os

import openai
from dotenv import load_dotenv

from product import Product

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

class Rater:
  MIN_RATING = -5
  MAX_RATING = 5
  START_PROMPT = f"""
  I am a product review benchmarker.
  I will be given texts of consumer reviews of musical instruments purchased on Amazon.
  I will be given 1 review at a time, for each review, I must translate the verbal review into a rating ranging from {MIN_RATING} to {MAX_RATING}, where a positive 5 means extremely positive experience; a negative 5 indicates extremely negative experience. If the review does not mention anything on that criteria, the rating is 0.
  on each of the 14 following criterias,
  while keeping in mind that the review is about a music instrument.
  I will give respond the rating in this exact format:
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

  def __init__(self):
    self.start_prompt = {"role": "user", "content": self.START_PROMPT}

  def parse_review(self,review:str):
    review = review.split("\n")
    ratings = []
    for line in review:
      try:
        rating = line.split(":")[1].strip()
      except:
        raise ValueError(f'Could not parse rating from line: {line}, bad input?')
      ratings.append(int(rating))

    return ratings

  def rate_product(self, product:Product):
    print(f'Rating review from reviewerId: {product.reviewerID}')
    try:
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          self.start_prompt,
          {"role":"user","content":product.reviewText}
          ]
        )

      review = response["choices"][0]["message"]["content"]

      return {product.reviewerID:self.parse_review(review)}

    except:
      return {product.reviewerID:[]}
