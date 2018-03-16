# Usage:
Run interface.py in Python 2.7.
```
python2 interface.py
```


# Overview:

This is a disease ontology capturing most common diseases patients have, designed for instructional purposes:
- to better visualize diseases
- to observe an easy to understand and modify disease ontology
- less powerful but more understandable

## Steps to complete:
- [x] Research and gather data about most common diseases and categorize their:
  - symptoms
  - treatment options
- [ ] ~~Completely finish research on entire list for a more complete and comprehensive ontology~~
- [ ] ~~Instead of manually researching and gathering data about common diseases, write a Python file that searches and parses Google's medical Knowledge Representation to include symptoms and treatment options~~

- [ ] ~~Compile information into OWL-based ontology for clarity~~
- [ ] Specify how a user is to interact with the system,
  - [ ] to query for information on different diseases
  - [ ] ask deducing questions to deduce disease
  - [x] how to check any symptoms against what exists in ontology

- [ ] ~~Refine ontology such that synonyms can be accounted for (e.g. joint pain vs. pain in joints)~~
- [ ] ~~Add more subclasses and structure to symptoms and treatment~~
## Features:
- As user gives more info/data to the program, program will ask (differentiating) questions to narrow down a differential diagnosis (the process of differentiating between two or more conditions that share similar signs or symptoms) and present diseases matching these symptoms

## Tools:
- user interaction with ontology
  - [ ] ~~built in Protege~~
- interaction with user
  - [x] Python 2.7 ~~with Tkinter GUI~~
