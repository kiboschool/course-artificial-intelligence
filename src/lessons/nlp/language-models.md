# Language Models
Before we begin discussing language models, I'd like you to take a minute and think about the term "model." What does it mean to you? What comes to mind when you hear the word "model"? How useful do you find having a model of something?

<Details>
<Summary>What is a Model?</Summary>
Not just yet. Take another minute and think more deeply about it.
<Details>
<Summary>Click here to see the answer</Summary>
When I hear the word "model," I usually think of a representation of something. It could be a physical representation, such as a miniature model of a building, or a conceptual representation, like a mathematical model of a system.

Models help us make sense of the world around us by capturing the essential features of a system and **abstracting** away the details that are not relevant to the problem at hand. 
This approach enables us to better understand the dynamics of the system, focus on the important factors, and perform various operations on it.

</Details>
</Details>


## What is a Language Model?
A language model is a representation of a language. We are interested in finding ways to represent languages so that machines can understand and process them. 

> One model I thought of while writing this section is one that represents sentences without any stop words or punctuation, with each word converted to its root form. How could this be useful? Well, this model could be used to compare sentences to see if they are similar or not, and perhaps even to compress text.

In the field of natural language processing (NLP), however, we are interested in more sophisticated models that can capture the entirety of a language and its dynamics. This helps us perform complex tasks such as machine translation, text summarization, and question answering.


## Rule-based Language Models
The natural starting point for developing language models is to turn to the field of linguistics, which has been the study of languages for centuries. This involves understanding how linguists have defined and represented languages over time.

A common method in this area mirrors how we typically learn languages in school. We study grammar rules, vocabulary, and syntax. We learn to construct sentences, use punctuation, and spell words correctly. This approach to language learning is rule-based.



## Grammar and Syntax
One method of teaching a computer to understand the structure of a natural language involves teaching it the rules of grammar and syntax. This constitutes the rule-based approach to language understanding.


> A formal grammar is a collection of rules for generating sentences in a language.

A **context-free grammar (CFG)** is a type of formal grammar that describes the syntactic structure of a language through a set of production rules. These rules dictate how various constituents (such as words, phrases, and sentences) can be combined to form grammatically correct sentences. A context-free grammar includes the following elements:

**Terminals**: These are the basic building blocks of the language, including words or punctuation symbols. Terminals are the most fundamental units of the language and cannot be broken down further. For instance, in English, terms like "cat", "dog", "run", and "jump" serve as terminals.

**Non-terminals**: These symbols represent categories of linguistic elements, such as noun phrases (NP), verb phrases (VP), Nouns (N), and verbs (V), among others. Non-terminals act as placeholders that can be substituted with terminals or other non-terminals in accordance with the production rules.

**Production Rules**: These rules outline how non-terminals can be expanded or substituted by other symbols (terminals or non-terminals). Each rule includes a non-terminal symbol on the left-hand side and a sequence of symbols (terminals or non-terminals) on the right-hand side.

To delve deeper into context-free grammars and their application in sentence generation, watch this informative video:


<iframe width="100%" height="450" src="https://www.youtube.com/embed/QAZc9xsQNjQ?si=yMLBk5kinJyvlTeU&amp;start=373&end=782" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The code sample below utilizes the Natural Language Toolkit (NLTK) library in Python to establish a context-free grammar (CFG) and parse sentences based on that grammar.

```python
import nltk

# Define a context-free grammar (CFG) for parsing sentences
grammar = nltk.CFG.fromstring("""
    S -> NP VP

    AP -> A | A AP
    NP -> N | D NP | AP NP | N PP
    PP -> P NP
    VP -> V | V NP | V NP PP

    A -> "big" | "blue" | "small" | "dry" | "wide"
    D -> "the" | "a" | "an"
    N -> "she" | "city" | "car" | "street" | "dog" | "binoculars"
    P -> "on" | "over" | "before" | "below" | "with"
    V -> "saw" | "walked"
""")

# Create a parser using the defined grammar
parser = nltk.ChartParser(grammar)

# Take an input sentence from the user
sentence = input("Sentence: ").split()
try:
    # Parse the sentence and generate parse trees
    for tree in parser.parse(sentence):
        tree.pretty_print()
except ValueError:
    # If no parse tree is possible, inform the user
    print("No parse tree possible.")
```

In this approach, we manually feed the computer with the rules of grammar and syntax. This method, however, has its limitations, as it is challenging to formulate rules that cover all possible sentences in a language. Additionally, accounting for the inherent ambiguity of human language poses a significant challenge.


### Statistical Language Models
You might already have an idea of what this entails. Isn't it similar to the approach we've been discussing throughout this course? We either hard-code the rules or—what's the other option? Yes, we use data to learn the rules or identify patterns.

Statistical language models are predicated on the notion that language behaves as a statistical phenomenon. These models employ statistical techniques to discern patterns and structures within a language from a vast corpus of textual data.

