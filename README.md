
# Prime Number Checker

This Python program implements a class-based approach to checking prime numbers. It includes both individual prime checking and batch checking within a range. The algorithm dynamically builds a list of known prime numbers to efficiently check divisibility, improving performance for large numbers.

## Features

- **Check if a number is prime**
- **Generate a list of primes up to a given number**
- **Detailed debug output (number of steps, divisibility by 5, etc.)**

## How it Works

The core of the program is the `Prime` class which maintains:
- A list of discovered primes (`prime_list`)
- A method to check if a number is prime (`isPrime`)
- A method to generate all primes in a range (`checkInRange`)

### Prime Number Checking Algorithm

1. For a given number `n`, the program first eliminates obvious non-primes like those ending in 0 or 5.
2. It uses the known list of primes to test divisibility.
3. If all known primes are less than `√n` and none divide `n`, the number is considered prime.
4. If needed, new primes are discovered recursively and added to the list.

This avoids checking unnecessary numbers and speeds up the process significantly.

### Time Complexity (Big-O)

- **Single prime check (`isPrime(n)`)**:  
  - Worst case: **O(√n)** — since it checks divisibility using primes up to `√n`.
  - Recursive prime discovery may increase overhead slightly but remains within the same asymptotic bound.
  - The number 2131131137 is a proof of the effieciency of this algorithm (speedwise)
  - The ourput when running this number was:
```bash
Please insert number: 2131131137
(True, 2131131137)
this took 46163 steps
```
  - - **√2131131137 = 46164** This is almost equal to **46163**
  - I came up with this number by testing
  
- **Range prime check (`checkInRange()`)**:  
  - Worst case: **O(n√n)** — for checking each number up to `n`, each requiring up to `√n` checks.

This makes the algorithm suitable for small to medium-sized inputs, but not for cryptographic-scale numbers.

## Usage

Run the script in a Python environment. You will be prompted to enter a number.

```bash
$ python prime_checker.py
Please insert number: 29
(True, 29)
this took 1 steps
```

To check all numbers up to `n`, uncomment the following line in the script:

```python
#print(prime.checkInRange())
```

## Example

For input `29`, the output might look like:

```
(True, 29)
this took 1 steps
```

## Notes

- This is a demonstration of recursive prime checking and is not optimized for very large numbers.
- It uses a list of previously found primes to reduce redundant work.

## License

This project is released under the MIT License.
