# Module Resolution ESM vs CJS Interop
## What
Module resolution is the process by which a JavaScript or TypeScript module locates and loads its dependencies. There are two primary module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses the `require` function to import modules, while ESM uses the `import` statement. Understanding how these two systems interact is crucial for effective module resolution.

## Why
In modern JavaScript development, it's common to encounter both CJS and ESM modules. Since Node.js supports both systems, developers must be aware of how to handle interop between them. This knowledge is essential to avoid errors and ensure seamless module resolution in projects that use a mix of CJS and ESM modules.

## How
To achieve interop between ESM and CJS, developers can use the following approaches:
* Use the `import` statement in ESM modules to import CJS modules, which will be treated as default imports.
* Use the `require` function in CJS modules to import ESM modules, but be aware that this may require additional configuration, such as using the `esm` package or setting the `type` field to `module` in the `package.json` file.
* Utilize tools like `esbuild` or `rollup` to bundle and transform modules, enabling better interop between the two systems.

## One exercise or command
Try running the following command to experiment with ESM and CJS interop:
```bash
node --experimental-specifier-resolution=node index.js
```
This command enables experimental specifier resolution, allowing you to test how Node.js resolves module specifiers.

## Further reading
* [Node.js documentation on ESM](https://nodejs.org/docs/latest/api/esm.html)
* [MDN Web Docs on JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
* [ECMAScript Modules in Node.js](https://www.freecodecamp.org/news/ecmascript-modules-in-node-today/)
* [TypeScript documentation on modules](https://www.typescriptlang.org/docs/handbook/modules.html)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
