# 2-Tier Containerized Python (Flask) & MySQL Web Application

A multi-container microservice web application built with Python Flask and MySQL, containerized using Docker and orchestrated with Docker Compose.

## 🏗️ Architecture Flow
`User / Browser` ➔ `Flask Web Container (Port 5000)` ➔ `Docker Bridge Network` ➔ `MySQL Container (Port 3306)` ➔ `Docker Named Volume (Persistent Data)`

## 🛠️ Tech Stack
* **Application:** Python 3.10, Flask
* **Database:** MySQL 8.0
* **Containerization:** Docker, Docker Compose
* **Storage:** Docker Named Volumes (Persistent Storage)

## 🚀 How to Run Locally

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Execution Steps
1. Clone this repository: