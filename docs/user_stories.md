# Coding Test: Develop an AI E-Commerce Assistant 

## Objective: 

Create a Python application that demonstrates your ability to work with OpenAI's Assistants API and function calling. Build an AI assistant for an e-commerce platform to help users interact with product information. 

## Task 

Build an AI assistant that can answer user queries about products in an e-commerce store. 

Use python and the OpenAI Assistants API with the gpt-4o model. 

Implement function calling to retrieve product information from a mock product catalog. 

## Requirements 

### Setup 

Use Python for the project. 

Install the OpenAI Python SDK. 

Set up the Assistants API using the gpt-4o model. 

### Create an Assistant 

__Name__: Choose an appropriate name for your assistant (e.g., "ShopBot"). 

__Instructions__: Define the assistant's role in helping users with product queries. 

__Function Calling__: Enable function calling to interact with product data. 

### Mock Product Catalog 

Create a simple product catalog within your application (e.g., an array or JSON file). 

Include at least 5 products with details: 

__Product ID__

__Name__

__Description__

__Price__

__Stock Availability__

### Implement Functions 

Define functions that the assistant can call, such as: 

__getProductInfo(productName)__: Returns product details. 

__checkStock(productName)__: Checks if the product is in stock. 

### User Interaction 

Simulate a conversation where the user asks about products, and the assistant responds using function calls. 

Example: 

User: "Tell me about the 'EcoFriendly Water Bottle'." 

Assistant: Provides details by calling getProductInfo. 

User: "Is it available?" 

Assistant: Checks stock using checkStock and informs the user. 

### Execution 

The assistant should process user messages and generate responses using the Assistants API. 

Implement function calling so the assistant can fetch and provide accurate product information. 

Display the conversation in the console or a simple interface. 

### Documentation 

Comment your code to explain your logic. 

Include a brief README with instructions on how to install dependencies and run your application. 



#### Resources

https://platform.openai.com/docs/assistants/quickstart 

https://platform.openai.com/docs/assistants/overview 

https://platform.openai.com/docs/guides/function-calling 

https://www.youtube.com/watch?v=p0I-hwZSWMs