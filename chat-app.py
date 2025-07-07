import os
from dotenv import load_dotenv

# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        if not project_endpoint or not model_deployment:
            raise ValueError("PROJECT_ENDPOINT or MODEL_DEPLOYMENT is not set in the .env file.")
        
        # Initialize the project client
        project_client = AIProjectClient(            
            credential=DefaultAzureCredential(
                exclude_environment_credential=True,
                exclude_managed_identity_credential=True
            ),
            endpoint=project_endpoint,
        )

        # Get a chat client
        openai_client = project_client.inference.get_azure_openai_client(api_version="2024-10-21")

        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text.strip()) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = openai_client.chat.completions.create(
                model=model_deployment,
                messages=prompt
            )
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == '__main__': 
    main()
