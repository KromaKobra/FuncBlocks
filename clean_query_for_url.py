# Turn name into a string that is url ready (Replace invalid characters with escape codes)
def clean_for_url(messy: str) -> str:
    char_codes = {
        ' ': "%20", '#': "%23", '&': "%26", '?': "%3F", '/': "%2F", '\\': "%5C",
        '<': "%3C", '>': "%3E", '%': "%25", '{': "%7B", '}': "%7D", '[': "%5B",
        ']': "%5D", '|': "%7C", '^': "%5E", '~': "%7E", '@': "%40", ':': "%3A",
        ';': "%3B", '=': "%3D", '+': "%2B"
    }
    clean = ""
    for char in messy:
        if char in char_codes:
            clean += char_codes[char]
        else:
            clean += char
    return clean

# I was going to use this for a project I'm working on, but then found out that the built in module:
# urllib has a module called parse that has a function called quote. Quote can be used to do this automatically :P