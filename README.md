# Manual Tweets Scrapper

## Description

These are just simple scripts to scrape tweets and then do some analysis. Here, we try to search for IPL tweets and then analyse them using Gemini LLM. You can use the js snippets for scraping and further do your own analysis.

## Steps

1. Goto Twitter [Explore](https://twitter.com/explore) section - https://twitter.com/explore

2. Add the snippets `scrape.js` and `auto_scroll.js` in your chrome devtools as snippets under `sources` section.

3. Search for your query, try to use twitter advanced search to filter out spam tweets and to use other filters. Highly recommended.

4. Run the `scrape` snippet.

5. Run the `auto_scroll` snipper.

6. Wait until you feel satisfied with the number of tweets scrapped. You can look at console to see the logs.

7. Once you get rate limited or you search bot, try log the variable `tweets` in the console. You can then right click and choose copy object.

8. In the `data/` folder create a new JSON file and paste your object in there.

9. Now you can merge all the files into one by running `merge.py` script.

10. Run the `run_genai.py` file after entering your Gemini API key in it. This will run through the tweets and create a file `analysed.json` in `results/` directory.

11. Use `preprocess.py` to make sure the results data is in consistent format.
