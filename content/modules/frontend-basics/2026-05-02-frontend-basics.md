# Form Accessibility: Labels, Errors, Focus Management
## What
Form accessibility refers to the practice of making web forms usable by everyone, including people with disabilities. This involves providing alternative text for form elements, using ARIA attributes, and managing focus to ensure that users can navigate and interact with forms using various devices and assistive technologies. Key aspects of form accessibility include labels, error handling, and focus management.

## Why
Accessible forms are essential for ensuring that all users, including those with visual, auditory, motor, or cognitive disabilities, can complete and submit forms successfully. Inaccessible forms can lead to frustration, abandonment, and even legal issues. Moreover, accessible forms improve the overall user experience, making it easier for everyone to use and interact with web applications.

## How
To create accessible forms, developers should follow best practices such as:
* Providing explicit labels for form elements using the `label` element
* Using ARIA attributes to describe dynamic content and interactive elements
* Implementing robust error handling and feedback mechanisms
* Managing focus to ensure that users can navigate forms using keyboards and other devices
* Testing forms with various assistive technologies, such as screen readers and keyboard-only navigation

## One exercise or command
Try adding the `autocomplete` attribute to a form field and test how it affects the user experience, especially for users with disabilities. For example: `<input type="email" id="email" autocomplete="email">`

## Further reading
* W3C Web Accessibility Initiative (WAI) - Form accessibility guidelines
* MDN Web Docs - Accessibility and inclusive design
* WebAIM - Creating accessible forms
* ARIA Authoring Practices - Form examples and best practices
* WCAG 2.1 - Success Criteria for accessible forms

## Senior interview checkpoint

**Prompt:** Audit a page for accessibility regressions after a redesign; list highest-risk fixes first.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
