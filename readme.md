# Blog Generation System

## Overview
This project implements a blog generation system that uses a language model (GPT-3.5) along with LangChain tools to generate well-structured blogs based on given topics. The system operates as an agent-based system, utilizing multiple tools to gather information and create high-quality blog content.

## Features
- **Agent-Based System**: Utilizes LangChain agents and tools to gather information and generate content.
- **Language Model**: Uses OpenAI's GPT-3.5-turbo model to generate blog content.
- **Information Gathering**: Leverages Wikipedia, DuckDuckGo, and Arxiv tools to gather relevant information for the blog topic.
- **Structured Output**: Produces blogs with clearly defined sections: Heading, Introduction, Content, and Summary.

## Requirements
- Python 3.10
- OpenAI API Key
- LangChain

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/riphunter7001x/Blog-Generation-System
   cd Blog-Generation-System
   ```

2. **Create a Conda Environment and Activate It:**
    ```bash
    conda create -n blog-gen python=3.10
    conda activate blog-gen
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables:**
    - Create a .env file in the root directory of the project.
    - Add your OpenAI API key to the .env file:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```
## Usage

1. **Run the System:**
    ```bash
    python blog_genrator_app.py
    ```
2. **Input the Blog Topic:**
    - When prompted, enter the topic for the blog generation
    ```bash
    Enter topic for blog generation (or type 'exit' to quit):
    ```
3. **View and Save the Generated Blog:**

- The generated blog will be printed on the screen and saved to the generated_blogs directory with the topic name as the filename.
- The system will display a success message indicating the location of the saved blog.

## Example

1. **Input:**

    ```bash
    Enter topic for blog generation (or type 'exit' to quit): The Future of Artificial Intelligence
    ```

2. **Output (saved to generated_blogs/The_Future_of_Artificial_Intelligence.txt):**



## Challenges Encountered
- **Tool Integration**: Ensuring the proper integration and usage of LangChain tools (Wikipedia, DuckDuckGo, Arxiv) required careful configuration and testing.
- **Prompt Design**: Crafting a prompt that consistently generates well-structured and informative blog content took multiple iterations and refinements.

## Suggestions for Improvement
- **Custom Tools**: Develop custom tools for more specialized information gathering.
- **Enhanced Prompt**: Further refine the prompt to improve the coherence and relevance of the generated content.
- **User Interface**: Add a simple UI to enhance user experience and make the system more accessible.

## License
This project is licensed under the MIT License.

## Acknowledgments
- OpenAI for providing the GPT-3.5-turbo model.
- LangChain for offering powerful tools and agents for language model integration.

## Contact
For any questions or issues, please contact adi.varpe117@gmail.com




