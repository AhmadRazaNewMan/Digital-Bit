# Form Accessibility: Labels, Errors, Focus Management
## What
Form accessibility is crucial for ensuring that all users can interact with web applications. It involves providing proper labels, handling errors, and managing focus to facilitate navigation. Key elements include:
* Associating form fields with corresponding labels using the `for` attribute
* Providing clear and concise error messages
* Implementing focus management to highlight active elements

## Why
Accessible forms are essential for several reasons:
* They enable screen reader users to understand the purpose of form fields
* They help users with visual impairments to identify errors and required fields
* They improve the overall user experience by reducing friction and anxiety

## How
To implement accessible forms, follow these best practices:
* Use the `label` element to associate text with form fields
* Utilize ARIA attributes to provide additional context for screen readers
* Implement focus management using CSS to highlight active elements
* Ensure error messages are clear, concise, and associated with the relevant form field

## One exercise or command
Try adding the `aria-required` attribute to a form field and verify that screen readers announce the field as required.

## Further reading
* [WCAG 2.1 guidelines for form accessibility](https://www.w3.org/TR/WCAG21/#forms)
* [ARIA attributes for accessible forms](https://www.w3.org/TR/wai-aria/')
* [WebAIM resources for accessible forms](https://webaim.org/techniques/forms/)

## Senior interview checkpoint

**Prompt:** Audit a page for accessibility regressions after a redesign; list highest-risk fixes first.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
