# Inferring with Logic
Inference is the process of determining whether a given sentence can be derived from the knowledge base.

Assume a knowledge base with the following formulae:

`KB = ( A ∨ C ) ∧ (B ∨ ¬ C )`

It could be representing something like:

- A: It is raining.
- B: It is cloudy.
- C: You have an umbrella. 

And the knowledge base states that "It is raining or you have an umbrella" and "It is cloudy or you don't have an umbrella".

`KB = ( A ∨ C ) ∧ (B ∨ ¬ C )`


Our aim is to determine if the sentence `α = ( A ∨ B )` can be inferred from the knowledge base or not.

To solve similar problems, we need an inference algorithm. An inference algorithm is a procedure to determine whether a given sentence can be derived from the knowledge base.

There are several algorithms to perform inference in propositional logic. Some of the most common algorithms are:
- Truth Table
- Forward Chaining
- Backward Chaining
- Resolution


## Model Checking with Truth Table
The model checking approach uses truth tables for inference. It is a brute force algorithm that checks all possible interpretations of the knowledge base. The algorithm works as follows:

1. Create a truth table with all possible combinations of truth values for the propositional symbols in the knowledge base.

2. For each interpretation, check if the knowledge base entails the sentence α (i.e. sentence α evaluates to true whenever KB evaluates to true)

|  A   |  B   |  C   | A ∨ C | (B ∨ ¬C) |    KB     |  α   |
|------|------|------|-------|----------|-----------|------|
| True | True | True | True  | True     | **True**      | **True** |
| True | True | False| True  | True     | **True**      | **True** |
| True | False| True | True  | False    | False     | **True** |
| True | False| False| True  | True     | **True**      | **True** |
| False| True | True | True  | True     | **True**      | **True** |
| False| True | False| False | True     | False     | True |
| False| False| True | True  | False    | False     | False|
| False| False| False| False | True     | False     | False|

We have 3 symbols (A, B, C), so we have 2^3 = 8 possible interpretations. For all possible interpretations, **The sentence α evaluates to true whenever the knowledge base evaluates to true**. Therefore, we can conclude that the sentence α can be inferred from the knowledge base.

In `logic.py` module that we used earlier, this is what the function `model_check` does. It enumerates all possible interpretations and checks if the knowledge base entails a given sentence or not.

## Inferring with Model Checking
Watch the video (~20 minutes) below to see an example of the model checking algorithm.
<iframe width="100%" height="450" src="https://www.youtube.com/embed/HWQLez87vqM?si=Jy6ozpURoQ8dUfSN&amp;start=1308&end=2406" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The video shows how to use the model checking algorithm to determine if a given sentence can be inferred from the knowledge base.

The code used in the video is available [here](https://cdn.cs50.net/ai/2020/spring/lectures/1/src1/harry.py)

## Soundness and Completeness

### Soundness
A logical inference algorithm is said to be sound if it never derives a false conclusion from premises. In other words, it will not give wrong answers (false positives).

**The truth model checking approach is a sound algorithm. It does not give us wrong answers.**

### Completeness
An inference algorithm is complete if it is capable of deriving any valid conclusion that can be drawn from a given set of premises. In other words, it checks all possible interpretations and does not miss any valid inference.

**The model checking approach is a complete algorithm. It checks all possible interpretations and does not miss any valid inference.**


### Question:
What is the time complexity of the model checking / truth table algorithm?

Think about the number of rows in the truth table and the number of propositional symbols in the knowledge base. Think about it before you click to see the answer below.

<Details>
<Summary>Click to see the answer</Summary>
The truth table approach has an exponential time complexity. It requires 2<sup>n</sup> rows in the truth table, where n is the number of propositional symbols in the knowledge base. Therefore, the truth table approach is not practical for large knowledge bases.
</Details>

## Inference Rules
As we need only to check the KB for True values, we can improve the truth table algorithm by using the inference rules approach. We can use the inference rules to simplify the knowledge base and then check if a sentence `α` can be inferred from the simplified knowledge base. Inference rules can be used to generate new (sound) sentences from existing ones.

</br>

<iframe width="100%" height="450" src="https://www.youtube.com/embed/HWQLez87vqM?si=znQyxnVy2LIyD58F&amp;start=3871&end=5421" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Inference Rules
Inference rules are used to generate new sentences from existing ones. Some of the most common inference rules are:

- Modus Ponens: If we know that `A` implies `B` and we know that `A` is true, then we can infer that `B` is true.

- And Elimination: If we know that `A ∧ B` is true, then we can infer that `A` is true and we can infer that `B` is true.

- Double Negation: If we know that `A` is true, then we can infer that `¬¬A` is true.

- Implication  Elimination: If we know that `A` implies `B`, then we can infer that `¬A ∨ B` is true.

- Bidirectional Elimination: If we know that `A` is true if and only if `B` is true, then we can infer that `(A → B) ∧ (B → A)` is true.

- De Morgan's Law: If we know that `¬(A ∧ B)` is true, then we can infer that `¬A ∨ ¬B` is true.

- Distribution: If we know that `A ∨ (B ∧ C)` is true, then we can infer that `(A ∨ B) ∧ (A ∨ C)` is true.

- And many more...



## [Optional] Inference By Resolution
Inferring by resolution is based on the resolution rule, which is a sound and complete inference rule. The resolution rule is used to generate new clauses from existing ones.

Watch the video below to see how to use the resolution rule to perform inference.
<iframe width="100%" height="450" src="https://www.youtube.com/embed/HWQLez87vqM?si=znQyxnVy2LIyD58F&amp;start=5421&end=5858" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Summary
- Inference is the process of determining whether a given sentence can be derived from the knowledge base.
- The model checking approach uses truth tables for inference. It is a sound and complete algorithm, but it has an exponential time complexity.
- Inference rules can be used to simplify the knowledge base and then check if a sentence `α` can be inferred from the simplified knowledge base.
- The resolution rule is a sound and complete inference rule. It is used to generate new clauses from existing ones.



<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/_ttwRaZOERc?si=W3d_z2gCtvf5RISB&amp;start=38" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->