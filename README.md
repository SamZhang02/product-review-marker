# Quantify product reviews with GPT
My friend had an assignment where they had to manually go through 500 amazon reviews and give a -5 to 5 rating on 14 criterias for each review so they can run some regression on it afterwareds.

#### *Of course we are not doing that lmao.*

---

The program uses OpenAI's gpt 3.5 turbo model to benchmark each review stored in a csv file according to the criterias, and appends the ratings to the end of each row.

## Docs
For an example of the input csv:
```
data/data.example.csv
``` 
For an example of the output csv
```
out/result.example.csv
``` 
You can view each criteria being rated in 
```
data/criteria.json
```

## Usage
This project uses `poetry` to manage dependencies.

Make a `.env` file according to `.env.example`
Install dependencies with
```
poetry install
```
or
```
just install
```

Run with
```
poetry run main.py
```
or
```
just main
```

