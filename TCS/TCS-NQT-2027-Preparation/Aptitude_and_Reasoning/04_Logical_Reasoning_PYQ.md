# Logical Reasoning - TCS NQT Last 5 Years PYQs

Logical reasoning requires careful reading. These are the most common patterns seen in TCS NQT.

---

## 1. Blood Relations (Coded)
**Question:** 
If A + B means A is the brother of B; 
A - B means A is the sister of B; 
A * B means A is the father of B. 
Which of the following means that C is the son of M?
Options:
a) M - N * C + F
b) F - C + N * M
c) N + M - F * C
d) M * N - C + F

**Solution Framework:**
Test option (d) using the family tree notation.
`M * N` -> M is father of N. `[M] | N`
`N - C` -> N is sister of C. `[M] | (N) — C`
`C + F` -> C is brother of F. `[M] | (N) — [C] — F`
Since M is the father of the siblings N, C, F, and C is a male (brother of F), C is the son of M.
**Answer: d**

## 2. Syllogism
**Question:**
Statements: 
1. Some Cats are Rats. 
2. All Bats are Rats.
Conclusions: 
I. Some Cats are Bats. 
II. No Cat is a Bat.

**Solution Framework:**
Draw the Venn diagram. 
Draw a circle for Cats intersecting a circle for Rats.
Draw the circle for Bats entirely inside the circle for Rats.
- Does the Cats circle HAVE to intersect the Bats circle? No, it could just intersect the non-Bat part of Rats. So Conclusion I is not definitely true.
- Does the Cats circle HAVE to be completely separated from the Bats circle? No, it *could* overlap. So Conclusion II is not definitely true.
However, notice the conclusions are a complementary pair ("Some A are B" and "No A is B"). If one is false, the other MUST be true.
**Answer: Either Conclusion I or Conclusion II follows.**

## 3. Seating Arrangement (Circular)
**Question:** Five friends P, Q, R, S, and T are sitting around a circular table facing the center. R sits second to the right of P. S sits exactly between R and P. T is not an immediate neighbor of P. Who sits to the immediate left of P?

**Solution Framework:**
1. Draw a circle with 5 spots.
2. "R sits second to the right of P." Place P anywhere. Move anti-clockwise 2 spots and place R.
3. "S sits exactly between R and P." Only one spot fits this (immediate right of P).
4. Now we have: P -> S -> R -> _ -> _ (Anti-clockwise).
5. "T is not an immediate neighbor of P." The spots left are immediate left of P, and next to R. So T must sit next to R.
6. The only person left is Q, who must sit in the remaining spot (immediate left of P).
**Answer: Q**

## 4. Coding and Decoding
**Question:** In a certain code language, "COMPUTER" is written as "RFUVQNPC". How will "MEDICINE" be written in that code language?

**Solution Framework:**
1. Write the word and code below it:
   C O M P U T E R
   R F U V Q N P C
2. Notice the first and last letters: C and R. They are swapped! First letter becomes last, last becomes first.
3. Let's look at the middle letters: O M P U T E
   Code: F U V Q N P
4. Reverse the middle letters: E T U P M O
5. Shift them by +1: F U V Q N P. It matches!
6. Rule: Swap first and last letters. Reverse the middle letters and add +1 to each.
7. Apply to MEDICINE: Swap M and E -> E _ _ _ _ _ _ M
8. Middle letters: E D I C I N. Reverse: N I C I D E. Shift +1: O J D J E F.
9. Final code: E O J D J E F M.
**Answer: EOJDDJEFM**

## 5. Direction Sense
**Question:** A man starts walking north and walks 10 km. He then turns right and walks 15 km. He then turns right again and walks 10 km. How far and in which direction is he from the starting point?

**Solution Framework:**
1. Start at point A.
2. North 10 km to point B.
3. Right turn (facing East) for 15 km to point C.
4. Right turn (facing South) for 10 km to point D.
5. Point D is exactly due East of point A because the north and south distances (10 km) cancel each other out. The distance is the east distance (15 km).
**Answer: 15 km East**

## 6. Statement and Assumptions
**Question:**
Statement: "Please do not use elevators during an earthquake." - A warning sign in a building.
Assumptions:
I. People might use elevators during an earthquake if the warning is not issued.
II. Elevators are generally safe during other times.

**Solution Framework:**
- Assumption I is implicit. Warnings are only issued because there is a possibility people might do the dangerous thing.
- Assumption II is implicit. Specifying "during an earthquake" implies that the prohibition doesn't apply at normal times.
**Answer: Both I and II are implicit.**
