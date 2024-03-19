# Sample Package

This Python package serves as a learning tool for understanding coding and programming aspects, particularly in creating a structured starter package. The current demo use case involves generating a UUID from a random group of integers, which is configurable.

## Features

- Generates a UUID from a random group of integers.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/sample-package.git
    # if its a master branch then rename it
    git branch -M main
    git push -uf origin main
    ```

2. Navigate to the cloned directory:
    ```bash
    cd sample-package
    ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # for Unix/Linux
   .\venv\Scripts\activate    # for Windows
   ```

4. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once installed, you can use the package to generate a UUID. Here's an example command:

```bash
python .\src\sample_package\sample_package.py
```

This will produce the following output:
```bash
Message: Hello, World, your request no is: 67676-49450-91095-20864-27637
```

## Testing

You can use the unittest lib for executing the tests

```bash
python -m unittest discover -v -s src/tests -p 'test_*.py'
```

This will produce the following output:
```bash
test_hello_world (test_basic.TestHelloWorld) ... ok
test_generate_random_number (test_basic.TestHelperFunctions) ... ok
test_generate_uuid (test_basic.TestHelperFunctions) ... ok
test_get_answer (test_basic.TestHelperFunctions) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

## Contribution

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to [raise an issue](https://github.com/austinnoronha/python-my-package-sample/issues) or [submit a pull request](https://github.com/austinnoronha/python-my-package-sample/pulls).

## License

This project is licensed under the [MIT License](LICENSE).


## Clone Repo

```
cd existing_repo
git remote add origin https://....git
git branch -M main
git push -uf origin main
```

## Common CMDs

```bash
# linting
pip install pylint
pylint --generate-rcfile > .pylintrc

#-- add in ci/cd pipeline
pylint src/

# documentation
pip install sphinx

# initailize
sphinx-quickstart docs

# to generate docs
sphinx-apidoc -o docs/source src/
cd docs
make html

sphinx-build -M html ./docs/source ./docs/build
```

## Code Structure 

```bash
repo/
│
├── docs/               # Documentation files
│   └── index.md
│
├── src/                # Source code directory
│   ├── your_library/   # Your Python library code
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   ├── module2.py
│   │   └── ...
│   │
│   └── tests/          # Unit tests directory
│       ├── test_module1.py
│       ├── test_module2.py
│       └── ...
│
├── .venv/               # Virtual environment directory
│
├── .gitignore          # Git ignore file
├── requirements.txt    # Dependency requirements file
└── README.md           # Repository README file
```