# phils-cool-photo-blog

**<u>*This demo will be presented live in a Webinar on Monday December 16th.*</u>**

Here’s what you’ll learn:
 • How to access secrets in your workflows with ease
 • How to connect 1Password with GitHub Actions
 • Live demo and Q&A with experts
 • Bonus: How to "automatigcally" generate AI-powered README updates

📅 Date: Monday, December 16

⏰ Time: 9am PST / 12pm EST

📍 Location: Online — Save your spot here

This session is ideal for developers, DevOps, and SecOps professionals who want to streamline workflows and ensure sensitive information stays out of your repos.

👉 Register now to save your spot! - https://www.linkedin.com/feed/update/urn:li:activity:7271943456992731136/



------------



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



## Dad Joke of the Day

Why did the programmer update README.md on the weekend?

Because he wanted everyone to be more certain about what they're committing to!
