
# Textile Data Scraping and Display

This project scrapes textile data from neighboring countries using Python and displays it on a React-based website with a Django backend.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves:
- Scraping textile-related data from external websites using Python.
- Serving the scraped data through a Django REST API.
- Displaying the data dynamically on a frontend built with React.

## Technologies Used

- **Backend**: Django, Django REST framework
- **Frontend**: React, Axios (for API requests)
- **Scraping**: Python requests and BeautifulSoup

## Setup and Installation

### Prerequisites
- **Node.js** and **npm** for the frontend.
- **Python 3.6+** and **pip** for the backend.

### Step-by-Step Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/textile-data-scraping.git
    cd textile-data-scraping
    ```

2. **Backend Setup**:
    - Navigate to the `backend` directory:
      ```bash
      cd backend
      ```
    - Create and activate a virtual environment:
      ```bash
      python -m venv env
      source env/bin/activate  # On Windows, use `env\Scripts\activate`
      ```
    - Install the Python dependencies:
      ```bash
      pip install -r requirements.txt
      ```
    - Run migrations to set up the Django database:
      ```bash
      python manage.py migrate
      ```
    - Start the Django server:
      ```bash
      python manage.py runserver
      ```

3. **Frontend Setup**:
    - Open a new terminal window and navigate to the `frontend` directory:
      ```bash
      cd ../frontend
      ```
    - Install Node dependencies:
      ```bash
      npm install
      ```
    - Start the React development server:
      ```bash
      npm start
      ```

### Scraping Data
To scrape textile data:
- Run the scraping script located in the `backend` folder, which fetches data and updates the API endpoint:
  ```bash
  python backend/scraper.py
  ```

## Usage

1. **Run both Backend and Frontend Servers**: Ensure both servers are running, and visit `http://localhost:3000` to view the application.

2. **Fetch Data**: Click on the "Fetch Data" button on the React site to load the latest textile data.

## Project Structure

```
textile-data-scraping/
│
├── backend/
│   ├── scraper.py             # Scraping script
│   ├── backend/               # Django project folder
│   │   ├── settings.py
│   │   ├── urls.py
│   └── textile/               # Django app for textile data
│       ├── views.py           # API view functions
│       └── models.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   └── App.js             # Main React component
│   └── package.json
│
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Description of changes"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
