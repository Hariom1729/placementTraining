# Quantitative Aptitude: Tricks and Frameworks

Quantitative Aptitude is the first and often the most aggressive elimination round in the TCS NQT. Speed and accuracy are paramount.

---

## 1. Number System Fundamentals

### Divisibility Rules
- **By 3:** Sum of digits is divisible by 3.
- **By 4:** Last two digits form a number divisible by 4.
- **By 8:** Last three digits form a number divisible by 8.
- **By 9:** Sum of digits is divisible by 9.
- **By 11:** Difference between the sum of digits at odd places and even places is 0 or a multiple of 11.

### Unit Digit Concept
To find the unit digit of an expression like $X^Y$:
1. Divide the power $Y$ by 4 and find the remainder $R$.
2. If $R = 0$, treat the power as 4.
3. The unit digit of $X^Y$ is the unit digit of $(\text{Unit digit of } X)^R$.
*Example: Find unit digit of $2^{43}$. 43 / 4 leaves remainder 3. $2^3 = 8$. Unit digit is 8.*

---

## 2. Percentages, Profit, and Loss

### Fractional Equivalents (Memorize These)
Knowing these conversions saves massive calculation time:
- $1/2 = 50\%$
- $1/3 = 33.33\%$
- $1/4 = 25\%$
- $1/5 = 20\%$
- $1/6 = 16.66\%$
- $1/7 = 14.28\%$
- $1/8 = 12.5\%$
- $1/9 = 11.11\%$
- $1/11 = 9.09\%$

### Successive Percentage Change
If a value is changed successively by $x\%$ and $y\%$, the net percentage change is given by the formula:
**Net Change = $x + y + (x \cdot y) / 100$**
*(Use negative signs for decreases/losses).*

---

## 3. Speed, Time, and Distance

- **Basic Formula:** Distance = Speed $\times$ Time
- **Conversion:** 
  - km/hr to m/s: Multiply by $5 / 18$
  - m/s to km/hr: Multiply by $18 / 5$

### Average Speed
If a person covers a certain distance at speed $A$ and the **same** distance at speed $B$, the average speed for the whole journey is:
**Average Speed = $(2 \cdot A \cdot B) / (A + B)$**
*(Do not just average A and B!)*

### Relative Speed
- Bodies moving in the **same** direction: Relative Speed = $S1 - S2$
- Bodies moving in **opposite** directions: Relative Speed = $S1 + S2$

---

## 4. Time and Work

**Efficiency Concept (The LCM Method):**
Instead of using fractions ($1/A + 1/B$), use the LCM method.
1. If A can do a job in 10 days and B in 15 days.
2. Let Total Work = LCM of (10, 15) = 30 units.
3. Efficiency of A = $30 / 10 = 3$ units/day.
4. Efficiency of B = $30 / 15 = 2$ units/day.
5. Together they do $3 + 2 = 5$ units/day.
6. Time taken together = $Total Work / Combined Efficiency = 30 / 5 = 6$ days.

---

## 5. Permutations and Combinations

- **Permutation (Arrangement):** Order matters. Formula: $^n P_r = n! / (n - r)!$
  - *Example:* Arranging people in a line, forming words from letters.
- **Combination (Selection):** Order does not matter. Formula: $^n C_r = n! / (r! \cdot (n - r)!)$
  - *Example:* Selecting a team from a group, drawing cards.

**Handshake Formula:**
Number of handshakes when $n$ people shake hands with everyone else: $(n \cdot (n - 1)) / 2$.
