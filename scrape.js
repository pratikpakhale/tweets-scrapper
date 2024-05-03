const uniqueTweetIdentifiers = new Set();
const tweets = [];

function saveTweets() {
  const tweetsElements = document.querySelectorAll(
    'article[data-testid="tweet"]'
  );
  tweetsElements.forEach(tweetElement => {
    const textElement = tweetElement.querySelector(
      'div[data-testid="tweetText"]'
    );
    const text = textElement ? textElement.innerText : '';
    const image = tweetElement.querySelector('img');
    const url = image ? image.getAttribute('src') : '';

    if (!uniqueTweetIdentifiers.has(text.trim())) {
      console.log('added a tweet');
      tweets.push({ text, url });
      uniqueTweetIdentifiers.add(text.trim());
    }
  });
}

const observer = new MutationObserver(mutationsList => {
  mutationsList.forEach(mutation => {
    mutation.addedNodes.forEach(addedNode => {
      saveTweets();
    });
  });
});

observer.observe(document.body, { childList: true, subtree: true });
