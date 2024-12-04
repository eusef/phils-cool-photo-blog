# phils-cool-photo-blog

A demo blog based on Docusaurus showing how 1Password and Github Actions can be used for development &amp; deployment.

This demo contains two parts.

1. Part 1 is a deployment script that summarizes the changes of the last commit and then updates the README with a Dad Joke summary of the changes. You will see these in the './github/workflow/run-python-ai-summarizer-script.yml' file. that interns runs the "append_dad_joke.py" script found in the root of the repo.

- This Github Action uses 1Password's Github action to pull in an OpenAI API token and make a call that intern updates the Dad Joke Section of the README file (this file).
- Documentation on how to configure access to a 1Password vault is forthcoming.

2. Part 2 is a Docusaurus blog, that a developer would use to create a nice little photography blog within github pages. More on this later :D.

Live View of the Deployed Project
- https://eusef.github.io/phils-cool-photo-blog/

For more information about the 1Password GitHub Action

- https://developer.1password.com/docs/ci-cd/github-actions/

// Below this spot are all the Dad Jokes based on a summary of the last commit!

