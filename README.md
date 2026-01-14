# NLP Course - Learning Summary

## NLTK - Natural Language Processing

**Overview:** Open-source Python library for computational linguistics and text analysis.

### What I Learnt:
- **Analysed texts** from established corpora (Gutenberg, Brown)
- **Tokenised** sentences into constituent words and punctuation marks
- **Removed stopwords** (high-frequency function words like "the", "is", "a")
- **Lemmatised** words to their canonical forms (e.g., "bats" → "bat", "feet" → "foot")
- **Applied POS tagging** to identify grammatical categories (nouns, verbs, adjectives)
- **Computed** word frequencies and lexical statistics
- **Discovered** word concordances, collocations, and semantic similarities
- **Scraped** web content and extracted plain text from HTML documents

### Essential Functions:
```python
nltk.word_tokenize()       # Segment text into tokens
WordNetLemmatizer()        # Reduce words to base forms
nltk.pos_tag()            # Label parts of speech
FreqDist()                # Calculate word frequencies
stopwords.words()         # Filter common words
BeautifulSoup()           # Parse HTML content
```

---

## Pandas - Data Wrangling & Analysis

**Overview:** Python library for structured data manipulation and statistical analysis.

### Projects Completed:

#### Dataset 1: Euro 2012 Football Statistics
- Loaded CSV data into DataFrame structures
- Explored dataset characteristics (dimensions, columns, data types)
- Selected specific columns and rows using indexing
- Sorted data by multiple criteria hierarchically
- Calculated descriptive statistics (mean, minimum, maximum)
- Applied conditional filtering for targeted analysis

#### Dataset 2: Film Industry Database (Cast & Release Information)
- Integrated multiple related datasets
- Eliminated duplicate records
- Filtered by temporal ranges and lexicographic order
- Computed value frequencies using `value_counts()`
- Implemented multi-index DataFrames for complex hierarchical queries
- Exported processed datasets to CSV format

#### Dataset 3: Global Alcohol Consumption Patterns
- Grouped data by categorical variables
- Calculated aggregate statistics per group
- Generated comprehensive summary statistics

### Core Operations:
```python
df.head()                          # Preview initial records
df[['col1', 'col2']]              # Column selection
df[df['year'] == 1950]            # Boolean indexing
df.sort_values()                   # Data sorting
df.groupby('category').mean()      # Aggregation by group
df['column'].value_counts()        # Frequency distribution
df.iloc[:, :7]                    # Position-based indexing
```

---

## Regular Expressions - Pattern Recognition & Text Processing

**Overview:** Declarative language for sophisticated string pattern matching and manipulation.

### Skills Developed:
- Matched complex character sequences and patterns
- Validated structured data formats (email addresses, dates, numerical formats)
- Extracted numerical data from unstructured text
- Sanitised text (removed non-alphanumeric characters, normalised whitespace)
- Constructed custom validators for domain-specific requirements

### Pattern Syntax Mastered:
- `\d` - any digit [0-9]
- `\w` - alphanumeric characters [a-zA-Z0-9_]
- `\s` - whitespace (spaces, tabs, newlines)
- `*` - zero or more repetitions
- `+` - one or more repetitions
- `?` - zero or one repetition
- `^` - start of string anchor
- `$` - end of string anchor
- `[abc]` - character class
- `{m,n}` - bounded quantifier

### Validators Implemented:
- Email address format checker
- ISO date validator (YYYY-MM-DD)
- Integer and fraction format validators
- Text normalisation utilities
- Numerical data extractors

### Essential Methods:
```python
re.search()     # Locate pattern anywhere in string
re.match()      # Match pattern at string beginning
re.findall()    # Extract all pattern occurrences
re.sub()        # Substitute matched patterns
re.split()      # Split string by pattern delimiter
re.compile()    # Precompile pattern for efficiency
```

---

## Key Competencies Acquired

Through this coursework, I developed proficiency in:

1. **Natural Language Processing** - Tokenisation, lemmatisation, POS tagging, and frequency analysis using NLTK
2. **Data Analysis & Manipulation** - Filtering, grouping, aggregation, and statistical analysis using Pandas
3. **Pattern Matching & Text Mining** - Validation, extraction, and text normalisation using Regular Expressions

These foundational skills form the cornerstone of computational linguistics and data science workflows.
