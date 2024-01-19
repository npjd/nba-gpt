# 🤖 NBA GPT 🏀

An open-source and minimal replica of [StatMuse](https://www.statmuse.com/) — use natural language to query basketball stats

![demo of nba gpt](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWU5Z3MwamZ0aGQ0ZGRsbnNqcWFxMng1Zm5mNm5wdWo5NHFxNGFpbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ik7cWpfj6hYDckgP5c/giphy.gif)


## Features

- [x] Natural language querying of SQL DB
- [x] Extendible to any other sports databse
- [x] Returns media from internet based on query
- [ ] Have most up to date data continously flowing — (currently goes up to only January 1st 2024 to 1997)
- [ ] Integration with other sports databases for cross-sport analysis
- [ ] Advanced search filters for more specific queries
- [ ] Adding play-by-play data
- [ ] Introducing some sort of auto-correct for player names

## Setup

### Prerequisites

- Docker v20>=
- Docker Compose v2>=
- OpenAI API Key
- Serper API Key

### Installation

1.  Clone the repo `git clone https://github.com/npjd/nba-gpt`
2.  Create a `.env` file with the following config

```dosini
OPENAI_API_KEY="<insert api key>"
DATABASE_URI="postgresql://nba_sql:nba_sql@localhost:5432/nba"
SERPER_API_KEY="<insert api key>"
```

3.  Run `docker-compose up`
4.  Visit http://localhost:8501/ once build is finished

## Usage

Simply enter your prompt in the streamlit app and get your response — keep in mind player names must be spelt correctly

## Contributing

We welcome contributions from the community! If you'd like to contribute to NBA GPT, please follow these guidelines:

1.  Fork the repository and clone it locally.
2.  Create a new branch for your contribution: `git checkout -b feature/new-feature`.
3.  Make your changes and test thoroughly.
4.  Commit your changes: `git commit -m "Add new feature"`.
5.  Push to the branch: `git push origin feature/new-feature`.
6.  Open a pull request with a clear title and description.
7.  Please make sure your code adheres to the existing coding standards and practices.

Thank you for helping to improve NBA GPT!

## License

NBA GPT is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
