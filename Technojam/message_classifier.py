# 1. Define common stop words to ignore
STOP_WORDS = ["the", "is", "at", "which", "and", "to", "a", "an", "for", "my", "i",
              "me", "was", "are", "it", "on", "in", "of", "this", "that", "with"]

def clean_and_tokenize(text):
    """Convert text to lowercase, split into words, and filter out stop words."""
    text = text.lower()
    # Strip basic punctuation so "crashes." doesn't slip past "crashes"
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    words = text.split()
    keywords = [word for word in words if word not in STOP_WORDS]
    return keywords

def classify_message(text):
    """Get filtered keywords and use if-else logic to classify the message."""
    keywords = clean_and_tokenize(text)

    if any(word in keywords for word in ["crash", "crashes", "bug", "broken", "error"]):
        category = "Technical Support"
    elif any(word in keywords for word in ["bill", "billed", "charged", "payment", "subscription"]):
        category = "Billing Support"
    else:
        category = "General Inquiry"

    return keywords, category

# ---- Test the script ----
test_messages = [
    "the app crashes every time I open it",
    "I was charged twice for my subscription this month",
    "What are your business hours on weekends?",
    "There is a broken link on the homepage",
    "Can you tell me more about your pricing plans?"
]

for msg in test_messages:
    keywords, result = classify_message(msg)
    print(f"Message: {msg}")
    print(f"Filtered Keywords: {keywords}")
    print(f"Classification: {result}")
    print("-" * 50)