# Form Accessibility: Labels, Errors, Focus Management
## What
Form accessibility is a crucial aspect of creating an inclusive user experience. It involves designing forms that can be easily used by everyone, including people with disabilities. This includes providing proper labels, handling errors, and managing focus effectively.

## Why
Accessible forms are essential for several reasons. They ensure that users with disabilities can interact with the form using assistive technologies such as screen readers. Additionally, accessible forms improve the overall user experience, making it easier for all users to fill out forms correctly and efficiently.

## How
To create accessible forms, several techniques can be employed. Firstly, each form element should have a corresponding label that is visibly associated with it. This can be achieved using the `for` attribute on the label element, which matches the `id` attribute of the form element. Secondly, error messages should be provided for invalid input, and these messages should be accessible to screen readers. This can be done using ARIA attributes, such as `aria-invalid` and `aria-describedby`. Finally, focus management is crucial, as it enables users to navigate the form using their keyboard. This can be achieved by ensuring that the tab order of the form elements is logical and consistent.

## One exercise or command
Try adding the `aria-required` attribute to a form element, such as a text input, and verify that a screen reader announces the requirement when the element receives focus.

## Further reading
* The Web Content Accessibility Guidelines (WCAG) provide detailed instructions on creating accessible forms
* The ARIA specification offers guidance on using ARIA attributes to enhance form accessibility
* The W3C tutorial on accessible forms provides practical examples and best practices for creating accessible forms
* Online tools such as Lighthouse and WAVE can be used to test the accessibility of forms and identify areas for improvement

## Senior interview checkpoint

**Prompt:** Explain hydration mismatch root causes and debugging strategy in SSR apps.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
