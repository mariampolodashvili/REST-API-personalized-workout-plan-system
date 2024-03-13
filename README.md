# REST-API-personalized-workout-plan-system
RESTful API for a Personalized Workout Plan system that allows users to create and manage customized workout plans and track their fitness goals.

# Features
- **User Authentication**: Secure user registration, login, and logout functionality using JWT.
- **Exercise Database**: A database of exercises, each with descriptions, instructions for execution, target muscles. The database is pre-filled with 20 exercises
- **Exercise-Plan Association**: Ability for users to select exercises from the predefined list and customize their workout by setting repetitions, sets, duration, or distance.
- **Workout Plans**: Functionality for users to create, change and delete tailored workout plans, specifying workout frequency, goals, daily session duration and exersice plans. 
- **Tracking Goals**: Features for users to track their weight over time.
- **Workout Mode**: A guided, real-time workout feature showing next exercises, sets, repetitions, duration, distance. Options for users to mark exercises as complete.
- **API Documentation**: Interactive API documentation powered by Swagger UI.

## Installation and Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## API Endpoints

### User Authentication:
- Register a new user: `POST /register`
- Log in: `POST /login`
- Log out: `POST /logout`

### Exercises:
- Create a new exercise: `POST /exercises`
- Retrieve all exercises: `GET /exercises`
- Retrieve a specific exercise: `GET /exercises/<exercise_id>`
- Delete an exercise: `DELETE /exercises/<exercise_id>`


### Workout Plans:
- Create a new workout plan: `POST /plans`
- Retrieve all workout plans: `GET /plans`
- Retrieve a specific workout plan: `GET /plans/<plan_id>`
- Update a workout plan: `PUT /plans/<plan_id>`
- Delete a workout plan: `DELETE /plans/<plan_id>`

### Exercise-Plans:
- Select an exercise and create its plan: `POST /exercise_plans/<int:exercise_id>`
- Change an exercise plan: `PUT /exercise_plans/<int:exercise_id>`
- Delete an exercise plan: `DELETE /exercise_plans/<int:exercise_id>`
- Retrieve an exercise plan: `GET /exercise_plans`
- Retrieve an exercise plans: `GET /exercise_plans/<int:exercise_id>`

### Tracking Goals:
- Set fitness goals: `POST /tracking_goal`
- Delete fitness goal: `DELETE /tracking_goals/<tracking_goals_id>`
- Change fitness goal: `PUT /tracking_goals/<tracking_goals_id>`
- Track progress towards goals: `GET /tracking_goal`
- Track progress towards goal: `GET /tracking_goals/<tracking_goals_id>`

### Workout moode:
-Got an exercise to do according to the plan: `GET /workout_mode/{plan_id}`

### API Documentation:
 - Explore the API using Swagger UI: [Swagger UI](https://your-api-documentation-url.com)
