# ag

自己实现命令 `ag` 在命令行中调用 `DeepSeek:v3` 大模型。

## 效果如下

![intro](https://github.com/user-attachments/assets/fe004408-bfc6-4983-9339-a7ead9a2e081)

## 如何在你的电脑安装

### 系统中要提前安装的软件

- Python 3.10.12
- pip 25.0.1

### 要安装的软件包

- openai

```shell
pip install openai
```

国内安装可以使用镜像安装，命令如下：

```shell
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- load-dotenv

```shell
pip install load-dotenv
```

### 克隆本项目到本地

- 克隆本项目

```shell
git clone https://github.com/shenjy712/ag.git
```

- 将本项目可控下来后，主要看 `.env` 这个文件

```
API_KEY=
API_BASE_URI=https://api.siliconflow.cn
MODEL=deepseek-ai/DeepSeek-V3
```

> 上面用到的大模型 API 是硅基流动的 API。大家也可以使用 硅基流动的 API，[注册硅基流动](https://cloud.siliconflow.cn/i/BLu934tI)

- 生成 API 密钥
  ![1740459963892](https://github.com/user-attachments/assets/c2556ff3-4c75-47ea-b735-a6b0368c6da5)

- 生成 API 密钥之后，将 API 密钥填入 `.env` 文件中的 `API_KEY=` 后面
- 执行下面命令

```shell
# 添加可执权限
chmod +x ag.py

# 将命令拷贝到 /usr/local/bin 目录下, 并将名字改成 ag
mv ag.py /usr/local/bin/ag

# 把 .env 文件也移动到同样的目录
mv .env /usr/local/bin/

# 或者用下面的命令
chmod +x ag.py && sudo mv ag.py /usr/local/bin/ag && sudo mv .env /usr/local/bin/
```

- 到现在，大家就可以在命令行中使用 `ag` 命令调用 `DeepSeek:v3` 模型了。

完~
