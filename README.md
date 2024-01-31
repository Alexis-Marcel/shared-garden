# Garden Management Platform

## Overview

This web application is designed to revolutionize the way users manage and participate in gardening projects. Built with a React and Tailwind CSS frontend and a Flask Python backend, our platform offers a robust solution for garden enthusiasts to register, create, and join garden projects. Utilizing PostgreSQL with SQLAlchemy ORM for database management, Axios for REST API interactions, and JWT for secure authentication, the application ensures a seamless and secure user experience. Additionally, it features an interactive map powered by Folium, enhancing the user's ability to visualize garden spaces.

## Features

- **User Registration**: Users can sign up with their email, username, first name, last name, and account creation date.
- **Garden Creation and Management**: Users can create gardens with details such as name, owner, type (public or private), and address. Gardens can be joined by other users.
- **Parcel Management**: Within a garden, owners can create parcels named after specific plants, each with its water requirements.
- **Real-Space Representation**: Parcels are divided into units, each with coordinates that define its real-world location in the garden.
- **Task Assignment**: Parcels can have associated tasks with deadlines, names, descriptions, statuses (to-do, in progress, completed), and assigned members.
- **Advanced Optimization**: Utilizes Numpy and Gurobi for complex algorithmic solutions.
- **Interactive Map Visualization**: Leverages Folium for dynamic and interactive garden mapping.

## Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **API Communications**: Axios
- **Authentication**: JWT (JSON Web Tokens)
- **Data Analysis and Optimization**: Numpy, Gurobi
- **Mapping**: Folium

## Installation and Setup

### Prerequisites

- Node.js and npm
- Python 3.x
- PostgreSQL
- Gurobi (with a valid license)

### Backend Setup

1. Clone the repository and navigate to the backend directory.
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database and update the `.env` file with your database credentials.
4. Run Flask migrations to set up your database schema:
   ```
   flask db upgrade
   ```
5. Start the Flask server:
   ```
   flask run
   ```

### Frontend Setup

1. Navigate to the frontend directory.
2. Install npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```
