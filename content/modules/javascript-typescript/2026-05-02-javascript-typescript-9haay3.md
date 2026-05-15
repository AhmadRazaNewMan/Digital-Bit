# Module Resolution: ESM vs CJS Interop
## What
Module resolution refers to the process by which a JavaScript or TypeScript module locates and loads its dependencies. There are two primary module systems in use today: ECMAScript Modules (ESM) and CommonJS (CJS). Understanding the differences between these two systems is crucial for effective module resolution and interop.

## Why
The main reason for using ESM over CJS is to take advantage of the built-in support for tree-shaking, which can significantly reduce the size of the bundled code. Additionally, ESM provides better support for static analysis and optimization. However, many existing libraries and modules are still written in CJS, making interop between the two systems necessary.

## How
To achieve interop between ESM and CJS, you can use the `type` field in your `package.json` file to specify the module system. For example, setting `"type": "module"` will tell Node.js to use ESM for the package. Alternatively, you can use the `.mjs` extension for ESM files and the `.cjs` extension for CJS files. When importing a CJS module in an ESM file, you can use the `import()` function with the `assert` option to specify the type of the module.

## One exercise or command
Try running the following command to test ESM interop with a CJS module:
```javascript
node --experimental-specifier-resolution=node mymodule.mjs
```
In this example, `mymodule.mjs` is an ESM file that imports a CJS module.

## Further reading
* The [Node.js documentation](https://nodejs.org/api/esm.html) provides an overview of ESM support in Node.js
* The [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/modules.html) covers module resolution and interop in TypeScript
* The [ECMAScript specification](https://tc39.es/ecma262/) defines the syntax and semantics of ESM
* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) provide a comprehensive guide to JavaScript modules and interop

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
