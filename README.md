# Quantify product reviews with GPT
My friend had an assignment where they had to go through 500 amazon reviews and give a -5 to 5 rating on 14 criterias for each review so they can run some regression on it afterwareds.

Obviously, I had to automate that.

The program uses OpenAI's gpt 3.5 turbo model to benchmark each review stored in a csv file according to the criterias, and adds the ratings to the end of each row.

## Example
```data/data.example.csv``` for an example of the input csv

```out/result.example.csv``` for an example of the output csv
