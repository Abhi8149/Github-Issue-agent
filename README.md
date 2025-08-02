# GitHub Issues RAG Agent

An intelligent AI agent that retrieves and analyzes GitHub repository issues using Retrieval-Augmented Generation (RAG) with vector search capabilities. The application fetches GitHub issues, stores them in a vector database, and provides intelligent responses through a conversational AI agent.

## 🚀 Features

- **GitHub Issues Fetching**: Automatically retrieves issues from specified GitHub repositories
- **Vector Database Storage**: Uses AstraDB for persistent vector storage of issue embeddings
- **Intelligent Search**: Semantic similarity search across GitHub issues
- **AI Agent Interface**: Interactive command-line agent for querying issues
- **Note-Taking Tool**: Built-in tool to save important information to local files
- **Real-time Updates**: Option to refresh issue data from repositories
- **Metadata Preservation**: Maintains issue metadata including author, comments, labels, and timestamps

## 🛠️ Technology Stack

- **Vector Database**: AstraDB Vector Store
- **Embeddings**: Nomic Embed Text (via Ollama)
- **Language Model**: Mistral Small (via MistralAI)
- **Framework**: LangChain with Tool-Calling Agents
- **GitHub API**: REST API integration for issue retrieval
- **Document Processing**: Custom GitHub issue parser

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running locally with required models
3. **GitHub Personal Access Token** for API access
4. **AstraDB Account** with vector database setup
5. **MistralAI API Key** for language model access

Required Ollama models:
```ollama pull nomic-embed-text```

## 🔧 Installation

1. **Clone the repository**:
   ```
    git clone <repository-url>
    cd github-issues-rag-agent
   ```
   
2. **Install required dependencies**:
   ```
   pip install langchain-astradb langchain-ollama langchain-mistralai langchain requests python-dotenv
   ```

3. **Create a `.env` file** with the following variables:
```
GITHUB_TOKEN=your_github_personal_access_token
ASTRA_DB_API_ENDPOINT=your_astradb_api_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_astradb_application_token
ASTRA_DB_KEY=your_astradb_keyspace_name
MISTRAL_API_KEY=your_mistral_api_key
```

## 🚀 Usage

1. **Configure Repository Settings**: 
Edit the `main.py` file to specify your target GitHub repository:
```
owner = "your-github-username"
repo = "your-repository-name"
```

2. **Run the Application**:
   ```
   python main.py
   ```

3. **Update Issues** (when prompted):
- Enter 'y' or 'yes' to fetch latest issues from GitHub
- Enter 'n' or 'no' to use existing cached issues

4. **Start Querying**: 
- Ask questions about GitHub issues in natural language
- Use the built-in note-taking feature to save important information
- Type 'q' to quit the application

## 💡 How It Works

1. **Issue Retrieval**: The `github.py` module fetches issues using GitHub REST API
2. **Data Processing**: Issues are converted to LangChain Document objects with metadata
3. **Vector Storage**: Documents are embedded using Nomic embeddings and stored in AstraDB
4. **Query Processing**: User queries are processed through semantic similarity search
5. **AI Response**: Mistral AI generates intelligent responses using retrieved issue context
6. **Tool Integration**: Agent can use additional tools like note-saving during conversations

## 📁 Project Structure
```
github-issues-rag-agent/
├── main.py # Main application and agent setup
├── github.py # GitHub API integration and issue fetching
├── note.py # Note-taking tool implementation
├── .env # Environment variables (create this)
├── notes.txt # Generated notes file
└── README.md # This file
```


## 🔍 Key Components

### GitHub Integration (`github.py`)
- `fetch_github_details()`: Generic GitHub API fetcher
- `load_doc()`: Converts GitHub issues to LangChain documents
- `fetch_github_issues()`: Main function to retrieve repository issues

### Agent System (`main.py`)
- `connect_to_vstore()`: Establishes AstraDB connection
- Retriever tool for semantic search
- Tool-calling agent with conversation capabilities

### Note-Taking Tool (`note.py`)
- `save_note()`: LangChain tool for saving notes to local file

## ⚙️ Configuration

### GitHub API Settings
- Requires personal access token with appropriate repository permissions
- API rate limits apply (5000 requests/hour for authenticated requests)

### Vector Database Settings
- Uses AstraDB for scalable vector storage
- Configurable collection name (`github`)
- Supports namespace isolation

### AI Model Settings
- Mistral Small model for balanced performance and cost
- Temperature set to 0.1 for consistent, factual responses
- Retrieval configured for top-3 similar issues

## 🛡️ Security & Privacy

- **API Token Security**: Store tokens securely in `.env` file
- **Data Persistence**: Issues stored in cloud vector database
- **Rate Limiting**: Respects GitHub API rate limits
- **Metadata Handling**: Preserves issue metadata for context

## 🔧 Troubleshooting

**Common Issues:**

1. **GitHub API Authentication**: Verify token has correct permissions
2. **AstraDB Connection**: Check endpoint and token configuration
3. **Ollama Models**: Ensure nomic-embed-text model is downloaded
4. **Rate Limits**: GitHub API has request limits - avoid frequent updates
5. **MistralAI API**: Verify API key and account credits

## 🤖 Available Tools

The agent has access to the following tools:

- **github_search**: Search through GitHub issues using semantic similarity
- **save_note**: Save important information to a local notes file

## 🚀 Example Queries

- "What are the most common bugs reported?"
- "Show me issues related to authentication"
- "Find issues created by specific user"
- "What feature requests are pending?"

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new GitHub data sources (PRs, commits, etc.)
- Implementing additional tools for the agent
- Improving query processing and response quality
- Adding support for multiple repositories

**Note**: This application requires valid API keys for GitHub, AstraDB, and MistralAI services. Ensure all credentials are properly configured in the `.env` file.
