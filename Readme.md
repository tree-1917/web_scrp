# 🕸️ Web Scraping Project: Job Listings

This project is a Python script that scrapes job listings from the Wuzzuf website, specifically targeting jobs related to Python. The script extracts relevant job details such as the job title, company name, location, skills required, and job links. The scraped data is then saved into a CSV file for further analysis or use.

## ✨ Features

- **Web Scraping**: Automatically fetches job listings from the Wuzzuf website using Python and the `BeautifulSoup` library.
- **Data Extraction**: Extracts key information including job titles, company names, locations, skills required, and job links.
- **CSV Export**: The scraped data is neatly organized and exported to a CSV file (`job.csv`) for easy access and further processing.
- **Error Handling**: Robust error handling ensures that the script continues running even if some elements are missing or if there are connection issues.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed along with the necessary libraries. You can install the required libraries using `pip`:

```bash
pip install requests lxml beautifulsoup4
```

### Running the Script

1. **Clone This Repository**:
   ```bash
   git clone https://github.com/your-username/web-scraping-job-listings.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd web-scraping-job-listings
   ```
3. **Activate Virtual Environment** (optional but recommended):
   ```bash
   source venv/bin/activate
   ```
4. **Run the Script**:
   ```bash
   python main.py
   ```

The script will scrape the job listings from the **Wuzzuf** website and save the extracted data into `job.csv`.

## 🔧 How It Works

1. **Fetching the Web Page**: The script uses the `requests` library to fetch the HTML content of the **Wuzzuf** search results page.
2. **Parsing the Content**: The `BeautifulSoup` library is used to parse the HTML content and extract the relevant job details.
3. **Data Extraction**: Job titles, company names, locations, skills, and job links are extracted using specific HTML tags and class names.
4. **Storing the Data**: The extracted data is saved into a CSV file using the `csv` library for further use.

## 📄 File Structure

- `main.py`: The main script that performs the web scraping and data extraction.
- `job.csv`: The output CSV file where the scraped job data is saved.
- `jo_ds.csv`: A backup or alternative CSV file (optional).
- `venv/`: Virtual environment directory (optional).
- `README.md`: This file, providing information about the project.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request if you have any improvements or additional features to add.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out via email at [gamalmo1917@gmail.com](mailto:gamalmo1917@gmail.com).

---

Happy scraping! 🕷️
