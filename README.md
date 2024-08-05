# College Football Realignment API

Welcome to the College Football Realignment API! This API is designed to help visualize and analyze the realignment of college football conferences. Built with Django and Django REST framework, this project showcases my ability to create and manage RESTful APIs, scrape and analyze data, and develop interactive [front-end visualizations](https://github.com/EvanJelley/CFB-Realignment-Site).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Data Analysis](#data-analysis)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

The College Football Realignment API provides endpoints to retrieve and analyze data on college football conferences. This data includes information on team locations, conference affiliations, and more. The primary goal is to allow users to explore realignments based on geographic metrics.

## Features

- **RESTful API**: Easily access data on college football teams and conferences.
- **Data Scraping**: Automated data scraping from Wikipedia to keep information up-to-date.
- **Geographic Analysis**: Calculate geographic centers and distances between teams.
- **Performance Metrics**: Analyze and visualize team performance metrics.
- **Interactive Front-End**: Integrate with a React front-end to create interactive maps and charts (See [CFB Realignment Visualizer](https://github.com/EvanJelley/CFB-Realignment-Site)).

## Installation

To get started with the College Football Realignment API, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/EvanJelley/CFB-Realignment-API.git
    cd CFB-Realignment-API
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

Once the development server is running, you can access the API at `http://127.0.0.1:8000/`. You can use tools like Postman or cURL to interact with the API endpoints.

## API Endpoints

The following endpoints are available:

- **`/api/conferencebyyear/`**: Retrieve a list of all conferences by year.
- **`/api/conferencebyyear/{id}/`**: Retrieve details of a specific conference by year.
- **`/api/conferencelogos/`**: Retrieve a list of all conference logos.
- **`/api/schoollogos/`**: Retrieve a list of all school logos.

### Detailed Endpoint Descriptions

#### `/api/conferencebyyear/`
- **GET**: Retrieve a list of all conferences by year.
  - **Response**: 200 OK
  - **Response Schema**: Array of `AllConferenceByYear` objects

#### `/api/conferencebyyear/{id}/`
- **GET**: Retrieve details of a specific conference by year.
  - **Parameters**:
    - **id** (integer, required): A unique integer value identifying this conference by year.
  - **Response**: 200 OK
  - **Response Schema**: `AllConferenceByYear` object

#### `/api/conferencelogos/`
- **GET**: Retrieve a list of all conference logos.
  - **Response**: 200 OK
  - **Response Schema**: Array of `ConferenceWithLogo` objects

#### `/api/schoollogos/`
- **GET**: Retrieve a list of all school logos.
  - **Response**: 200 OK
  - **Response Schema**: Array of `SchoolWithLogo` objects

## Data Analysis

The API includes functionality for scraping data from Wikipedia, calculating geographic centers, and analyzing the distance between each school. This allows for the exploration of the impact of realignment on the travel requirements for the typical school.

## Technologies Used

- **Backend**: Django, Django REST framework
- **Data Scraping**: BeautifulSoup, Requests
- **Data Analysis**: Pandas
- **Database**: SQLite (for development), Postgres (for production)
- **Deployment**: Heroku (for production)

## Future Enhancements

- **Potential Realignment Scenarios**: Incorporate front-end calculator to show the impact of potential realignments in the college athletics.
- **Expanded Data Sources**: Incorporate additional data sources for more comprehensive analysis such as university spending on athletics, and past team success.
- **K-Nearest Calculations**: Use expanded data to analyze with k-nearest and find optimal conference arrangements.
- **User Authentication**: Add user authentication and authorization for accessing certain endpoints.
- **Caching**: Implement caching to improve performance.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact me at [jelleyevan@gmail.com](mailto:jelleyevan@gmail.com).