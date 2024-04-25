# LLaMA3 Chatbot

A Streamlit application that allows users to chat with the LLaMA3 language model using the Groq API.

## Features

- User-friendly chat interface
- Adjustable model parameters (temperature, top-p, and maximum sequence length)
- Customizable pre-prompt text
- Clear chat history button
- Logout button

## Requirements

- Python 3.11
- Streamlit
- Groq API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/llama3-chatbot.git
```

2. Navigate to the project directory:

```bash
cd llama3-chatbot
```

3. Install the required dependencies:

```bash
pip install streamlit groq
```

4. Set your Groq API key as an environment variable:

```bash
export GROQ_API_KEY=your_api_key
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. The application will open in your default web browser.
3. Adjust the model parameters and pre-prompt text as desired in the sidebar.
4. Start chatting with the LLaMA3 model by typing your messages in the input box.
5. Use the "Clear History" button to clear the chat history or the "Logout" button to log out of the application.

## Code Structure

- `app.py`: Main application file containing the Streamlit code.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the user interface framework
- [Groq](https://www.groq.io/) for the LLaMA3 language model API
