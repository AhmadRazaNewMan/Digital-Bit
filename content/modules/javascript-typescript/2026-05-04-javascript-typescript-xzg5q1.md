# Generics for Reusable API Wrappers
## What
Generics in TypeScript allow for creating reusable functions and classes that can work with multiple data types. In the context of API wrappers, generics enable developers to write type-safe and flexible code that can handle different types of data returned by APIs.

## Why
Using generics for API wrappers provides several benefits, including:
* Improved type safety: Generics ensure that the correct data types are used, reducing the risk of type-related errors.
* Increased flexibility: Generics enable API wrappers to work with various data types, making them reusable across different applications and APIs.
* Better code maintainability: With generics, developers can write more generic code that can be easily modified or extended to support new data types.

## How
To create a reusable API wrapper using generics, developers can follow these steps:
* Define a generic interface or class that represents the API wrapper.
* Use type parameters to specify the data types that the wrapper can work with.
* Implement the wrapper's methods and properties using the type parameters.

## One exercise or command
Create a simple API wrapper using generics to fetch data from a JSON API:
```javascript
interface ApiResponse<T> {
  data: T;
}

class ApiWrapper<T> {
  async fetchData(): Promise<ApiResponse<T>> {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    const data: ApiResponse<T> = await response.json();
    return data;
  }
}

const apiWrapper = new ApiWrapper<{ title: string; body: string }>();
apiWrapper.fetchData().then((response) => console.log(response.data));
```

## Further reading
* The official TypeScript documentation on generics: https://www.typescriptlang.org/docs/handbook/2/generics.html
* An article on using generics in TypeScript for API wrappers: https://medium.com/@ghastelyn/typescript-generics-for-api-wrappers-5d5f6c0f4e2
* A tutorial on creating reusable API wrappers with TypeScript and generics: https://www.freecodecamp.org/news/building-reusable-api-wrappers-with-typescript-generics-3d2d6f90a2f3/
