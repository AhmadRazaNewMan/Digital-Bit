# Module Resolution: ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. There are two primary module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses `require` and `module.exports`, while ESM uses `import` and `export`.

## Why
Understanding module resolution is crucial for interoperability between CJS and ESM. As the JavaScript ecosystem evolves, many libraries are transitioning from CJS to ESM, and developers need to know how to work with both systems.

## How
In Node.js, the `type` field in `package.json` determines the module system. When `type` is set to `module`, Node.js uses ESM. Otherwise, it defaults to CJS. To enable ESM interop, use the `esm` package or the `--experimental-vm-modules` flag. In TypeScript, the `moduleResolution` option in `tsconfig.json` controls how modules are resolved.

## One exercise or command
To test ESM interop, create a new project with a `package.json` file containing `"type": "module"`. Then, run `node --experimental-vm-modules index.js` to execute an ESM file.

## Further reading
* [Node.js documentation on ESM](https://nodejs.org/api/esm.html)
* [TypeScript documentation on module resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
* [ECMAScript Modules in Node.js](https://nodejs.org/api/modules.html)

## Senior interview checkpoint

**Prompt:** Design cancellation-safe async flow with AbortController for chained requests.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
