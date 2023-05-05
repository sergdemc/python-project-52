[![Actions Status](https://github.com/sergdemc/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/sergdemc/python-project-52/actions)
[![run tests](https://github.com/sergdemc/python-project-52/actions/workflows/run_test.yml/badge.svg)](https://github.com/sergdemc/python-project-52/actions/workflows/run_test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/7e17dccfb736bd7985d2/maintainability)](https://codeclimate.com/github/sergdemc/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7e17dccfb736bd7985d2/test_coverage)](https://codeclimate.com/github/sergdemc/python-project-52/test_coverage)


---

## Task manager
Task Manager is a full-featured application based on the Django framework that enables you to register, create, delete, and modify tasks, labels, and statuses. You can assign task executors and filter tasks by tags, statuses, and executors, or filter only the tasks that you have created.

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.10+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### PostgreSQL

As database the PostgreSQL database system is being used. You need to install it first. You can download the ready-to-use package from [official website](https://www.postgresql.org/download/) or use Homebrew:
```shell
>> brew install postgresql
```

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/sergdemc/python-project-52.git && cd python-project-52
```

Then you have to install all necessary dependencies:

```bash
>> make install
```

Create .env file in the root folder and add following variables:
```
DATABASE_URL = postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY = '{your secret key}'
```
Run commands from `database.sql` to create the required tables.

---

## Usage

Start the gunicorn Django server by running:
```bash
make start
```
By default, the server will be available at http://0.0.0.0:8000. 

_It is also possible to start it local in development mode with debugger active using:_
```bash
make dev
```
_The dev server will be at http://127.0.0.1:8080._


To add a new site, enter its address into the form on the home page. The specified address will be validated and then added to the database.

After the site is added, you can start checking it. A button appears on the page of a particular site, and clicking on it creates an entry in the validation table.

You can see all added URLs on the `/urls` page.
https://web-production-fb23.up.railway.app