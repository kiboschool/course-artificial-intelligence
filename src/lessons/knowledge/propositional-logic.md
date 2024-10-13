
# Propositional Logic
Propositional logic is a type of logic that deals with propositions. A proposition is a statement that is either true or false. For example, "Kibo is an institution that allows students to earn a degree in Computer Science." is a proposition, and it is true. "The sky is green" is also a proposition, but it is false. 

<aside>
This concept of propositional logic, including the evaluation of statements as true or false, is fundamental to what we studied in our discrete math class, particularly when exploring the foundations of mathematical reasoning and computation.
</aside>

## Propositional Symbols
In propositional logic, we use variables (or symbols) to represent propositions. For example, we can use the variable **p** to represent the proposition "Kibo is an institution that allows students to earn a degree in Computer Science." and the variable **q**  to represent the proposition "The sky is green". We can then use logical operators to combine these propositions. 

## Premises 
In logic, the term "premises" refers to the statements or propositions that are **assumed to be true** in an argument or inference. 

## Sentences
A sentence is a combination of propositions and logical operators. For example, the sentence "The sky is blue and it is daytime" is a combination of the propositions "The sky is blue" and "It is daytime" using the logical operator "and".


## Logical Connectives
Logical connectives are operators that can be used to combine propositions. The main logical connectives are:

- **Negation or Not (¬)**: This operator takes a proposition and returns its negation. For example, if p is the proposition "The sky is blue", then ¬p is the proposition "The sky is not blue".

- **Conjunction or And (∧)**: This operator takes two propositions and returns their conjunction. For example, if p is the proposition "The sky is blue" and q is the proposition "It is daytime", then p ∧ q is the proposition "The sky is blue and it is daytime".

- **Disjunction or Or (∨)**: This operator takes two propositions and returns their disjunction. For example, if p is the proposition "The sky is blue" and q is the proposition "The sky is green", then p ∨ q is the proposition "The sky is blue or the sky is green".

- **Implication (→)**: This operator takes two propositions and returns their implication (if...then). For example, if p is the proposition "The sky is blue" and q is the proposition "It is daytime", then p → q is the proposition "If the sky is blue, then it is daytime".

- **Biconditional (↔)**: This operator takes two propositions and returns their biconditional. For example, if p is the proposition "The sky is blue" and q is the proposition "The sky is green", then p ↔ q is the proposition "The sky is blue if and only if the sky is green".


# Truth Tables

Truth tables are tables that show the truth value of a compound proposition for all possible combinations of truth values of its components. For example, the truth table for the conjunction p ∧ q is:

| p     | q     | p ∧ q |
|-------|-------|-------|
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |

The truth table for the implication p → q is:

| p     | q     | p → q |
|-------|-------|-------|
| True  | True  | True  |
| True  | False | False |
| False | True  | True  |
| False | False | True  |

The truth table for the biconditional p ↔ q is:

| p     | q     | p ↔ q |
|-------|-------|-------|
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | True  |


## Knowledge Base (KB)
In the context of propositional logic, A knowledge base is a set of propositions that represent the facts and rules about the world. For example, the knowledge base for the medical diagnosis assistant we mentioned earlier might contain the following proposition:

"If a person exhibits sneezing and a runny nose but no fever, it is certain that they have allergies."

Which can be represented as: 
( S ^ R ^ ¬F ) → A

Where:

- S: A person has sneezing.
- R: A person has a runny nose.
- F: A person has fever.
- A: A person has allergies.

It represents the rule that if a person has sneezing and a runny nose, but no fever, then they have allergies.

You can write a simple python code to represent the above knowledge base and query it just by using if else statements. However, in real-world problems, the knowledge base can be very large and complex, and so it is not practical to use if else statements to represent it. This is where logic-based knowledge representation comes in handy.

Representing the facts and the rules, as we did above, is a cruical step in building an intelligent system that can reason about the world. The next step will be using algorithms to draw conclusions from the knowledge base.

Watch this video for another example:
<iframe width="100%" height="450" src="https://www.youtube.com/embed/HWQLez87vqM?si=nmJWvW_D6mcFwgvD&amp;start=104&end=212" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### Code Example
Let's write a simple python code to represent the medical diagnosis knowledge base we mentioned earlier and query it.

```python
# colab notebook for this code is available here: 
# https://colab.research.google.com/drive/1DQMAZz8j_-OeZ932crsQE3hIukBFBSr2

# Define symbols
S = Symbol("Sneezing")
R = Symbol("RunnyNose")
F = Symbol("Fever")
A = Symbol("Allergies")


# Construct the knowledge base
knowledge = Implication(And(S, R, Not(F)), A)

# a set of propositions that represent a possible state about the world that we can query next
model = And(And(S, R), Not(F))

# query to ask
query = Implication(model, A)

# Check if the knowledge base entails the person has allergies
# can we imply A (Allergies) from the model ( S ^ R ^ ¬F )?
result = model_check(knowledge, query)

print("Does the person have allergies?", result)
```
In the above code, we define the symbols S, R, F, and A to represent the propositions "A person has sneezing", "A person has a runny nose", "A person has fever", and "A person might have allergies", respectively. 

We then construct the query to represent the question "Does the person have allergies if they have sneezing and a runny nose, but no fever?". 

The code used the `model_check` function to check if the knowledge base entails the query. We will discuss the `model_check` function in the next section.

## Entailment
The result of the above program is `True`, which means that the knowledge base **entails** the query, and so the person has allergies.

**Entailment** is the relationship between a knowledge base and a query. A knowledge base entails a query if the query is true in the knowledge base.

The notation for entailment is `|=`. For example, if KB is the knowledge base and q is the query, then `KB |= q` means that the knowledge base entails the query.



## Test Your Understanding
### Q1. In the context of a knowledge base (KB) in propositional logic, what does the expression (S ∧ R ∧ ¬F) → A signify given the propositions S: Sneezing, R: Runny Nose, F: Fever, A: Allergies?
- A) If a person has sneezing, a runny nose, and no fever, then they have allergies.
- B) A person with a fever, sneezing, and a runny nose has allergies.
- C) Sneezing and a runny nose are sufficient to conclude allergies, regardless of fever.
- D) If a person has allergies, they will have sneezing, a runny nose, and no fever.


### Q2. Consider the propositions p: "The sky is blue", q: "It is raining". Which of the following represents the statement "If the sky is blue, then it is raining"?

- A) p → q
- B) p ∧ q
- C) p ∨ q
- D) p ↔ q

### Consider the propositions p: "The sky is blue", q: "It is raining". Which of the following represents the biconditional 'p if and only if q'?
- A) p → q
- B) p ∧ q
- C) p ∨ q
- D) p ↔ q

<Details>
<Summary>Answer</Summary>
Q1. The correct answer is A) If a person has sneezing, a runny nose, and no fever, then they have allergies.

Q2. The correct answer is A) p → q

Q3. The correct answer is D) p ↔ q
</Details>


## Summary
- Propositional logic is a type of logic that deals with propositions.
- A proposition is a statement that is either true or false.
- Propositional logic uses variables (or symbols) to represent propositions.
- Logical connectives are operators that can be used to combine propositions.
- A knowledge base is a set of propositions that represent the facts and rules about the world.
- Entailment is the relationship between a knowledge base and a query. A knowledge base entails a query if the query is true in the knowledge base.



<!-- 
video that exlains all in one
https://www.youtube.com/watch?v=nLU-4Zc626g -->