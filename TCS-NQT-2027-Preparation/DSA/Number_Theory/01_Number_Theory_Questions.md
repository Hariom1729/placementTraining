# Number Theory & Mathematics - TCS NQT Preparation

TCS NQT extensively tests mathematical logic and number theory in their coding rounds. The questions generally require an understanding of prime numbers, GCD/LCM, modulo arithmetic, digit extraction, and basic combinatorics.

Here are 25 high-frequency Number Theory questions asked in TCS NQT:

---

## 1. Prime Numbers & Factors

**1. Check if a number is Prime.**
*Approach:* Loop from 2 to `sqrt(N)`. If `N % i == 0`, it's not prime. Time complexity: $O(\sqrt{N})$.

**2. Print all Prime Numbers in a given range (L to R).**
*Approach:* Use the Sieve of Eratosthenes if the range is up to $10^6$, else use the basic $\sqrt{N}$ check for each number.

**3. Sieve of Eratosthenes.**
*Approach:* Create a boolean array `prime[n+1]` initialized to true. For $p=2$ to $\sqrt{N}$, if `prime[p]` is true, mark all multiples of $p$ as false.
```cpp
void sieve(int n) {
    vector<bool> prime(n + 1, true);
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) prime[i] = false;
        }
    }
}
```

**4. Find all factors of a number.**
*Approach:* Iterate from 1 to `sqrt(N)`. If `N % i == 0`, print `i`. If `N/i != i`, also print `N/i`.

**5. Prime Factorization of a Number.**
*Approach:* Divide the number by 2 until it's odd. Then iterate from 3 to `sqrt(N)` with step 2, dividing out prime factors. Finally, if $N > 2$, $N$ is a prime factor itself.

**6. Count total divisors of a number.**
*Approach:* Find prime factorization $p_1^{a_1} \times p_2^{a_2} \dots$. The total divisors = $(a_1 + 1) \times (a_2 + 1) \dots$

## 2. GCD & LCM

**7. Find the GCD (Greatest Common Divisor) of two numbers.**
*Approach:* Euclidean Algorithm.
```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

**8. Find the LCM (Least Common Multiple) of two numbers.**
*Approach:* $\text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}$.

**9. Find the GCD of an array of numbers.**
*Approach:* Take the GCD of the first two numbers, then the GCD of the result with the third number, and so on.

**10. Find the LCM of an array of numbers.**
*Approach:* Similar to GCD of an array. Keep updating `ans = (ans * arr[i]) / gcd(ans, arr[i])`.

## 3. Digit Manipulation

**11. Reverse a number.**
*Approach:* `while(N > 0) { rem = N % 10; rev = rev * 10 + rem; N /= 10; }`

**12. Check if a number is a Palindrome.**
*Approach:* Reverse the number and check if it equals the original number.

**13. Check if a number is an Armstrong Number.**
*Approach:* Count digits ($K$). Sum the $K$-th power of each digit. If sum == original number, it's an Armstrong number (e.g., $153 = 1^3 + 5^3 + 3^3$).

**14. Find the sum of digits of a number until it becomes a single digit.**
*Approach:* The result is simply `(N % 9 == 0) ? 9 : (N % 9)`. (If $N=0$, answer is 0).

**15. Check if a number is a Strong Number.**
*Approach:* A strong number is one where the sum of the factorials of its digits equals the number (e.g., $145 = 1! + 4! + 5!$).

## 4. Modulo Arithmetic

**16. Compute $(A^B) \pmod M$ efficiently (Modular Exponentiation).**
*Approach:* Exponentiation by squaring.
```cpp
long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        exp = exp >> 1;
        base = (base * base) % mod;
    }
    return res;
}
```

**17. Find the trailing zeroes in $N!$ (Factorial).**
*Approach:* Count the number of 5s in the prime factors of $N!$. The formula is $\lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \lfloor N/125 \rfloor \dots$

**18. Find the last digit of $A^B$.**
*Approach:* Last digits repeat in cycles of 4 (e.g., 2's powers end in 2, 4, 8, 6). Find `A % 10` and `B % 4` (if `B%4 == 0`, treat it as 4) and compute.

## 5. Sequences & Series

**19. N-th Fibonacci Number.**
*Approach:* Uses loop (iterative) or Binet's Formula or Matrix Exponentiation for large N. Time complexity $O(N)$ for loop.

**20. Check if a number is a Perfect Square.**
*Approach:* Binary search from 1 to $N$, or check if $\lfloor\sqrt{N}\rfloor \times \lfloor\sqrt{N}\rfloor == N$.

**21. Find the N-th term of a given series (TCS Specific).**
*Problem:* E.g., $1, 2, 1, 3, 2, 5, 3, 7 \dots$ (Mix of two series: Fibonacci at odd indices, Primes at even indices).
*Approach:* Separate the series based on odd and even indices and compute independently.

**22. Calculate ${}^nC_r$ (Combinations).**
*Approach:* Compute using a loop to avoid overflow:
```cpp
long long nCr(int n, int r) {
    long long res = 1;
    if (r > n - r) r = n - r;
    for (int i = 0; i < r; ++i) {
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}
```

## 6. Miscellaneous Math

**23. Find if two numbers are Coprime.**
*Approach:* Two numbers are coprime if their GCD is 1.

**24. Find the leap year.**
*Approach:* A year is a leap year if `(year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)`.

**25. Check if a number is a Perfect Number.**
*Approach:* A perfect number is a positive integer that is equal to the sum of its proper divisors (e.g., $6 = 1 + 2 + 3$). Find all factors (excluding $N$) and sum them.
