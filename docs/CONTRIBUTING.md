# Contributing to GeekBot


## Getting Started

- **Fork the Repository**: Start by forking the repository to your GitHub account.

- **Clone the Repository**: Clone your forked repository to your local machine:
  ```bash
  git clone https://github.com/<your-username>/GeekBot.git
  ```
- **Set Up the Development Environment**:
  ```bash
  python3 -m venv venv
  source ./venv/bin/activate # or ./venv/Scripts/activate.bat
  ```

- **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

## Making Changes

- **Create a Branch**: Create a new branch for your changes:
  ```bash
  git checkout -b feature/your-feature-name
  ```

- **Write Code**: Make your changes in the appropriate files. Ensure your code follows the project's coding standards.

## Linting, Formatting, and Type-checking

- We use [`pylint`](https://pypi.org/project/pylint/) for linting and expect a score above `9`

  ```bash
  pylint ./src
  ```

- We use [`black`](https://pypi.org/project/black/) for code formatting

  ```bash
  black ./src
  ```

- We use [`mypy`](https://pypi.org/project/mypy/) for type-checking and expect no errors at all

  To install type-stubs the first time around

  ```bash
  mypy --ignore-missing-imports --follow-imports silent --install-types --non-interactive ./src
  ```

  ```bash
  mypy ./src
  ```

- You can install these basic tools with

  ```bash
  pip install --force-reinstall --upgrade mypy black pylint
  ```

## Submitting Changes

- **Commit Your Changes**: Write clear and concise commit messages:
  ```bash
  git add .
  git commit -m "Add feature: your-feature-name"
  ```

- **Push Your Changes**: Push your branch to your forked repository:
  ```bash
  git push origin feature/your-feature-name
  ```

- **Open a Pull Request**: Go to the original repository and open a pull request. Provide a detailed description of your changes.
