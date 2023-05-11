import os

import openai
from dotenv import load_dotenv

from product import Product

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

class Rater:
  with open(os.path.join('data','prompt.txt'),'r') as prompt:
    START_PROMPT = prompt.read()

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
    print(f'Rating review {product.ratingId}')
    try:
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          self.start_prompt,
          {"role":"user","content":product.content}
          ]
        )

      review = response["choices"][0]["message"]["content"]

      return {product.ratingId:self.parse_review(review)}

    except:
      return {product.ratingId:[]}
