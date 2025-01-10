# Overview
Test ini dibuat untuk keperluan proses rekrutmen sekaligus demonstrasi mengenai kemampuan untuk automation test dengan best-practices. Perlu diketahui bahwa terdapat *test case* pada folder *indonesia indicator (parent indicator sebelum ini)*. Test script menggunakan framework *pytest* untuk eksekusi script dan *allure* untuk reporting test case. 

# How to use
Clone repository
```bash
$ git clone https://github.com/MRX760/QA-practice.git
$ cd QA-practice/Indonesia_indicator/Python
```

Install poetry for package and env management
```bash
$ pip install poetry
$ poetry install 
```

Activate environment
```bash
$ poetry shell
```

Running test (after activating environment)
```bash
$ pytest tests/test_cases/home_page_ui --alluredir='report'
```

Viewing test report
```bash
$ allure serve report
```

# Test report docs screenshot
![test report screenshot](https://github.com/MRX760/QA-practice/blob/main/Indonesia_indicator/Python/assets/allure_report1.png)
