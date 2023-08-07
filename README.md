<|SOS|> `xongptshnvm`

# xongptshnvm

   - xonsh (bash &amp; python) &amp; nvm (node version manager) environment for Llama2, gpt4all, LocalAI, gpt4free, git-llm, large foundational model API's, local-llm etc LogSeq integration and Zettelkasten note-taking 'knowledge base'
   - Projects primary goals:
       - Maintenance of a 'text:text' [[RLHF]] training and conversational database for all LLM interactions within the system
       - Maintenance of 'requirements.txt', 'package.json', 'instructions.md', and other persistence and reproduction schemas for all elements and dependencies
       - CI/CD and 'best practices', [[heuristics]], which allow for effective collaboration between various ai chatbot [[agent]] and LLM based applications, functions, modules, and libs
       - The most important of all of the **rules of thumb** is the performance, illustration, or generation of a cognitive process
           - A [[cognitive process]] is one which takes place within the object oriented paradigm bootstrapped within the chain of cognition ($ToT) or presented within the specific ($context), ($prompt), or ($chat) of every single ($instantiation) within the process
           - They include information encoded in plain text for use in NLP algorithms and functions which is organized in various schemas and methods but which can be simply modeled as a hierarchical data structure like html
           - In addition to the encoded NLP data, a cognitive process represents a specific contiguous (sorted) collection of `Response:` and `Query:`, call-and-response or back-and-fourth 'dialogue' or what is referred to as ($cognition), the process itself then bootstraps furthermore ($cognition) which generally takes the shape of a [[TRAIN OF THOUGHT]] ($ToT)
       - In the context of cognitive processes and thinking, a [[TREE OF THOUGHT]], an alternative label for ($ToT), refers to a representation of a person's or an agent's thought process as a tree-like graph-type object which is sorted and traversable 
       - Each node in the tree represents a distinct thought or cognitive state, and the edges between nodes represent the flow of reasoning or exploration from one thought to another.
           - In the context of unix stdio a node would be a CLI application and an edge would be the parameters passed via stdio to another application or node/endpoint.
           - The applications of this abstraction represent the ability for the sorted data structure and sum-total of available ($context) for each ($instantiation) to resolve in an organized and methodical fashion, enabling [[meta-cognition]], or the analysis and re-analysis of the on-going or future ($ToT)
       - Establishment, boostrapping, and maintenance of the (performance of an) [[operation]] of (a) standardized 'cognitive' processes utilizing parameter-passing mechanisms including unix stdio (on ubuntu), xonsh scripting, python, and npm modules as well as custom typescript or other code which preforms work on the hierarchical ($ToT)
       - Provide a step-by-step thought process leading to the final `Return:` value which will involve a multi-step cognitive process involving the 'evolution' of many ordered sub-processes which may also involve their own `Return:` but which all fit within the hierarchical data structure provided by the other **rules of thumb** and the ($context) available within this ($instantiation).
       - Here is an example of a cognitive NLP hierarchy which can usefully be applied to accomplish cognitive processes with a user in a 'chatbot/user' paradigm. The following NLP semantic logic block is given in backticks like a `codeblock`:

        ```
        You will guide the user through a series of questions one at a time.
        
        The first question is broad, and subsequent questions become more specific.
        
        1. Identify the [key element/variable] in the [problem/scenario/question].
        2. Understand the [relationship/connection] between [element A] and [element B].
        3. [Analyze/Evaluate/Consider] the [context/implication] of the [relationship/connection] between [element A] and [element B].
        4. [Conclude/Decide/Determine] the [outcome/solution] based on the [analysis/evaluation/consideration] of [element A], [element B], and their [relationship/connection].
        5. To fulfill the requirements of the ongoing task, invoke the final return using the key-value pairs and format provided in this {prompt}.
        
        [Answer/Conclusion/Recommendation]: Provide a coherent and logical response based on the train of thought.
        
        In order to preserve the data structure and increase accountability, you are to output your thoughts as you think them while formulating your ultimate return, which you will invoke specifically with a key-value pair after the conclusion of all the steps or all of the work done in a cognitive process. The ultimate `Return:` should be wrapped in backticks to signify code. Remember to show your work continuously and provide all additional information or cognition step-by-step! Pay attention to the initial ($prompt) as well as the evolving ($context) at all times during this instantiation.
        ```
        
  - By utilizing cognitive functions like the above within a chatbot agent's cognitive toolkit, an expanding knowledgebase of increasing complexity and interconnectivity can be fashioned which are useful for both the primary ($user) (and learner) as well as future instantiations of potentially unaffiliated ai agents created within the project filestructure.
  - Other than with stdio and parameter passing mechanisms the primary means of extending cognitive processes is with the encoding of semantic NLP into a ($prompt)-type data object.
  - The final common method of extending a cognitive process is via the use of API and internet which is encoded within the stream in an OOP-fashion in-which the chain of cognition it belongs to maintains [[ownership]] over that api-call which represents a step in the chain of cognition, or the flow of a train of thought.
      - This type of link in a chain of cognition must be accompanied by a [[control]], a fail-safe cognitive state that the ($ToT) can fall down to and which the next agent or semantic/logical operation can continue from in-the-event of some-kind of failure with the external tool usage.
  - Following is another code-blocked example in triple backticks which provides a good example/model "cognitive process" which either represents cognition itself or which is a syntactic or NLP component of a train of thought, parameter-passing or logging mechanisms, or even a ($prompt) object which are used to instantiate new agents or new processes within the chain of cognition. See: 
        
```
# Rules of Thumb & Heuristics
Creating a clear project structure is vital for seamless development. Consider these guidelines:

1. Use consistent naming conventions for keys and values to make understanding and searching easier.
2. Organize related data logically using nesting and arrays.
3. Provide comments to explain complex or ambiguous data.
4. Enhance readability with proper indentation for levels of hierarchy.
5. Keep the structure simple, avoiding unnecessary complexity.
6. Test and validate structured data to ensure accuracy and error-free implementation.
1. **Understand the Project Purpose and Requirements**: Clearly define the project's purpose and target domain(s) such as Prompt Engineering, Prompt Generation, NLP tasks, or AI assistance. This understanding is crucial for effective customization.

2. **Clarity, Specificity, and Context**: Ensure the project is well-defined, specific, and contextually rich to generate desired responses effectively. Avoid ambiguity and vagueness.

3. **Include Relevant Data and Context**: Provide all relevant data and context within the project's objective or files. Use variables or placeholders for dynamic elements or files and folders.
   - **Define Variables and Placeholders**: Identify dynamic elements that require specific values during generation.
   - **Provide Examples and Data Sources**: Offer data examples to fill variables or placeholders, and reference external data sources if applicable.
   - **Contextual References**: Refer to past interactions to maintain context and coherence.

4. **Explicit Instructions and Guidelines**: Clearly specify instructions and constraints for new additions. Ensure even AI models or novices can comprehend the boundaries and limitations. For instance, "Calculate the dot product using a new class method without importing a new python library for it."
   - **Precise Language**: Use clear and concise language to express instructions. Avoid ambiguity or vagueness.
   - **Step-by-Step Instructions**: Break complex tasks into step-by-step instructions for effective user and AI model responses.
   - **Boundary Definitions**: Clearly define limitations for users, contributors, or AI models. Specify allowed methods, CLI arguments, etc.
   - **Example Usage**: Provide correct usage examples with expected responses for desired behavior.
   - **Error Handling**: Include instructions on handling potential errors or unexpected situations. Define fallback options or alternative instructions.

5. **Structured Data Formats**: Utilize JSON to represent the project's data and I/O. Consistent naming, nesting, and comments enhance readability and understanding.
   - **Example of a structured data format**: {"key": "value", "data": "syntax_hint"}
   - The provided JSON string object follows standard syntax with keys and string values enclosed in double quotes (") and separated by colons (:).
   - JSON validation libraries or built-in functions can programmatically validate the syntax.
   - The "syntax_hint" section provides supplementary guidance during messaging creation and organization, unlocking advanced practices.
   - To effectively use this crucial structure, think of key-value pairs as atomic units within an object (hash table).
   - Each key identifies a unique concept and frequently uses lowercase or abbreviated words for readability.
   - Values then provide detailed contents related to their respective keys, associating names with descriptions, facts, or instructions across various domains.
   - Structured data formats allow for easier integration with other systems and applications. eg: Many APIs require data to be in a specific format like json or bash.
   - Use a variety of data structures to store information, including arrays, dictionaries, hash tables, trees, graphs, strings, JSON, and other formats for text-based data.
```
        
   - Having a systematic approach to the storage and retrieval of cognitive processes is vital for making actionable, instructive, and useful cognition. The ($user) does this using [[LogSeq]] and whatever processes are introduced should play nicely with the markdown 'LogSeq' formatting style outlined below:

**Zettelkasten**:
   - Note-taking and knowledge management system
   - Aid in the organization and retrieval of information through interconnected notes
   - Each note represents a discrete piece of knowledge, concept, or idea, is given a unique identifier
   - String identifiers enclosed in double brackets [['double bracketed']] Denoted by the '#' symbol; tags, or links between unique identifiers and the strings they are found within  
   - To facilitate cross-referencing, back-propagation, and linking utilize a graph-type structure with elements and edges between elements as a model
   - Export to [[LogSeq]], it is the preferred [[Zettelkasten]] software which is a native markdown text editor and knowledge base

   - A systematic approach to ($instantiation) of an ($agent) involves the use of a ($prompt) object. See this example:

