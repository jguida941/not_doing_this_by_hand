# not_doing_this_by_hand

A collection of tools to automate tedious discrete math busywork so I don't have to waste time with it.

## Why This Exists

Because memorizing calculation procedures is pointless when Python can do it in one line.

```python
# GCD? One line.
import math
math.gcd(315, 550)  # 5

# LCM? One line.
(315 * 550) // math.gcd(315, 550)  # 34650

# Why are we still doing this manually in 2025?
```

## What's Included

### GCD/LCM Calculator
- Calculates GCD and LCM instantly
- Shows the stupid prime factorization format the homework wants
- Dark mode UI because I'm not a monster
- Handles the work format for you

### Coming Soon (as assignments force me to make them)
- Prime factorization tool
- Set operation calculator
- Truth table generator
- Whatever other tedious math I have to automate

## Installation

1. Clone this repo
2. Run `pip install -r requirements.txt` (if there are any)
3. Run the tool you need:
   ```
   python gcd_lcm_calculator.py
   ```

## Use Cases

- Doing discrete math homework without wasting time
- Checking your manual work
- Learning practical programming instead of abstract math
- Getting through required math courses while focusing on useful skills

## Requirements

- Python 3.6+
- A burning hatred for tedious mathematical busywork
- An appreciation for automation over memorization

## License

Do whatever you want with this. Copy it, modify it, sell it, I don't care.
If it helps you get through tedious math assignments faster, that's all that matters.

## Acknowledgements

- Thanks to the math professors who refuse to update their curriculum for the computer age, forcing students to waste time on calculations that should be automated
- Thanks to Python for having a math library so I don't have to implement this myself
- Thanks to AI for helping generate some of this code so I can focus on useful skills

## Disclaimer

Use at your own risk. If your professor finds out you're using this to generate homework answers, that's between you and them. This tool exists because time is valuable and should be spent learning useful skills, not doing repetitive calculations.
