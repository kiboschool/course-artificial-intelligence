# Practice: KB Representation

Open the Colab notebook below and complete the following exercise:

Extend the knowledge base in the notebook to include the following two rules:

1. If a person exhibits fever, cough, and body aches, it is certain that they have the flu.

2. If a person exhibits cough and a runny nose, but no fever, it is certain that they have a common cold.






</br>

<a href = "https://colab.research.google.com/drive/1DQMAZz8j_-OeZ932crsQE3hIukBFBSr2" target="_blank" >
<img src="https://img.shields.io/static/v1?label=Open%20Practice&message=KB%20Representation&color=yellow"/>
</a>

<Details>
<Summary> Possible Solution</Summary>

```python
# Define symbols
S = Symbol("Sneezing")
R = Symbol("RunnyNose")
F = Symbol("Fever")
A = Symbol("Allergies")
C = Symbol("Cough")
B = Symbol("BodyAches")

# Construct the knowledge base
knowledge = And(
    Implication(And(S, R, Not(F)), A),  # Rule for allergies
    Implication(And(F, C, B), Symbol("Flu")),  # Rule for flu
    Implication(And(C, R, Not(F)), Symbol("CommonCold"))  # Rule for common cold
)

# Questions
questions = [
    (And(F, C), "Does the person have a common cold?"),  # Question 1
    (And(F, B, C), "Does the person have a common cold?"),  # Question 2
    # Add more questions here
]

# Check each question against the knowledge base
for query, question_text in questions:
    result = model_check(knowledge, query)
    print(question_text, result)
```
</Details>


