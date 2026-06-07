# Logical Reasoning - Extended TCS NQT Interview Questions (Part 2)

Further challenging Logical Reasoning models.

---

## 7. Data Sufficiency
**Question:** What is the two-digit number?
Statement I: The difference between the two digits is 3.
Statement II: The sum of the two digits is 7.
Options:
A. Statement I alone is sufficient.
B. Statement II alone is sufficient.
C. Both statements together are sufficient.
D. Both statements together are not sufficient.

**Solution Framework:**
1. Analyze Statement I: Diff is 3. Possible pairs: (0,3), (1,4), (2,5), (3,6), (4,7), (5,8), (6,9). Many possible numbers (e.g., 41, 14, 52, 25). Not sufficient alone.
2. Analyze Statement II: Sum is 7. Possible pairs: (0,7), (1,6), (2,5), (3,4). Possible numbers: 70, 16, 61, 25, 52, 34, 43. Not sufficient alone.
3. Combine I and II: We need a pair whose sum is 7 and diff is 3.
   $x + y = 7$
   $x - y = 3$
   Adding: $2x = 10 \implies x = 5$. Then $y = 2$.
   The digits are 5 and 2.
4. What is the number? It could be 52 or 25. Even with both statements, we cannot definitively find *the* single two-digit number.
**Answer: D. Both statements together are not sufficient.**

## 8. Inequalities
**Question:**
Statements: $P < Q \le R = S$; $R > T$
Conclusions:
I. $P < S$
II. $Q > T$

**Solution Framework:**
1. Combine statements if necessary, or trace paths.
2. For Conclusion I: Check path from P to S. $P < Q \le R = S$. The relation flows from P to S with the strongest operator being `<`. Therefore, $P < S$ is definitely true.
3. For Conclusion II: Check path from Q to T. $Q \le R > T$. Notice the operators flip directions ($\le$ and $>$). When operators point in opposite directions between two elements, no definitive relationship can be established between them. Therefore, Conclusion II is false.
**Answer: Only Conclusion I follows.**

## 9. Blood Relations (Puzzle Form)
**Question:** A family consists of six members P, Q, R, X, Y, and Z. Q is the son of R but R is not the mother of Q. P and R are a married couple. Y is the brother of R. X is the daughter of P. Z is the brother of P. How many female members are there in the family?

**Solution Framework:**
Draw the family tree:
1. Q is the son of R. R is not the mother. Therefore, R must be the father (Male). `[R] | [Q]`
2. P and R are married. Since R is male, P is female. `(P) === [R] | [Q]`
3. Y is the brother of R. `[Y] — [R] === (P)`
4. X is the daughter of P. Since P and R are married, X is sibling to Q. `[Y] — [R] === (P) | [Q] — (X)`
5. Z is the brother of P. `[Y] — [R] === (P) — [Z]`
Count the females (circles): P and X.
**Answer: 2**

## 10. Number Series
**Question:** Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?
**Solution Framework:**
Find the pattern between consecutive terms.
- 2 to 1: Divide by 2 (or multiply by 1/2)
- 1 to 1/2: Divide by 2
- 1/2 to 1/4: Divide by 2
The pattern is multiplying the previous term by 1/2.
Next term = $(1/4) \times (1/2) = 1/8$.
**Answer: 1/8**

## 11. Clocks and Calendars
**Question:** What was the day of the week on 15th August 1947?
**Solution Framework:**
Use the odd days concept.
1. 1946 years = $1600 + 300 + 46$.
2. 1600 years = 0 odd days. 300 years = 1 odd day.
3. 46 years = 11 leap years + 35 ordinary years = $(11 \times 2) + (35 \times 1) = 22 + 35 = 57$ odd days.
4. $57 / 7 = 8$ weeks + 1 odd day.
5. Total odd days for 1946 years = $1 + 1 = 2$.
6. For 1947 (up to Aug 15): Jan (3) + Feb (0, not a leap year) + Mar (3) + Apr (2) + May (3) + Jun (2) + Jul (3) + Aug (15) = 31 days.
7. $31 / 7 = 4$ weeks + 3 odd days.
8. Total odd days = $2 \text{ (from years)} + 3 \text{ (from months)} = 5$ odd days.
9. 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat.
**Answer: Friday**

## 12. Order and Ranking
**Question:** In a row of boys, If A who is 10th from the left and B who is 9th from the right interchange their positions, A becomes 15th from the left. How many boys are there in the row?
**Solution Framework:**
1. A's new position is the exact same physical spot as B's old position.
2. We know B's old position was 9th from the right.
3. We are given A's new position is 15th from the left.
4. Therefore, this specific chair is 15th from the left AND 9th from the right.
5. Total = (Left Position + Right Position) - 1
6. Total = $(15 + 9) - 1 = 24 - 1 = 23$.
**Answer: 23 boys**
