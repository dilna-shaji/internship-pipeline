def clean_text(text):
    return text.strip().lower() if text else ""

def is_india_internship(role_text, location_text):
    role_clean = clean_text(role_text)
    loc_clean = clean_text(location_text)
    is_intern = any(kw in role_clean for kw in ["intern", "internship", "apprentice"])
    is_in_india = any(kw in loc_clean for kw in ["india", "remote", "mumbai", "bangalore", "bengaluru", "delhi", "pune", "hyderabad", "chennai", "kochi"])
    return is_intern and is_in_india

def normalize_location(location_text):
    loc = location_text.strip().title()
    if "Bengaluru" in loc or "Bangalore" in loc: return "Bangalore, India"
    if "Remote" in loc: return "Remote (India)"
    return loc
