# School Management API

This API is designed to manage small schools or training centers, providing functionalities such as user management,
course enrollment, and program management. The API is built using **FastAPI**, with **PostgreSQL** as the database, and
utilizes **Alembic** for database migrations. It is containerized using **Docker** for easy deployment.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Docker Setup](#docker-setup)
  - [Manual Setup](#manual-setup)
- [Running the Application](#running-the-application)
- [Database Migrations](#database-migrations)
- [API Documentation](#api-documentation)
- [Directory Structure](#directory-structure)

## Features

- User management (teachers, students, administrators)
- Enrollment handling for programs and courses
- Program and promotion management
- Time slots and levels for programs
- Supports PostgreSQL with Alembic for database migrations

## Tech Stack

- **FastAPI**: Web framework for building APIs
- **PostgreSQL**: Relational database
- **Alembic**: Database migrations
- **Docker**: Containerization for easy deployment and development
- **Pydantic & SQLAlchemy**: Data validation and ORM
- **Swagger UI**: Auto-generated API documentation for FastAPI

## Prerequisites

Ensure you have the following installed before starting the project:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Getting Started

### Docker Setup

1. Clone the repository: \`\`\`bash git clone https://github.com/your-repo.git cd your-repo \`\`\`

2. Build and run the Docker container: \`\`\`bash docker-compose up --build \`\`\`

   This will start the FastAPI server and PostgreSQL in a Docker container.

### Manual Setup

If you prefer to run the project locally without Docker, follow these steps:

1. Clone the repository: \`\`\`bash git clone https://github.com/your-repo.git cd your-repo \`\`\`

2. Create a virtual environment and install the dependencies: \`\`\`bash python3 -m venv venv source venv/bin/activate
   pip install -r requirements.txt \`\`\`

3. Set up the environment variables. Create a \`.env\` file with the following content: \`\`\`env
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name \`\`\`

4. Run the FastAPI application: \`\`\`bash uvicorn app.main:app --reload \`\`\`

5. The application will be available at \`http://127.0.0.1:8000\`.

## Running the Application

After the setup, run the FastAPI server using one of the following methods:

- **With Docker**: \`\`\`bash docker-compose up \`\`\`
- **Without Docker** (Manual setup): \`\`\`bash uvicorn app.main:app --reload \`\`\`

## Database Migrations

To manage database migrations using Alembic:

1. Generate a new migration after making changes to the models: \`\`\`bash alembic revision --autogenerate -m "your
   message" \`\`\`

2. Apply the migration: \`\`\`bash alembic upgrade head \`\`\`

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit the following URL to
view it:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Directory Structure

\`\`\`
.
├── Dockerfile
├── README.md
├── alembic/               # Alembic migrations folder
├── app/
│   ├── core/              # Configurations
│   ├── db/                # Database connection
│   ├── models/            # Database models
│   ├── modules/           # Features (users, programs, enrollments)
│   └── main.py            # FastAPI application entry point
├── requirements.txt       # Python dependencies
└── run.py                 # Main script to run the application
\`\`\`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
