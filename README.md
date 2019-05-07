# _LISPAT_ - Lost in Space and Time

## _When Plagiarism is a Good Thing_

_Sr. Design Project – Medtronic_

**LISPAT** _(Lost in Space and Time)_ is built to convert documents from their common pdf/docx format to txt, allowing for the use of Natural Language Processing on the provided data, with the goal of finding _semantic similarities_ between two documents. Using methods such as text cleaning, top keyword counts, top ngram counts, and leveraging python libraries to get the most out of the data. It extracts the most valuable information from each document all in order to capture the original information, in a manner that preserves and increases its value, accessibility and usefulness.

**_IMPORTANT:_** Please scroll down for some important notes.

## 📒 Documentation

**Home** - LISPAT's Home Page

**API Reference** - Detailed reference for LISPAT's API

**Usage Guides** - How to use LISPAT and its features

## 💪 Features

- Converts 2 uploaded _pdf/docx/doc_ documents for comparison/analysis
- Finds top keywords in both documents
- Highlights selected top keywords
- Search for a keyword in specific document
- Visualize the document's term frequency on a graph
- Visualize the way that 2 documents use a particular word

### Using LISPAT

Follow the home page link above to access LISPAT.

**Notes about LISPAT.**

1. To clear a search, click "enter", once you have removed your search words.
   - Search words are case sensitive.
2. Selected keywords will contain any word that has the same character occurrences of the keyword.
   For example: the word `words` is contained within `keywords`. So keywords will show up in the term search.
   If you want to contain the whole word, please enter it in the search bar.
3. The documents will contain headers and footers from the pdf or docx document, due to the processing when
   converting the documents the data from each document is not perfectly formatted and some attributes may be
   missing.

### Using the Graph

The graph shows you the differences in the way the words are used in each document.

Top Right Corner: These are common words found in both documents, ideally you would want to find most of
your top terms in this corner.

Bottom Left Corner: These are the words least common words used by each document. They are rarely used.

Top Left Corner: These are the most frequent terms found in the 1st Document.

Bottom Right Corner: These are the most frequent terms found in the 2nd Document.

Selecting a term on the graph or column will show you where they were found in each document, with side by side
comparison.
---

## Packaging and Delivery

Docker

### Docker Hub

Note: To install docker please reference https://docs.docker.com/install/

```
> docker pull jbrummet/lispat:2.0.0
> docker tag jbrummet/lispat:2.0.0 lispat
> docker run -it -p 5000:5000 lispat
  open 0.0.0.0:5000 in the browser
```

### Docker locally

```
> cd path/to/{lispat}
> docker build . -t lispat
> docker run -it -p 5000:5000 lispat
open 0.0.0.0:5000 in the browser
```

LISPAT does have a fairly large docker file. The installation process does take
a minute since there are so many dependencies between both python and javascript.

Cheers,
Team LISPAT
