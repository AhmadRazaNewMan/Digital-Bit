# Module Resolution ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. There are two primary module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses `require` and `module.exports`, while ESM uses `import` and `export`.

## Why
Understanding the differences between ESM and CJS is crucial for interoperability between modules written in different styles. ESM is the standard for modern JavaScript, while CJS is still widely used in older codebases and Node.js environments. Interoperability issues can arise when trying to import CJS modules into ESM code or vice versa.

## How
To achieve interop between ESM and CJS, you can use the following strategies:
* Use `import` statements with `.cjs` file extensions to import CJS modules into ESM code
* Use `export` statements with `module.exports` to export ESM modules to CJS code
* Utilize tools like `esm` or `@std/esm` to enable ESM support in Node.js environments

## One exercise or command
Try running the following command to enable ESM support in a Node.js environment: `node --experimental-vm-modules your-esm-module.mjs`

## Further reading
* [ECMAScript Modules documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
* [Node.js ESM documentation](https://nodejs.org/api/esm.html)
* [ TypeScript documentation on module resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)

## Senior interview checkpoint

**Prompt:** Refactor an API client to discriminated unions; show how this prevents runtime bugs.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
