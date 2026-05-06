# Generics for Reusable API Wrappers
## What
Generics in TypeScript allow for creating reusable functions and classes that can work with multiple data types. When it comes to wrapping APIs, generics can help create flexible and type-safe wrappers that can handle different types of data.

## Why
Using generics for API wrappers provides several benefits, including:
* Improved code reusability: Generics enable you to write a single wrapper that can work with multiple data types, reducing code duplication.
* Enhanced type safety: Generics help ensure that the correct data types are used, preventing type-related errors at runtime.
* Better maintainability: With generics, you can modify the wrapper to support new data types without modifying the underlying code.

## How
To create a reusable API wrapper using generics in TypeScript, you can follow these steps:
* Define a generic interface for the API response data
* Create a generic class or function that takes the response data type as a type parameter
* Use the type parameter to define the type of the response data in the wrapper

## One exercise or command
Create a simple API wrapper using generics that can handle both JSON and XML data:
```typescript
interface ApiResponse<T> {
  data: T;
}

class ApiWrapper<T> {
  async fetchData(): Promise<ApiResponse<T>> {
    // Simulate API call
    const response = await fetch('https://example.com/api/data');
    const data: T = await response.json();
    return { data };
  }
}

// Usage
const jsonWrapper = new ApiWrapper<{ id: number; name: string }>();
const xmlWrapper = new ApiWrapper<string>();

jsonWrapper.fetchData().then((response) => console.log(response.data));
xmlWrapper.fetchData().then((response) => console.log(response.data));
```

## Further reading
* TypeScript documentation on generics: https://www.typescriptlang.org/docs/handbook/generics.html
* Example use cases for generics in API wrappers: https://www.freecodecamp.org/news/how-to-use-generics-in-typescript/
* Best practices for using generics in TypeScript: https://www.tutorialspoint.com/typescript/typescript_generics.htm
* Type inference in TypeScript: https://www.typescriptlang.org/docs/handbook/type-inference.html
