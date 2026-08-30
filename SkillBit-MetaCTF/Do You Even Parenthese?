# Do You Even Parenthese?
 
**Platform:** Skill Bit (previously MetaCTF)
 
**Description:** This is called a LISP expression. What does it evaluate to?
 
```
(MULT (ADD 6 (EXP 2 2)) (DIV 72 (MULT (SUB 21 17) 3)))
```
 
## Approach
 
This challenge just asks us to evaluate the number the expression comes out to. The math itself is simple, so the real work is knowing what each operator means and how to break a big nested expression down.
 
LISP uses prefix notation, which means the operator comes first and the values come after it:
 
```
(OPERATOR value1 value2)
```
 
The important part is that value1 and value2 don't have to be plain numbers. Either one can be another expression in parentheses, which is why this one looks so messy. Every set of parentheses is its own little problem, so you start with the innermost ones and work your way out.
 
## Operators used in this challenge
 
| Operator | Meaning | Example |
|---|---|---|
| `ADD` | add the two numbers | `ADD 6 4` = 6 + 4 |
| `SUB` | subtract the second number from the first | `SUB 21 17` = 21 - 17 |
| `MULT` | multiply the two numbers | `MULT 4 3` = 4 * 3 |
| `DIV` | divide the first number by the second | `DIV 72 12` = 72 / 12 |
| `EXP` | raise the first number to the power of the second | `EXP 2 2` = 2 ^ 2 |
 
## Breaking it down
 
Start with the innermost parentheses and work outward.
 
```
(MULT (ADD 6 (EXP 2 2)) (DIV 72 (MULT (SUB 21 17) 3)))
```
 
1. `EXP 2 2` = 4 and `SUB 21 17` = 4
   `(MULT (ADD 6 4) (DIV 72 (MULT 4 3)))`
2. `MULT 4 3` = 12
   `(MULT (ADD 6 4) (DIV 72 12))`
3. `ADD 6 4` = 10 and `DIV 72 12` = 6
   `(MULT 10 6)`
4. `MULT 10 6` = 60
## Answer
 
```
60
```
 
## Takeaway
 
Nothing here is hard math. The whole challenge is reading prefix notation and being disciplined about resolving the innermost parentheses first instead of trying to read the expression left to right like normal math.
