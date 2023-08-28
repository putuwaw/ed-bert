# ed-bert

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![LICENSE](https://img.shields.io/github/license/putuwaw/experimental-connection?style=for-the-badge)
![BUILD](https://img.shields.io/github/actions/workflow/status/putuwaw/ed-bert/lint.yml?style=for-the-badge)

Emotional Detection using Bidirectional Encoder Representations from Transformers (BERT).

## Features 🚀

Using ED-BERT, you can:

- [x] Detect emotion from text.
- [x] Report incorrect prediction and save the data on database.
- [x] Train your own model with additional data from database.

## Prerequisites 📋

- Python 3.10 or higher
- Streamlit 1.25.0 or higher
- MySQL 8.0.32 or higher
- Docker 24.0.4 or higher (optional)
- docker-compose 1.29.2 or higher (optional)

## Installation 🛠

## Manual Installation

- Clone the repository

```bash
git clone https://github.com/putuwaw/ed-bert.git
```

- Create virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```
- Set up database using SQL dump in [init.sql](db/init.sql) file.

- Run the app

```bash
streamlit run Home.py
```

> [!IMPORTANT]  
> This repository contain .h5 file which is the model of ED-BERT. Please consider to read about Git Large File Storage.

## Docker Installation

- Clone the repository

```bash
git clone https://github.com/putuwaw/ed-bert.git
```

- Run the app

```bash
docker-compose up
```

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
