from src.agents import tools
from src.prompt import prompt
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from a .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI language model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Create an OpenAI tools agent using the LLM, tools, and prompt
agent = create_openai_tools_agent(llm, tools, prompt)

# Create an agent executor with the agent and tools, set to verbose mode for detailed output
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Define the output file path for saving generated blogs
output_file_path = r"./generated_blogs"

# Ensure the output directory exists
os.makedirs(output_file_path, exist_ok=True)

# Start a loop to continuously ask for topics until "exit" is entered
while True:
    topic = input("Enter topic for blog generation (or type 'exit' to quit): ")
    
    # Break the loop if the user types 'exit'
    if topic.lower() == 'exit':
        print("Exiting the blog generation tool.")
        break
    
    # Invoke the agent executor with the provided topic
    response = agent_executor.invoke({"topic": topic})
    
    # Print the generated blog output
    print(response["output"])
    
    # Create a filename from the topic
    filename = f"{output_file_path}/{topic.replace(' ', '_')}.txt"
    
    # Save the generated blog to a text file with the topic as the heading
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Heading: {topic}\n\n")
        file.write(response["output"])
    
    # Print a success message
    print(f"Blog saved successfully to {filename}")

