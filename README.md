# ag

Implement the `ag` command to call the `DeepSeek:v3` model in the command line.

## The effect is as follows

![intro](https://github.com/user-attachments/assets/fe004408-bfc6-4983-9339-a7ead9a2e081)

## how to install in your Linux

### Prerequisites

- Python 3.10.12
- pip 25.0.1

### Dependencies to install

- openai

```shell
pip install openai
```

For domestic installation, you can use mirror installation, the command is as follows：

```shell
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- load-dotenv

```shell
pip install load-dotenv
```

### Clone this repo to local

- clone repo

```shell
git clone https://github.com/shenjy712/ag.git
```

- `.env` file

```
API_KEY=
API_BASE_URI=https://api.siliconflow.cn
MODEL=deepseek-ai/DeepSeek-V3
```

> The large model API used above is the API of Silicon Flow. You can also use the API of Silicon Flow, [Register Silicon Flow](https://cloud.siliconflow.cn/i/BLu934tI)

- generate API KEY
  ![1740459963892](https://github.com/user-attachments/assets/c2556ff3-4c75-47ea-b735-a6b0368c6da5)

- After generating the API key, fill in the API key after `API_KEY=` in the `.env` file
- execute following command

```shell
# Add executable permissions
chmod +x ag.py

# Copy the command to the /usr/local/bin directory and change the name to ag
mv ag.py /usr/local/bin/ag

# Move the .env file to the same directory
mv .env /usr/local/bin/

# or use this command line
chmod +x ag.py && sudo mv ag.py /usr/local/bin/ag && sudo mv .env /usr/local/bin/
```

- Now you can use the `ag` command in the command line to call the `DeepSeek:v3` model.

over~
