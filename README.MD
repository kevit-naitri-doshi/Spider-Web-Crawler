# Spider Web Crawler Project

This project is a web crawler built from scratch using Python's built-in libraries and packages such as `urllib`, `html.parser`, and `threading`. The crawler is designed to navigate through websites, extract URLs, and save them in text files for further analysis. The project supports multi-threading to speed up the crawling process.

## Project Structure

The project creates a directory named after the project along with two text files:

- `queue.txt`: Contains the list of URLs to be crawled.
- `crawled.txt`: Contains the list of URLs that have already been crawled.

## Features

- Crawls web pages starting from a given URL.
- Extracts and stores URLs found on each page.
- Utilizes multi-threading to enhance crawling speed and efficiency.
- Maintains a queue of URLs to be crawled and a list of already crawled URLs.

## Requirements

- Python 3.x
- No external libraries are required as the project uses built-in Python modules.

## Configuration

You can change the crawler's parameters by modifying the `config.py` file. This file includes settings such as the project name, homepage URL, domain name, and the number of threads to be used.

### config.py

```python
# config.py

PROJECT_NAME = 'myproject'
HOMEPAGE = 'https://example.com'
DOMAIN_NAME = 'example.com'
NUMBER_OF_THREADS = 8
```

## How to Use

1. **Clone the Repository**

   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/kevit-naitri-doshi/Spider-Web-Crawler.git
   ```

2. **Configure the Parameters**

   Open `config.py` and set your desired parameters such as project name, homepage URL, domain name, and the number of threads.

3. **Run the Crawler**

   Run the Python script to start crawling.

   ```bash
   python main.py
   ```

## Code Overview

### spider.py

This file contains the `Spider` class, which is responsible for crawling web pages, extracting URLs, and managing the queue and crawled lists.

#### Methods

- `__init__(self, project_name, base_url, domain_name)`: Initializes the spider with the project name, base URL, and domain name.
- `crawl_page(self, thread_name, page_url)`: Crawls a single page.
- `gather_links(self, page_url)`: Extracts links from the given page URL.
- `add_links_to_queue(self, links)`: Adds extracted links to the queue.
- `update_files(self)`: Updates the `queue.txt` and `crawled.txt` files.

### main.py

This file contains the main script to start the crawling process. It initializes the `Spider` class and starts multiple threads to crawl the web pages concurrently.

#### Functions

- `create_workers()`: Creates worker threads.
- `work()`: The worker function that processes URLs from the queue.
- `create_jobs()`: Creates jobs for the worker threads.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
