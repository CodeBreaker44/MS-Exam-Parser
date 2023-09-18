# MS-Exam-Parser
This Python script, "ExamTopics Parser," is designed to help you quickly find and access exam-related questions and topics using Google search. You can specify the exam series code, exam number, and topic number to narrow down your search. Additionally, you can specify a range of questions to explore.

## Prerequisites
* Before you can use this script, you need to ensure that Python is installed in your machine.
* Dependencies: Install the required dependencies by running the following command within the project directory:

  ```shell
  pip install -r requirements.txt
  ```

## Getting Started

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the script.

3. Run the script using the following command:
   ```shell
    python examtopics_parser.py
   ```
4. Follow the on-screen prompts to input the exam series code, exam number, topic number, and the range of questions you want to explore.
5. The script will perform Google searches for the specified queries and open the search results in your default web browser.

## Usage

* Exam Series Code: Enter the code for the exam series you're interested in (e.g., AZ, SC, etc.).

* Exam Number: Enter the specific exam number (e.g., 200, 300, 400, 500, etc.).

* Topic Number: Enter the topic number you want to search for.

* Range of Questions: Define the range of questions you want to explore by specifying the starting and ending question numbers.

## Customization
You can customize the script by modifying the user_agents list to specify different user-agent strings for web requests. This can help you simulate different web browsers or devices.

## Notes

* The script uses the BeautifulSoup library to parse HTML content, requests to send HTTP requests, and webbrowser to open search results in your default web browser.

* Please be aware that web scraping may be subject to the terms of service of the websites you visit, and excessive or automated scraping may violate those terms. Use this script responsibly and ensure compliance with any applicable terms and conditions.

* This script provides a basic example of web scraping for educational purposes. Depending on your use case, you may need to add error handling, logging, or other enhancements for robustness and reliability.

## Disclaimer
This script is provided for educational and informational purposes only. The authors and contributors are not responsible for any misuse or violation of terms of service resulting from the use of this script.

## Demo
![image](https://github.com/CodeBreaker44/MS-Exam-Parser/assets/89404773/9abb383f-edc5-4bb8-9221-659a4dfecd00)

