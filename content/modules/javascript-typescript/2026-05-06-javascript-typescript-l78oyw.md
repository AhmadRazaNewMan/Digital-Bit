# Module Resolution ESM vs CJS Interop
## What
Module resolution in Javascript and Typescript refers to the process of locating and loading modules. ESM (ES Modules) and CJS (CommonJS) are two different module systems used in Javascript. ESM is the standard for modular Javascript, while CJS is a legacy system. Understanding the differences and interop between ESM and CJS is crucial for effective module management.

## Why
The main reason for using ESM over CJS is that ESM provides better support for tree-shaking, static analysis, and module resolution. However, many existing libraries and modules are still written in CJS, making interop between ESM and CJS necessary. Typescript supports both ESM and CJS, and understanding how to use them together is essential for building robust and maintainable applications.

## How
To achieve interop between ESM and CJS, Typescript provides several options. One approach is to use the `type` field in the `package.json` file to specify the module system. For example, setting `"type": "module"` will enable ESM, while setting `"type": "commonjs"` will enable CJS. Another approach is to use the `--module` and `--moduleResolution` flags when compiling Typescript code.

## One exercise or command
Try running the following command to compile a Typescript file using ESM: `tsc --module es2020 --moduleResolution node yourfile.ts`. This will generate a Javascript file that uses ESM.

## Further reading
* The official Typescript documentation on [module resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
* The Node.js documentation on [ESM](https://nodejs.org/api/esm.html)
* A detailed guide on [ESM and CJS interop](https://blog.logrocket.com/es-modules-in-node-today/) 
* Understanding the differences between [ESM and CJS](https://medium.com/@nickchips/es-modules-in-node-today-32efd0a49d4)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
