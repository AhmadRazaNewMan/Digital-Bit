# Module Resolution: ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. There are two primary module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses `require` and `module.exports`, while ESM uses `import` and `export`.

## Why
Understanding module resolution is crucial for interoperability between CJS and ESM. As JavaScript and TypeScript projects increasingly adopt ESM, seamless interaction with existing CJS modules is essential. Interop issues can arise due to differences in module syntax, resolution, and loading mechanisms.

## How
To achieve interop between ESM and CJS, developers can use the following strategies:
* Use `import()` function to dynamically import CJS modules in ESM
* Employ `export` syntax in CJS modules to make them compatible with ESM
* Leverage tools like `esbuild` or `webpack` to handle module resolution and interop

## One exercise or command
Try running the command `node --experimental-vm-modules your-esm-file.mjs` to test ESM module resolution in Node.js.

## Further reading
* TypeScript documentation on [Module Resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
* MDN Web Docs on [ECMAScript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
* Node.js documentation on [ESM support](https://nodejs.org/api/esm.html)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
