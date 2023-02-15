# profile

<a href='/README_ZH.md'>中文文档 </a>

This is a opensource project base on openAI_demo(https://github.com/openai/openai-quickstart-python.git). It integer Werbot and flask, It's easy to use If you are in China. Just  you need to get a vpn soft, and install it on your server.

![pic](https://github.com/minLaoGe/ChatGPT-Werobot-Flask/blob/main/pic/1.jpg)
![pic](https://github.com/minLaoGe/ChatGPT-Werobot-Flask/blob/main/pic/2.jpg)

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:3000](http://localhost:3000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
