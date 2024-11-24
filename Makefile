# Define default target
.PHONY: clean test build

# Clean task: Remove any previous build artifacts
clean:
	rm -rf dist/            # Remove the dist directory

# Test task: Run unit tests
test:
	- python -m unittest discover -s . -p "test_*.py"
	

# Build task: Clean, run tests, and create a deployable package
build: clean test
	mkdir dist              # Create a dist directory
	cp app.py dist/         # Copy the main application file to dist
	echo "Build successful. Files are in the 'dist' folder."