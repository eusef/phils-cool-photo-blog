import os
from openai import AsyncOpenAI
import re
import sys
import subprocess

# Read the last non-dad-joke commit message
def get_last_non_dad_joke_commit():
    log_output = os.popen('git log --pretty=%B').read().strip().split('\n')
    for message in log_output:
        if not re.search(r'chore: add dad joke to README', message, re.IGNORECASE):
            return message.strip()
    return None

# Generate a dad joke using OpenAI's API based on the commit message
async def generate_dad_joke(commit_message):
    prompt = f"Create a dad joke inspired by the following commit message: \"{commit_message}\""
    try:
        client = AsyncOpenAI(api_key=os.environ['OPENAI_API_KEY'])
        completion = await client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "user", "content": prompt}])
        joke = completion.choices[0].message.content.strip()
        return joke
    except Exception as e:
        print(f"Error generating joke: {e}")
        sys.exit(1)

async def main():
    commit_message = get_last_non_dad_joke_commit()

    if not commit_message:
        print("No suitable commit message found. Skipping.")
        sys.exit(0)

    joke = await generate_dad_joke(commit_message)

    # Append the joke to the README file
    readme_path = 'README.md'
    try:
        with open(readme_path, 'a') as readme_file:
            readme_file.write(f"\n\n## Dad Joke of the Day\n{joke}\n")
        print("Dad joke appended to README.")
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error appending to README: {e}")
        sys.exit(1)

    # Commit and push changes
    def commit_and_push_changes():
        try:
            subprocess.run(["git", "config", "--local", "user.name", "github-actions[bot]"], check=True)
            subprocess.run(["git", "config", "--local", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
            subprocess.run(["git", "add", readme_path], check=True)
            subprocess.run(["git", "commit", "-m", "chore: add dad joke to README"], check=True)
            subprocess.run(["git", "push", "https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/eusef/phils-cool-photo-blog.git"], check=True)
            print("Changes committed and pushed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error committing or pushing changes: {e}")
            sys.exit(1)

    commit_and_push_changes()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
