# Overview
Test ini dibuat untuk keperluan proses rekrutmen sekaligus demonstrasi mengenai kemampuan untuk automation test dengan best-practices. Perlu diketahui bahwa terdapat **`test case`** pada folder **`indonesia indicator (parent folder ini)`**. Test script menggunakan framework **`pytest`** untuk eksekusi script dan **`allure`** untuk reporting test case.  Test script ini juga menggunakan **`POM`** (Page Object Model) yang dapat memudahkan maintenance kode ketika terjadi sebuah error. 

# Warning
Terdapat update dalam penggunaan Actionchains di repository ini, ada kemungkinan beberapa test case akan failed karena perubahan struktur POM dan penggunaan actionchains dalam melakukan interaksi web secara otomatis.

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
## overview
![test report screenshot](https://github.com/MRX760/QA-practice/blob/main/Indonesia_indicator/Python/assets/allure_report2.png)

## report screenshot with image documentation
![test report screenshot](https://github.com/MRX760/QA-practice/blob/main/Indonesia_indicator/Python/assets/allure_report1.png)
