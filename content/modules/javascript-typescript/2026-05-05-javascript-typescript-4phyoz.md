# Module Resolution: ESM vs CJS Interop
## What
Module resolution in JavaScript refers to the process of locating and loading modules. There are two main module systems: CommonJS (CJS) and ECMAScript Modules (ESM). CJS uses `require` and `module.exports` for importing and exporting modules, while ESM uses `import` and `export` keywords.

## Why
The need for interop between ESM and CJS arises because many existing libraries and frameworks are built using CJS, while modern JavaScript applications are increasingly adopting ESM. Understanding how to resolve modules and enable interop between these two systems is crucial for developing hybrid applications that can leverage the benefits of both worlds.

## How
To achieve interop between ESM and CJS, you can use the following approaches:
* Use the `.mjs` file extension for ESM modules and the `.cjs` file extension for CJS modules.
* Utilize the `type` field in `package.json` to specify the module type, either `"commonjs"` or `"module"`.
* Leverage tools like Webpack or Rollup to handle module resolution and interop.
* Employ the `interop` option in tools like `esbuild` to enable default exports for CJS modules.

## One exercise or command
Try the following command to run an ESM module with Node.js:
```javascript
node --experimental-vm-modules your-module.mjs
```
This command enables experimental VM modules, allowing you to run ESM modules directly with Node.js.

## Further reading
* The Node.js documentation on [ESM](https://nodejs.org/api/esm.html) and [CJS](https://nodejs.org/api/modules.html)
* The ECMAScript specification for [Modules](https://tc39.es/ecma262/#sec-modules)
* Articles on [ESM interoperability](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#other_ways_of_loading_modules) and [CJS to ESM migration](https://blog.logrocket.com/migrating-from-commonjs-to-es-modules/)
