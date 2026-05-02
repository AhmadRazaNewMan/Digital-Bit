# Module Resolution ESM vs CJS Interop
## What
Module resolution in JavaScript and TypeScript refers to the process of locating and loading modules. ESM (ECMAScript Modules) and CJS (CommonJS) are two different module systems used in JavaScript. ESM is the standard for modular JavaScript, while CJS is a legacy system. Understanding the differences between ESM and CJS is crucial for effective module resolution.

## Why
The main reason for using ESM over CJS is that ESM provides better support for tree-shaking, static analysis, and other build-time optimizations. However, many existing libraries and frameworks still use CJS, making interop between ESM and CJS necessary. TypeScript supports both ESM and CJS, and its module resolution system can handle interop between the two.

## How
In TypeScript, the `moduleResolution` option in the `tsconfig.json` file determines how modules are resolved. The `node` option uses the Node.js module resolution algorithm, which supports both ESM and CJS. The `nodeNext` option uses the Node.js module resolution algorithm with support for ESM and CJS interop. To enable ESM support in a TypeScript project, the `type` option in the `package.json` file should be set to `module`.

## One exercise or command
To test ESM and CJS interop in a TypeScript project, create a new TypeScript project with the following `tsconfig.json` file:
```json
{
  "compilerOptions": {
    "module": "nodeNext",
    "moduleResolution": "nodeNext",
    "outDir": "build"
  }
}
```
Then, create a new file `main.ts` with the following content:
```typescript
import { foo } from './foo.cjs';
console.log(foo);
```
And a new file `foo.cjs` with the following content:
```javascript
module.exports = { foo: 'bar' };
```
Run the command `tsc` to compile the TypeScript code, and then run `node build/main.js` to execute the compiled code.

## Further reading
* [TypeScript documentation on module resolution](https://www.typescriptlang.org/docs/handbook/module-resolution.html)
* [Node.js documentation on ESM](https://nodejs.org/api/esm.html)
* [Node.js documentation on CJS](https://nodejs.org/api/modules.html)
* [TypeScript configuration options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
