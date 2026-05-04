# Form Accessibility: Labels, Errors, Focus Management
## What
Form accessibility is crucial for ensuring that all users, including those with disabilities, can interact with web forms easily. This involves providing proper labels, handling errors, and managing focus effectively. Key aspects include:
* Associating form fields with their corresponding labels
* Displaying error messages and providing suggestions for correction
* Managing focus to enable easy navigation using assistive technologies

## Why
Implementing form accessibility features is essential for several reasons:
* It ensures that users with visual or motor impairments can use web forms independently
* It enhances the overall user experience by providing clear and concise feedback
* It helps to avoid potential legal issues related to non-compliance with accessibility guidelines

## How
To achieve form accessibility, developers can follow these best practices:
* Use the `<label>` element to associate form fields with their corresponding labels
* Implement ARIA attributes to provide screen readers with additional information about form fields and errors
* Use JavaScript to manage focus and provide visual feedback when form fields receive focus or contain errors

## One exercise or command
Try adding the `autocomplete` attribute to a form field and observe how it improves the user experience:
```html
<input type="email" id="email" autocomplete="email">
```
This attribute helps users by pre-filling the form field with their saved email address, reducing the need for manual input.

## Further reading
* [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/)
* [ARIA attributes for accessibility](https://www.w3.org/TR/wai-aria/)
* [Form accessibility best practices](https://www.w3.org/WAI/tutorials/forms/)
