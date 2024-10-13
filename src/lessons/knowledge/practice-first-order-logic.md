# Practice: First Order Logic

Q1. Translate the statement "David is a professor." into First-Order Logic.

<Details>
<Summary>Answer</Summary>
Professor(David)
</Details>

Q2. Translate the statement "Mohammed Teaches AI." into First-Order Logic.
<Details>
<Summary>Answer</Summary>
Teaches(Mohammed, AI)
</Details>

Q3. Translate the statement "Deans are professors." into First-Order Logic.

<Details>
<Summary>Answer</Summary>
∀x (Dean(x) → Professor(x))
</Details>

Convert the sentence "There exists a product with a price higher than $100" into First-Order Logic.

<Details>
<Summary>Answer</Summary>
∃x (Product(x) ∧ Price(x) > 100)
</Details>


Translate the statement "For every product that has been ordered, there exists a customer who placed the order" into First-Order Logic.
<Details>
<Summary>Answer</Summary>
∀x (Product(x) ∧ Ordered(x) → ∃y (Customer(y) ∧ PlacedOrder(y, x)))
</Details>



Represent the statement "All employees who work on a project are assigned specific tasks" in First-Order Logic.
<Details>
<Summary>Answer</Summary>
∀x (Employee(x) ∧ WorksOnProject(x) → ∃y (Task(y) ∧ AssignedToTask(x, y)))
</Details>

