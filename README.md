# Sample app using Flask, Postgres and Docker

## Setup
1. Clone this repo
2. Setup virtual environment e.g. venv
	* python3 -m venv app
3. Install alembic (only if you want to create migrations)
	* source bin/activate (activate venv)
	* pip3 install alembic
	* note: the alembic folder has been renamed to migrations
	* note: alembic.ini has been moved to migrations/
	* use -c migrations/alembic.ini on all alembic calls
4. Build the images
	* docker-compose build
5. Start the containers
	* docker-compose run -d
6. Navigate to localhost:5000 (should say Hello World!)
7. Navigate to localhost:5000/create (should say Created Simon Olsson!)