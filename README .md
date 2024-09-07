# COVID-19 Data Scraper with Python

# Acknowledgments
We would like to extend our gratitude to the following individuals and organizations who have contributed to this project:

- **JetBrains** 
  - We would like to express our sincere appreciation to JetBrains for providing us with PyCharm. This powerful Integrated Development Environment (IDE) has been instrumental in enhancing our Python development workflow, making our coding experience more efficient and enjoyable.

- **Lena Morozova**
  - We would like to thank Lena Morozova for her interest and suggestions regarding the project. Due to my own oversight, I had not added a README file to my open-source project. Thank you for your reminder; it was a great suggestion. Fortunately, it's not too late, and I have now added it.

## Project Description

This project aims to automatically scrape COVID-19 related data using Python and store it in a structured format (such as JSON). The collected data can be used for further data analysis, visualization, and other purposes. The project utilizes the `requests` library to send HTTP requests, the `BeautifulSoup` library to parse HTML documents, and the `pandas` library to handle data.

## Features

- **Data Scraping**: Fetch the latest COVID-19 data from specified websites.
- **Data Cleaning**: Clean the scraped data by removing invalid or unnecessary information.
- **Data Storage**: Save the cleaned data as JSON files or other formats.
- **Data Display**: Display the scraped data through a simple command-line interface.

## Technology Stack

- Python 3.7+
- requests (for sending HTTP requests)
- BeautifulSoup (for parsing HTML)
- pandas (for data handling)

## Installation

### Environment Setup

Ensure that Python 3.7 or higher is installed on your system. You can verify this by running the following command:

```bash
python --version
```

### Dependency Installation

Install the project dependencies by running the following command:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage Guide

### Running the Project

Clone this repository locally:

```bash
git clone git@github.com:byuan98/covid-19_data_crawler_BC.git

cd covid-19_data_crawler_BC/boot
```

Run the main script:

```bash
python main.py
```

## Contribution Guidelines

If you encounter any issues or have suggestions for improvements, please contribute through GitHub Issues or Pull Requests.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Contact Information

For any questions or suggestions, please contact:

- GitHub: [ZhangBoyuan](https://github.com/byuan98)
- Email: byuan98@outlook.com