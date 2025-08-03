# String Calculator Explanation

The `add()` function is designed to compute the sum of positive integers from an input string, where the numbers are separated by default or custom delimiters. It also validates the numbers, ensuring that negative numbers and numbers greater than 1000 are not included in the sum.

---

## Code Breakdown

### Regular Expressions (Regex)

- **`MUL_DELIM_REGEX = r"(\[.*?\])"`**  
  This regex matches custom delimiters that are surrounded by square brackets (`[]`). Example: `"[***]"` or `"[abc]"`.

- **`DELIM_REGEX = r"(\/\/(.*?)\n)?(.*)"`**  
  This regex is used to match the custom delimiter declaration at the start of the string, i.e., `//[***][abc]\n`. It captures:
  - The optional delimiter declaration (after `//`).
  - The rest of the input string containing the numbers.

---

### Function Behavior

1. **Delimiter Initialization:**
   - The function starts by setting the default delimiter to `","` (comma).

2. **Custom Delimiter Handling:**
   - If the input string starts with `//` (indicating custom delimiters), it:
     - Uses `re.match()` to capture the delimiter declaration.
     - Removes the delimiter declaration part (e.g., `//[***][abc]`).
     - Extracts any custom delimiters from the declaration, e.g., `[***]` and `[abc]`.
     - If no custom delimiters are found, the list `delims` is reset to `,`.

3. **Delimiter Addition:**
   - The newline character (`\n`) is appended to the `delims` list to handle multi-line inputs.

4. **Splitting the Input:**
   - The input string is split into separate numbers using the delimiters specified in `delims`. It escapes each delimiter using `re.escape()` to ensure proper regex handling.

5. **Processing the Numbers:**
   - For each number:
     - Whitespace is stripped, and the number is converted to an integer.
     - The number is checked to ensure it's between 0 and 1000 (inclusive).
     - Negative numbers are added to the `invalid_nums` list.

6. **Error Handling:**
   - If negative numbers are found, a `ValueError` is raised, indicating which negative numbers were present.

7. **Return Value:**
   - If no valid numbers are found, the function returns `0`.
   - If valid numbers are found, the function returns the sum of the valid numbers.

---

## Usage

Call the `add()` function with a string input containing numbers. The string may include:
- Numbers separated by custom delimiters (if specified).
- An optional custom delimiter declaration at the beginning of the input.

### Example:

```python
add("//[***][abc]xyz\n2***3***6\n1abc1000")
