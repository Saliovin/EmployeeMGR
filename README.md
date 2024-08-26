# Sprout Exam
A fullstack employee management app

## Project Setup

### Clone the repository

```
git clone https://github.com/Saliovin/Sprout-Exam.git
```

### Run Docker Compose

```
docker compose up --build
```

If you would like to run the app without docker compose, check the READMEs in the backend and frontend directories

## Question - Answer
Q: If we are going to deploy this on production, what do you think is the next
improvement that you will prioritize next? This can be a feature, a tech debt, or
an architectural design.

A: Here are some priority improvements on the project
- Improve tests
    - As of now tests are a single positive test case per unit. Adding more positive test cases and negative test cases will ensure dev security and code quality
- Move to a 3rd Party Auth Service
    - Managing authentication on top of developing a service is difficult and leads to compromising security
- Improve error handling on the frontend
    - The frontend is missing visual cues for many errors. Currently handles errors through logging