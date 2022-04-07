# To build & run the program
pre-build:
	pip install --upgrade pip && \
	pip install -r requirements.txt

local-env:
	make pre-build && \
	docker-compose up -d

run-local:
	make local-env && \
	cd src && \
	flask run

#To build and run the test cases
pre-test-build:
	pip3 install --upgrade pip && \
	pip3 install -r requirements_test.txt


local-test-setup:
	make pre-test-build && \
	docker-compose up -d

test-unit:
	pytest

# To run test case using postman collections
run-postman-collection:
	brew install newman && /
	newman run postman_collection.json




