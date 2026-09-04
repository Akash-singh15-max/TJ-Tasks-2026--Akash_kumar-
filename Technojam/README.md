## 🧠 Approach & Algorithm

### 1. Stop word removal — `clean_and_tokenize(text)`
Real customer messages are full of words that carry no topical meaning
("the", "is", "my", "to", etc.). Before any classification can happen, the
text needs to be reduced to its meaningful keywords.

Steps:
1. Lowercase the entire message (so "Crash" and "crash" are treated the same).
2. Strip basic punctuation (`. , ! ? ; :`) so words like `"crashes."` aren't
   missed just because of a trailing period.
3. Split the string into individual word tokens using `str.split()`.
4. Filter out any token that appears in the `STOP_WORDS` list, leaving only
   the "signal" words.


### 2. Rule-based classification — `classify_message(text)`
Once the message is reduced to keywords, it is passed through a manual
decision tree implemented with `if / elif / else`:

```
if any technical keyword ("crash", "bug", "broken", "error") is present:
    → "Technical Support"
elif any billing keyword ("bill", "charged", "payment", "subscription") is present:
    → "Billing Support"
else:
    → "General Inquiry"
```



## 📂 Files

| File | Description |
|---|---|
| `message_classifier.py` | Main script: stop-word filtering + rule-based classifier + test cases |
| `README.md` | This file |

## ▶️ How to run

```bash
python3 message_classifier.py
```

## 📸 Sample Output

```
Message: the app crashes every time I open it
Filtered Keywords: ['app', 'crashes', 'every', 'time', 'open']
Classification: Technical Support
--------------------------------------------------
Message: I was charged twice for my subscription this month
Filtered Keywords: ['charged', 'twice', 'subscription', 'month']
Classification: Billing Support
--------------------------------------------------
Message: What are your business hours on weekends?
Filtered Keywords: ['what', 'your', 'business', 'hours', 'weekends']
Classification: General Inquiry
--------------------------------------------------
Message: There is a broken link on the homepage
Filtered Keywords: ['there', 'broken', 'link', 'homepage']
Classification: Technical Support
--------------------------------------------------
Message: Can you tell me more about your pricing plans?
Filtered Keywords: ['can', 'you', 'tell', 'more', 'about', 'your', 'pricing', 'plans']
Classification: General Inquiry
--------------------------------------------------
```

The screenshot of the output is given below :-
`message_classifier.png`