```
A prompt guides an AI chatbot's responses with instructions and constraints. Some essential means of doing so include:

    Utilizing variables, which act as placeholders to be replaced by specific values during enumeration, evaluation, or formulation.

    Each properly formatted instructive prompt is a prompt object, encompassing all necessary information for a single operation.

    An operation represents the result of a cognitive iteration derived from a train-of-thought of an agent. It is instantiated or being instantiated by a prompt.

    A specific operation must always follow a specific prompt executed by a particular iteration or invocation of an agent.

    Due to the chronological and ordered nature of operations, a specific operation representing an iteration of an agent's train-of-thought must be preceded by a prompt and some contextual information.

    The context of any given iteration, governing each possible operation, is of paramount importance.

    Alongside the prompt itself, the specific context heavily influences generating an ultimate return or the specific train of thought.

    To fulfill the requirements of each iteration, invoke the final return using the provided formatting only after producing the functionally required train of thought for each return.

    Given the object-oriented paradigm within each prompt, the task involves passing plain text as parameters and returning plain text.

The goal is to maintain context and convey relevant information through parameter passing mechanisms.
Incorporating Structured Data Formats

Incorporating structured formats fosters clearer conversations and offers valuable benefits when referencing past interactions. It enables easier recall of key details, follow-up on action items, tracking project progress, identifying patterns and trends, and improving collaboration. Structured data formats allow for easier integration with other systems and applications. For example, many APIs require data to be in a specific format, and using a structured format can make it easier to facilitate and process data from these APIs.
To create a clear structure, consider the following rules of thumb:

    Use consistent naming conventions for keys and values to allow for easier understanding and searching.

    Organize related data in a logical and intuitive way using nesting and arrays.

    Provide context and explanations for complex or ambiguous data through comments.

    Improve readability and denote levels of hierarchy with proper indentation.

    Denote code or programming language syntax using backticks.

    Keep the structure as simple as possible while still meeting your needs, avoiding unnecessary complexity.

    Test and validate your structured data to ensure it is accurate and error-free.

    If presented with a data structure, respond with a data structure.
```


**Constraints**:
   - Scope limited to text files and Markdown [[Plain Text]]
   - Command line interfaces for accessibility [[CLI]]
   - Embrace Unix/POSIX compatibility, employing file-centric [[Scripting]]
   - Consumer hardware limitations [[Hardware Constraints]]
   - When printing debug information, consider redirecting all messages to a log file so that logs are saved permanently.
   - Include docstrings for both your module and any public functions within it so users know what the code does and how to use it.
   - Well-defined endpoints and routes [[Endpoints]]
   - Consistent response formats and codes [[Responses]]
   - Authentication and access control [[Authentication]]
   - Validation of inputs and outputs [[Validation]]
   - Versioning and backward compatibility [[Versioning]]
   - Rate limiting policies [[Rate Limiting]]
   - Implement retries with exponential backoff [[Retries]]
   - OpenAPI/Swagger documentation [[Documentation]]
   - Prefer simplicity and avoid premature optimization [[YAGNI]]
   - Develop intuitions before diving into complexity [[Intuition Building]]
   - Don't repeat yourself (DRY) [[DRY]]
   - Encapsulate complexity behind abstractions [[Abstraction]]
   - Loose coupling between modules [[Loose Coupling]]
   - Separation of concerns [[Separation of Concerns]]
   - Use load balancers to distribute requests [[Load Balancing]]
	 - Virtual environments for isolation [[Virtual Environments]]
   - Pip and PyPI and Miniconda for installing packages [[Pip, PyPI, Conda]]  
   - Setuptools for wrapping and distributing [[Setuptools]]
   - Assertions to catch issues early [[Assertions]]

### Github imports and libs

`insturctions for use and implementation of open-source libraries and imports to the project`

LocalAI Reversed API endpoint from github

   [[LocalAI]] is a dockerized API endpoint for AI models. It is designed to be used as a local alternative to OpenAI's API. It is a reverse-engineered version of the OpenAI API, and it is not affiliated with OpenAI in any way. It is intended to be used for testing and development purposes only.
   - Docker-compose up -d --pull always
   - curl http://localhost:8080/v1/models
   - put your model in the models folder, note its name eg. orca-mini-7b.ggmlv3.q4_0.bin
   ```call
   (3ten) op@deV:~/cognic/LocalAI$ curl http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{
     "model": "orca-mini-7b.ggmlv3.q4_0.bin",            
     "prompt": "A long time ago in a galaxy far, far away",
     "temperature": 0.7
   }'
   ```
   ```response
   {"object":"text_completion","model":"orca-mini-7b.ggmlv3.q4_0.bin","choices":[{"index":0,"finish_reason":"stop","text":", there was a group of people who called themselves the Jedi. They were a religious order dedicated to using the Force for good and fighting against the dark side. One of these Jedi was named Luke Skywalker, who lived on the planet of Tatooine with his family. One day, he received a message from his friend and fellow Jedi, Obi-Wan Kenobi, asking him to come to the desert planet of Dagobah to receive Jedi training from the wise and powerful Master Yoda. Luke accepted the invitation and set off on a journey that would change the course of the galaxy forever."}],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}
   ```
   
<|EOS|>