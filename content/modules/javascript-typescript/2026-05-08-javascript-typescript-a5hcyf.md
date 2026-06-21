# Module Resolution: ESM vs CJS Interop
## What
Module resolution refers to the process by which JavaScript or TypeScript files find and load their dependencies. There are two primary module systems in use today: CommonJS (CJS) and ECMAScript Modules (ESM). Understanding the differences between these two systems is crucial for effective module resolution and interop.

## Why
Historically, Node.js has used the CommonJS module system, while modern web browsers have adopted ECMAScript Modules. As a result, developers often need to handle both formats when working on projects that involve server-side rendering, static site generation, or other technologies that bridge the gap between Node.js and the browser. ESM offers better support for static analysis and tree shaking, making it a popular choice for new projects.

## How
To achieve interop between ESM and CJS, developers can use the `type` field in their `package.json` file to specify the module system. For example, setting `"type": "module"` will enable ESM support in Node.js. When importing CJS modules in an ESM file, the `import` statement can be used with the `.cjs` extension or the `import()` function for dynamic imports. Conversely, CJS modules can require ESM modules using the `require()` function with the `.mjs` extension.

## One exercise or command
Try running the following command in your terminal to create a new Node.js project with ESM support:
```javascript
npm init -y --type=module
```
This will create a new `package.json` file with the `"type": "module"` field set, enabling ESM support in your project.

## Further reading
* [Node.js documentation on ESM](https://nodejs.org/api/esm.html)
* [Types of JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#types_of_javascript_modules)
* [Using ES modules in Node.js](https://www.sitepoint.com/using-es-modules-in-node-today/)
* [CJS to ESM migration guide](https://auth0.com/blog/migrating-from-commonjs-to-es-modules/)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
