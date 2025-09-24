# CSS Selectors vs XPath: A Complete Guide with Examples

When scraping websites, the two most common ways to locate elements are **CSS selectors** and **XPath** . CSS is shorter and familiar to front-end developers, while XPath is more powerful and flexible.

In this article, we’ll start with a single HTML snippet and explore how to select elements using **both CSS and XPath** . Along the way, we’ll cover attributes, children, siblings, positions, negations, and even advanced text handling using `normalize-space()`.

---

## Example HTML

We’ll use this throughout the article:

```html
<div id="container">
  <div class="card featured" data-id="101">
    <h2>First Card</h2>
    <p>Description one</p>
  </div>

  <div class="card" data-id="102">
    <h2>Second Card</h2>
    <p>Description two</p>
  </div>

  <div class="card" data-id="103">
    <h2>Third Card</h2>
    <p>Description three</p>
  </div>
</div>
```

---

## 1. Select by Tag

- **CSS:**
  ```css
  div
  ```
- **XPath:**
  ```xpath
  //div
  ```

Both select every `<div>` element.

---

## 2. Select by Class

- **CSS:**
  ```css
  .card
  ```
- **XPath:**
  ```xpath
  //*[contains(concat(' ', normalize-space(@class), ' '), ' card ')]
  ```

👉 `normalize-space(@class)` removes extra spaces around the `class` attribute, making it safer for matching.

👉 **Why so long?** Because in XPath, `class` can hold multiple space-separated values. This ensures we match `"card"` exactly, not just part of another class name like `"cardio"`.

---

## 3. Select by ID

- **CSS:**
  ```css
  #container
  ```
- **XPath:**
  ```xpath
  //*[@id="container"]
  ```

---

## 4. Tag + Class

- **CSS:**
  ```css
  div.card
  ```
- **XPath:**
  ```xpath
  //div[contains(concat(' ', normalize-space(@class), ' '), ' card ')]
  ```

---

## 5. Tag + ID

- **CSS:**
  ```css
  div#container
  ```
- **XPath:**
  ```xpath
  //div[@id="container"]
  ```

---

## 6. Has Attribute

- **CSS:**
  ```css
  div[data-id]
  ```
- **XPath:**
  ```xpath
  //div[@data-id]
  ```

---

## 7. Attribute Equals

- **CSS:**
  ```css
  div[data-id="102"]
  ```
- **XPath:**
  ```xpath
  //div[@data-id="102"]
  ```

---

## 8. Attribute Starts With

- **CSS:**
  ```css
  div[data-id^="10"]
  ```
- **XPath:**
  ```xpath
  //div[starts-with(@data-id, "10")]
  ```

---

## 9. Attribute Ends With

- **CSS:**
  ```css
  div[data-id$="3"]
  ```
- **XPath:**
  ```xpath
  //div[substring(@data-id, string-length(@data-id) - string-length("3") + 1) = "3"]
  ```

---

## 10. Attribute Contains

- **CSS:**
  ```css
  div[data-id*="2"]
  ```
- **XPath:**
  ```xpath
  //div[contains(@data-id, "2")]
  ```

---

## 11. Direct Child vs Descendant

- **CSS (direct child):**
  ```css
  div > h2
  ```
- **XPath:**
  ```xpath
  //div/h2
  ```
- **CSS (any descendant):**
  ```css
  div h2
  ```
- **XPath:**
  ```xpath
  //div//h2
  ```

---

## 12. Adjacent Sibling

- **CSS:**
  ```css
  h2 + p
  ```
- **XPath:**
  ```xpath
  //h2/following-sibling::*[1][self::p]
  ```

---

## 13. General Sibling

- **CSS:**
  ```css
  h2 ~ p
  ```
- **XPath:**
  ```xpath
  //h2/following-sibling::p
  ```

---

## 14. First Child

- **CSS:**
  ```css
  div: first-child;
  ```
- **XPath:**
  ```xpath
  //div/*[1]
  ```

---

## 15. Last Child

- **CSS:**
  ```css
  div: last-child;
  ```
- **XPath:**
  ```xpath
  //div/*[last()]
  ```

---

## 16. Nth Child

- **CSS:**
  ```css
  div: nth-child(2);
  ```
- **XPath:**
  ```xpath
  //div/*[2]
  ```

---

## 17. Nth Last Child

- **CSS:**
  ```css
  div: nth-last-child(2);
  ```
- **XPath:**
  ```xpath
  //div/*[last() - 2 + 1]
  ```

---

## 18. Nth of Type

- **CSS:**
  ```css
  h2: nth-of-type(2);
  ```
- **XPath:**
  ```xpath
  //h2[2]
  ```

---

## 19. First of Type

- **CSS:**
  ```css
  h2: first-of-type;
  ```
- **XPath:**
  ```xpath
  //h2[1]
  ```

---

## 20. Last of Type

- **CSS:**
  ```css
  h2: last-of-type;
  ```
- **XPath:**
  ```xpath
  //h2[last()]
  ```

---

## 21. Empty Elements

- **CSS:**
  ```css
  div: empty;
  ```
- **XPath:**
  ```xpath
  //div[not(node())]
  ```

---

## 22. Only Child

- **CSS:**
  ```css
  div: only-child;
  ```
- **XPath:**
  ```xpath
  //div[count(preceding-sibling::*) = 0 and count(following-sibling::*) = 0]
  ```

---

## 23. Odd and Even Children

- **CSS:**
  ```css
  div:nth-child(odd)
  div:nth-child(even)
  ```
- **XPath:**
  ```xpath
  //div/*[position() mod 2 = 1]   (odd)
  //div/*[position() mod 2 = 0]   (even)
  ```

---

## 24. Negation

- **CSS:**
  ```css
  div: not(.featured);
  ```
- **XPath:**
  ```xpath
  //div[not(contains(concat(' ', normalize-space(@class), ' '), ' featured '))]
  ```

---

## 25. Text Content with normalize-space

Sometimes you want elements by their **visible text** , ignoring whitespace.

Example: Select the `<h2>` with text `"Second Card"` (note the messy spaces in HTML).

- **CSS:** ❌ Not possible (CSS can’t match text directly).
- **XPath:**
  ```xpath
  //h2[normalize-space(text()) = "Second Card"]
  ```

---

## Key Insights

- **CSS selectors** are simpler and shorter → great for quick scraping.
- **XPath selectors** are more powerful → text matching, parent traversal, advanced filtering.
- Always use `normalize-space()` in XPath when dealing with text content or class attributes to avoid whitespace issues.

---

👉 Next step: I can also create a **Python example (using lxml or Selenium)** that applies all these selectors on the same HTML so you can see them in action.

Would you like me to write that code?
