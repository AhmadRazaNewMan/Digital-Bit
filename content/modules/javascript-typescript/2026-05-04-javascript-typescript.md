# Module Resolution: ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. There are two primary module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses the `require` function to import modules, while ESM uses the `import` statement.

## Why
Understanding the differences between ESM and CJS is crucial for effective module resolution and interop. ESM offers better support for tree-shaking, static analysis, and asynchronous loading, whereas CJS provides a more traditional, dynamic approach to module loading. Interoperability between the two systems is essential for seamless integration of third-party libraries and legacy code.

## How
To achieve ESM and CJS interop, developers can use the following strategies:
* Use the `type` field in `package.json` to specify the module type (e.g., `type: "module"` for ESM).
* Utilize the `interop` field in `tsconfig.json` to enable interoperability between ESM and CJS.
* Employ the `__esModule` flag to indicate whether a module is an ESM or CJS module.

## One exercise or command
Try running the following command to verify the module type of a package: `node --experimental-vm-modules your-package.mjs`. This command loads the specified package as an ESM module.

## Further reading
* [ECMAScript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
* [Node.js Documentation: ES Modules](https://nodejs.org/api/esm.html)
* [TypeScript Documentation: Modules](https://www.typescriptlang.org/docs/handbook/modules.html)
* [CJS vs ESM: Which Module System to Use](https://blog.logrocket.com/cjs-vs-esm-which-module-system-to-use/)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
