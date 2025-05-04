# Streamlit Chatbot Web Application

This project is a Streamlit-based chatbot application that utilizes a local language model and a vector store for retrieving relevant information. The chatbot is designed to answer frequently asked questions (FAQs) related to Philips AI.

## Project Structure

```
streamlit-chatbot-webapp
├── app
│   ├── app.py                # Main application code for the Streamlit chatbot
│   ├── embedding
│   │   └── chroma_db        # Directory for persistent vector store database
│   └── __init__.py           # Marks the directory as a Python package
├── requirements.txt           # Lists the dependencies required for the project
├── .env                       # Stores environment variables
├── .gitignore                 # Specifies files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-chatbot-webapp
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file as needed.

## Running the Application

To run the Streamlit chatbot application, execute the following command in your terminal:
```
streamlit run app/app.py
```

This will start the Streamlit server, and you can access the chatbot in your web browser at `http://localhost:8501`.

## Usage

Once the application is running, you can type your questions into the input box, and the chatbot will respond with relevant answers based on the embedded knowledge.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.