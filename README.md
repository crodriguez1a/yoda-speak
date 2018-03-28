# yoda-speak
Code-Heads Club | Clinic | Python | Learn to convert English to Yodish using spaCy

### "I will take you to him"
### "Take you to him I will"

## Setup

With Pip and [Python](https://docs.brew.sh/Homebrew-and-Python) installed:

**Source files**:

```bash
git clone https://github.com/crodriguez1a/yoda-speak.git

cd path/to/yoda-speak
```

**Virtualenv**:

```bash
pip install virtualenv

virtualenv venv

source venv/bin/activate
```

**Spacy**:

```bash
pip install spacy && python -m spacy download en
```


## Reference:

- [Spacy](http://spacy.io) is a natural language processing package
- [Yoda Jeff](http://www.yodajeff.com/pages/talk/yodish.shtml) is an expert on Yoda and Yodish speech patterns
- [Python](https://www.python.org/) is a programming language that lets you work quickly
and integrate systems more effectively.


## Glossary:

**Spacy - Universal Part-of-speech Tags**

| POS        | DESCRIPTION | EXAMPLES |
| ------------- |:-------------:|:-------------:|
| ADJ |	adjective |	big, old, green, incomprehensible, first |
| ADP |	adposition |	in, to, during |
| ADV |	adverb |	very, tomorrow, down, where, there |
| AUX |	auxiliary |	is, has (done), will (do), should (do) |
| CONJ |	conjunction |	and, or, but |
| CCONJ |	coordinating conjunction |	and, or, but |
| DET |	determiner |	a, an, the |
| INTJ |	interjection |	psst, ouch, bravo, hello |
| NOUN |	noun |	girl, cat, tree, air, beauty |
| NUM |	numeral |	1, 2017, one, seventy-seven, IV, MMXIV |
| PART |	particle |	's, not, |
| PRON |	pronoun |	I, you, he, she, myself, themselves, somebody |
| PROPN |	proper noun |	Mary, John, Londin, NATO, HBO |
| PUNCT |	punctuation |	., (, ), ? |
| SCONJ |	subordinating conjunction |	if, while, that |
| SYM |	symbol |	$, %, §, ©, +, −, ×, ÷, =, :), 😝 |
| VERB |	verb |	run, runs, running, eat, ate, eating |
| X |	other |	sfpksdpsxmsa |
| SPACE |	space | |

**Yoda Jeff - Parts-of-speech Shorthand**

| Symbol        | Definition |
| ------------- |:-------------:|
| S | subject |
| V | verb |
| deepV | dependent verb |
| Adj | adjective |
| Adv | adverb |
| con | conjunction |
| pp | preposition |
| DO | direct object |
| IO | indect object |
| O | objects as a whole |
| ObP | object of a preposition |
| PM | predicate modifier |
| I | interrogative |
| poss | possessive |
| neg | negation of a verb |
| pDO | phrase acting as a direct object |

Examples:

```
"Take you to him I will" => (V+DO+pp+ObP+S+ depV)
```

```
"A teacher will I be" => (PM+depV+S+V)
```

```
"Soon parents will Sharon and Eric be" => (Adv+PM+depV+S+V)
```

```
"Strong you are..." => (PM+S+ beingV)
```

```
"...reckless is he" => (PM+beingV+ S)
```
