# File Uploads: Streaming vs Buffering Tradeoffs
## What
File uploads are a crucial aspect of many web applications, allowing users to share files with others or store them for later use. When handling file uploads, developers have two primary approaches: streaming and buffering. Streaming involves processing the file in a continuous flow, while buffering involves loading the entire file into memory before processing it.

## Why
The choice between streaming and buffering depends on the specific requirements of the application. Streaming is suitable for large files, as it avoids loading the entire file into memory, reducing the risk of memory overflow errors. On the other hand, buffering is faster for small files, as it allows for immediate processing without the need for continuous streaming. Understanding the tradeoffs between these approaches is essential for designing efficient and scalable file upload systems.

## How
To implement streaming file uploads, developers can use libraries that support streaming, such as Node.js's `stream` module. This module allows developers to create readable streams that can be piped to writable streams, enabling continuous processing of the uploaded file. For buffering, developers can use libraries that provide buffering capabilities, such as Node.js's `fs` module. This module allows developers to read the entire file into memory before processing it.

## One exercise or command
To demonstrate the difference between streaming and buffering, try running the following command using Node.js's `stream` module:
```javascript
const fs = require('fs');
const { createReadStream } = require('fs');

const readStream = createReadStream('largefile.txt');
readStream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes`);
});
readStream.on('end', () => {
  console.log('File upload complete');
});
```
This command creates a readable stream for a large file and logs the number of bytes received as the file is being uploaded.

## Further reading
* Benefits of streaming:
  * Reduced memory usage
  * Improved performance for large files
  * Support for real-time processing
* Benefits of buffering:
  * Faster processing for small files
  * Simplified implementation
  * Support for random access to file data
* Node.js streaming documentation: https://nodejs.org/api/stream.html
* Node.js fs module documentation: https://nodejs.org/api/fs.html

## Senior interview checkpoint

**Prompt:** Design idempotent retry handling for a payment callback endpoint.

**What a senior answer should include**

- Constraints first (traffic, latency, reliability, ownership boundaries).
- Tradeoffs with at least two viable alternatives.
- Failure modes, observability signals, and rollback plan.
- A measurable success criterion after rollout.