In statistical language models, rather than handling the entirety of the text data at once, we can adopt the n-gram methodology we explored earlier. This strategy involves segmenting the text into smaller fragments to learn patterns within each segment. This forms the basis of statistical language models. For instance:

Consider the sentence "I am going to the   ". A statistical language model might predict that the next word is "store" with considerable probability because the phrase "going to the store" frequently occurs in English.

Or take the sentence "no the dark eat banana." A statistical language model could indicate that this sequence is likely not a valid English sentence. It might even suggest a more grammatically correct version of the sentence if possible.


Here's an interesting example involving the use of a Markov chain statistical model to generate text:

<iframe width="100%" height="450" src="https://www.youtube.com/embed/QAZc9xsQNjQ?si=0YVWCQ6S2haP9HOu&amp;start=1018&end=1149" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The code used in the video is available [here](https://cdn.cs50.net/ai/2023/x/lectures/6/src6/markov/)

> A Markov chain represents a mathematical model that transitions from one state to another among a finite or countable number of possible states.




Watch this video for a slightly different take on statistical language models:
<iframe width="100%" height="450" src="https://www.youtube.com/embed/W0TcVrI_vRg?si=kLOKe0qPrF4skyBX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## Neural-Networks-based Language Models
Another approach to language modeling leverages neural networks to model the probability distribution over words in a sentence. Beyond this, we can employ various types of neural networks to learn different aspects, capture distinct patterns, and address a wide array of problems.

Watch this video to learn about neural network-based language models and how RNNs and Transformers are used in language modeling:

<iframe width="100%" height="450" src="https://www.youtube.com/embed/QAZc9xsQNjQ?si=avxuNlAWLiN5fVs_&amp;start=2433&end=3781" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Recurrent Neural Networks (RNNs)
One of the most favored neural network architectures for language modeling is the Recurrent Neural Network (RNN). Designed to process sequential data, such as word sequences in a sentence, RNNs are adept at capturing the context of a word within its sentence, rendering them particularly suitable for language modeling tasks.

An advancement in language models involves the application of RNNs, especially **Long Short-Term Memory (LSTM)** networks, to model the probability distribution across words. We have a practice on this topic in the next section.

### Transformers

The inherent sequential nature of RNNs introduces inefficiencies when processing lengthy data sequences, such as extended sentences or documents. This inefficiency stems from the vanishing gradient problem, hindering the network's ability to recognize long-range dependencies within the data. In response, researchers have devised more sophisticated neural network architectures like **transformers**, optimized for efficiently handling long data sequences.

**Transformers** employ the **attention** mechanism, enabling the model to concentrate on different segments of the input sequence during prediction. This model has attained unparalleled performance, forming the backbone of the most advanced language models, including BERT, GPT-2, and GPT-3.

## Large Language Models
A "large" language model is typically characterized by its training on a vast dataset. The term "large" reflects not just the dataset's volume but also its complexity and diversity. These models are developed on extensive text corpora, potentially comprising billions or even trillions of words, gathered from a variety of sources like books, articles, websites, and other text repositories. Training on such broad datasets allows the model to acquire a comprehensive understanding of natural language, encompassing syntax, semantics, and contextual subtleties, often resulting in more accurate and robust models capable of efficiently performing a plethora of natural language processing tasks.

Training large language models requires considerable computational resources, such as powerful GPUs or TPUs, alongside expansive distributed training infrastructure. This process usually involves executing millions of iterations of the training algorithm, tuning the model parameters based on the gradients of the loss function relative to the parameters.

### Language Models Examples

Modern language models such as Google's BERT, OpenAI's GPT series, Facebook AI's RoBERTa, and Palm's T5 signify progress in natural language processing.

**BERT** revolutionized understanding bidirectional context through its transformer architecture, enhancing performance in tasks like text classification and named entity recognition.

The **GPT** series, notably GPT-3, is celebrated for its autoregressive approach, sequentially generating coherent text based on preceding tokens. RoBERTa refined BERT's architecture, enhancing pre-training methods for better efficacy in tasks such as sentiment analysis and machine translation.

**T5** marked a significant advancement by treating all NLP tasks as text-to-text tasks, thus enabling a unified approach to handling diverse tasks and facilitating adaptation to new domains. T5's adaptability, scalability, and its integration of transformer architecture with a multi-task learning approach, establish it as a cutting-edge solution for a broad range of language processing challenges.



## Large Language Models Resources
For those keen on delving deeper into large language models, the following resources are invaluable:
- [Large Language Models From Scratch](https://www.youtube.com/watch?v=lnA9DMvHtfI)
- [How to Train a new Language Model](https://huggingface.co/blog/how-to-train)
- [How to Build a Large Language Model from Scratch Using Python](https://www.freecodecamp.org/news/how-to-build-a-large-language-model-from-scratch-using-python/)
- [Creating a Large Language Model from scratch: A beginner's guide](https://www.pluralsight.com/resources/blog/data/how-build-large-language-model)
- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- [T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)


