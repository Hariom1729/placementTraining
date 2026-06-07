# Quantitative Aptitude - Extended TCS NQT Interview Questions (Part 2)

Further challenging Aptitude models that frequently appear in TCS exams.

---

## 9. Profit, Loss, and Discount (Successive Discounts)
**Question:** A shopkeeper offers two successive discounts of 15% and 20% on an article marked at Rs. 5000. What is the selling price of the article?
**Solution Framework:**
1. Method 1 (Successive Formula): Net Discount = $x + y - (xy/100) = 15 + 20 - (15 \times 20)/100 = 35 - 3 = 32\%$.
2. Selling Price = $(100\% - 32\%) \text{ of } 5000 = 68\% \text{ of } 5000$.
3. $SP = 0.68 \times 5000 = 3400$.
**Alternative Method (Multiplier):**
$SP = 5000 \times (1 - 0.15) \times (1 - 0.20) = 5000 \times 0.85 \times 0.80 = 5000 \times 0.68 = 3400$.
**Answer: Rs. 3400**

## 10. Time, Speed, and Distance (Boats and Streams)
**Question:** A boat can travel with a speed of 13 km/hr in still water. If the speed of the stream is 4 km/hr, find the time taken by the boat to go 68 km downstream.
**Solution Framework:**
1. Downstream Speed (Speed of boat + Speed of stream) = $13 + 4 = 17 \text{ km/hr}$.
2. Upstream Speed (Speed of boat - Speed of stream) = $13 - 4 = 9 \text{ km/hr}$.
3. We need time for downstream travel.
4. Time = Distance / Speed = $68 / 17 = 4$ hours.
**Answer: 4 hours**

## 11. Mixtures and Alligations (Replacement)
**Question:** A container contains 40 liters of milk. From this container, 4 liters of milk was taken out and replaced by water. This process was repeated further two times. How much milk is now contained by the container?
**Solution Framework:**
Use the formula: Final Quantity = Initial Quantity $\times (1 - \text{Replacement Volume} / \text{Total Volume})^N$
1. Initial = 40. Replacement = 4. Total = 40. $N = 3$ (Done once, then repeated two *more* times).
2. Final Milk = $40 \times (1 - 4/40)^3$
3. Final Milk = $40 \times (1 - 1/10)^3 = 40 \times (9/10)^3$
4. Final Milk = $40 \times (729 / 1000) = 4 \times 7.29 = 29.16$ liters.
**Answer: 29.16 liters**

## 12. Percentages (Elections)
**Question:** In an election between two candidates, one got 55% of the total valid votes, 20% of the votes were invalid. If the total number of votes was 7500, the number of valid votes that the other candidate got, was:
**Solution Framework:**
1. Total votes = 7500.
2. Invalid votes = 20%. Therefore, valid votes = 80%.
3. Number of valid votes = $80\% \text{ of } 7500 = 0.8 \times 7500 = 6000$.
4. Winning candidate got 55% of valid votes.
5. Losing candidate got $(100\% - 55\%) = 45\%$ of valid votes.
6. Votes for losing candidate = $45\% \text{ of } 6000 = 0.45 \times 6000 = 2700$.
**Answer: 2700**

## 13. Ages
**Question:** The present age of a father is 3 years more than three times the age of his son. Three years hence, father's age will be 10 years more than twice the age of the son. Find the present age of the father.
**Solution Framework:**
1. Let son's present age = $x$.
2. Father's present age = $3x + 3$.
3. 3 years hence: Son = $x + 3$. Father = $3x + 3 + 3 = 3x + 6$.
4. Condition given: Father's age = $2 \times (\text{Son's age}) + 10$.
5. $3x + 6 = 2(x + 3) + 10$
6. $3x + 6 = 2x + 6 + 10$
7. $x = 10$.
8. Father's present age = $3(10) + 3 = 33$.
**Answer: 33 years**

## 14. Number System (HCF and LCM)
**Question:** The H.C.F. of two numbers is 11 and their L.C.M. is 7700. If one of the numbers is 275, then the other is:
**Solution Framework:**
Use the fundamental property: Product of two numbers = Product of their HCF and LCM.
1. Let numbers be $A$ and $B$. $A \times B = \text{HCF} \times \text{LCM}$.
2. $275 \times B = 11 \times 7700$.
3. $B = (11 \times 7700) / 275$.
4. $275 / 11 = 25$. So, $B = 7700 / 25$.
5. $B = 308$.
**Answer: 308**

## 15. Averages
**Question:** The average weight of 8 persons increases by 2.5 kg when a new person comes in place of one of them weighing 65 kg. What might be the weight of the new person?
**Solution Framework:**
1. Total increase in weight = $8 \text{ persons} \times 2.5 \text{ kg} = 20 \text{ kg}$.
2. This increase is solely caused by the new person replacing the old one.
3. Therefore, the new person must be 20 kg heavier than the person they replaced.
4. Weight of new person = Weight of old person + Total Increase = $65 + 20 = 85 \text{ kg}$.
**Answer: 85 kg**
