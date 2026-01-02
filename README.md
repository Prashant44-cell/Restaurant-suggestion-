# Restaurant Suggestion Generator

## Introduction

The Restaurant Suggestion Generator is an AI-powered web application built with Streamlit and LangChain. It uses OpenAI's GPT models to suggest creative restaurant names and menu items based on the selected cuisine type. Whether you're planning a new restaurant or just looking for inspiration, this app provides quick and fun suggestions.

## Features

- **Cuisine Selection**: Choose from a variety of cuisines like Indian, Italian, Chinese, etc.
- **AI-Generated Names**: Get fancy, creative restaurant name suggestions.
- **Menu Item Ideas**: Receive tailored menu item recommendations for the suggested restaurant.
- **User-Friendly Interface**: Simple Streamlit-based UI for easy interaction.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.8 or higher
- A valid OpenAI API key (sign up at [OpenAI](https://platform.openai.com/) if you don't have one)
- Internet connection for API calls

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/restaurant-suggestion-generator.git
cd restaurant-suggestion-generator
```

Replace `your-username` with your actual GitHub username or the repository URL.

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including Streamlit, LangChain, OpenAI, and related packages.

## Configuration

### Set Up OpenAI API Key

1. Obtain your OpenAI API key from the [OpenAI Platform](https://platform.openai.com/account/api-keys).
2. Open the `secret_key.py` file in the project directory.
3. Replace the placeholder with your actual API key:

   ```python
   OPENAI_API_KEY = "your-actual-openai-api-key-here"
   ```

   **Security Note**: Never commit your API key to version control. Consider using environment variables for production.

## Usage

### Running the Application

To start the Streamlit app, run the following command in your terminal:

```bash
streamlit run main.py
```

This will launch the app in your default web browser. You can access it at `http://localhost:8501` (or the URL shown in the terminal).

### How to Use

1. Open the app in your browser.
2. Select a cuisine from the sidebar dropdown (e.g., Indian, Italian).
3. The app will generate a restaurant name and a list of menu items.
4. Enjoy the suggestions!

### Testing the Backend

You can also test the LangChain helper function directly:

```bash
python langchain_helper.py
```

This will print a sample output for "Indian" cuisine.

## Project Structure

```
restaurant-suggestion-generator/
├── main.py                 # Main Streamlit application
├── langchain_helper.py     # LangChain logic for AI suggestions
├── secret_key.py           # API key configuration (keep private)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Troubleshooting

- **API Key Errors**: Ensure your OpenAI API key is valid and has sufficient credits.
- **Import Errors**: Make sure all dependencies are installed via `pip install -r requirements.txt`.
- **Port Issues**: If port 8501 is busy, Streamlit will suggest an alternative port.
- **LangChain Deprecation Warnings**: The code uses some deprecated classes; consider updating to newer LangChain APIs for future-proofing.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web app framework.
- [LangChain](https://www.langchain.com/) for AI chain management.
- [OpenAI](https://openai.com/) for the GPT models powering the suggestions.

## Still the code is not running and in developing phases
