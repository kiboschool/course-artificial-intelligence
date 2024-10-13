# Logic and Knowledge Representation
<p align="center">
  <img src="../../images/facts_rules.png" alt="AI Logic"  />
</p>

## What is logic? 
In the context of AI, logic refers to a formal system used to represent and reason about knowledge and information. It is the same logic that we use in mathematics and philosophy, but applied to the domain of AI. Logic is used to represent facts and rules, and to draw conclusions from them. For example, we can use logic to represent the fact that "it's raining outside", and the rule that "if it's raining outside, then I should take an umbrella", and then use it to draw the conclusion that "I should take an umbrella".

## What is Knowledge?
Knowledge refers to the information, understanding, and awareness that an individual or a system possesses about the world. It encompasses facts, concepts, beliefs, insights, experiences, and skills acquired through learning, observation, reasoning, and experimentation.

Knowledge of facts, also called **propositional knowledge**, is often characterized as true belief that is distinct from opinion or guesswork by virtue of justification. - Wikipedia

Since our study is about intelligent systems and decision making, we are interested in the propositional knowledge. This is the type of knowledge that can be represented as a set of propositions, or statements that can be either true or false.

## Knowledge Representation (KB)
Knowledge representation is a field of artificial intelligence that focuses on how to formally represent knowledge in a way that can be used to solve problems.

Based on the goals and the type of questions you will ask or use the KB for, you would select the appropriate knowledge representation model. For example, if you are interested in representing the knowledge in a way that allows you to query facts, you would use a different model than if you are interested in representing the knowledge in a way that allows you to generate new content.

### Knowledge Representation Models
Semantic Networks, Frames, Conceptual Graphs, Neural Networks and Logic are all examples of knowledge representation models. Each model is suitable for different types of problems. 

Semantic networks, for example, are suitable for representing knowledge about the relationships between objects, which is useful in building cognitive systems like chatbots. On the other hand, logic-based knowledge representation is suitable for representing facts and rules, which is useful in building expert systems.

In this lesson, we focus on the logic-based knowledge representation model. This model allows us to represent facts and rules, and to draw conclusions from them. 

An example of what we can do with logic-based knowledge representation is a medical diagnosis assistant.
- If a person exhibits sneezing and a runny nose but no fever, it is certain that they have allergies.

- If a person exhibits fever, cough, and body aches, it is certain that they have flu.

- If a person exhibits cough and runny nose, but no fever, it is certain that they have a common cold.


We can represent these facts and rules in a knowledge base, using propositional logic or first-order logic, and then use it to diagnose a patient based on their symptoms. 


## Different Types of Logic
There are different types of logic, each suitable for different types of problems. The two main types of logic that we will focus on in this class are:
- Propositional Logic
- First-Order Logic

Other types of logic include:
- Temporal Logic
- Fuzzy Logic
- Probabilistic Logic
- and more.

