import re 

test_string = "fooaaabcde0"

# 1.1 An 'a' followed by zero or more b's
pattern = r'ab*'
First = re.search(pattern, test_string)
print(First)

# 1.2 An 'a' followed by one or more b's
pattern2 = r'ab+'
second = re.search(pattern2, test_string)
print(second)

# 1.3 An 'a' followed by zero or one b's
pattern3 = r'ab?'
third = re.search(pattern3, test_string )
print(third)

# 1.4 An 'a' followed by exactly three b's
pattern4 = r'ab{3}'
fourth = re.search(pattern4, test_string)
print(fourth)

# 1.5 A string that contains only letters and digits
pattern5 = r'^[a-zA-Z0-9]+$'
fifth = re.search(pattern5, test_string)
print(fifth)

# 1.6 A string that starts with a word character
pattern6 = r'^\w+'
sixth = re.search(pattern6, test_string)
print(sixth)

# 1.7 A string that ends with a word character
pattern7 = r'\w+$'
seventh = re.search(pattern7, test_string)
print(seventh)

# 1.8 A string that contains at least one vowel
def has_vowel(test_string):
    return(bool(re.search(r'[aeiouAEIOU]', test_string)))   
print(has_vowel(test_string))

# 1.9 Returns True if the string represents an integer
def is_integer(test_string):
    pattern = r'^-?\d+$'
    return(bool(re.fullmatch(pattern, test_string)))
print(is_integer(test_string))

# 1.10 Returns True if the string represents a valid fraction
def is_fraction(test_string):
    pattern = r'^-?\d+/\d*[1-9]\d*$'
    return bool(re.fullmatch(pattern, test_string))
print(is_fraction(test_string))

# 1.11 Separates and returns all numbers from a string
def extract_numbers(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    return [int(num) for num in numbers]
print(extract_numbers(test_string)) 

# 1.12 Valid Date (YYYY-MM-DD format)
def is_valid_date(text):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.fullmatch(pattern, text))
print(is_valid_date(test_string))

# 1.13 Normalise Whitespace
def normalise_whitespace(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text).strip()
print(normalise_whitespace(test_string))

# 1.14 Remove non-alphanumeric
def remove_non_alphanumeric(text):
    pattern = r'[^a-zA-Z0-9]'
    return re.sub(pattern, '', text)
print(remove_non_alphanumeric(test_string))

# 1.15 Valid e-mail
def is_valid_email(text):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9.]+\.(edu|com|ord|net)$' # Using 'ord' as stated in the question (should this be 'org'?)
    return bool(re.fullmatch(pattern, text))
print(is_valid_email(test_string))

