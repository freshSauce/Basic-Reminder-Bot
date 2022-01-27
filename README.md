
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![AGPL 3.0 License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]



<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Basic Reminder Bot</h3>

  <p align="center">
    Have you ever wanted a reminder bot? Look no more! This bot is for you :D
    <br />
    Made with a 100% love.
    <br />
    <br />
    <a href="https://github.com/freshSauce/Basic-Reminder-Bot"><strong>Give the project a star!</strong></a>
    <br />
    <br />
    <a href="https://github.com/freshSauce/Basic-Reminder-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/freshSauce/Basic-Reminder-Bot/issues">Request Feature</a>
  </p>


<!-- ABOUT THE PROJECT -->
## About The Project

Hi there! In Telegram we have a lot of bots, from bots made for moderate groups to bots made to make UNO games. Made as a fun-made

### Main modules
* [Flask](https://palletsprojects.com/p/flask/)
* [requests](https://docs.python-requests.org/en/latest/)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/)



## Bot installation

### Setting up environment variables

In order to run the bot you have to set up the following environment variables:

- API_KEY - The API key provided by the bot father in Telegram
- DB_URI - MongoDB URI to store the reminders (support for SQL databases or CSV storage might be added)


#### Linux
```bash
export API_KEY="YOUR_API_KEY"
export DB_URI="mongodb+srv://YOUR_MONGODB_URI"
```

#### Windows
```bat
set API_KEY="YOUR_API_KEY"
set DB_URI="mongodb+srv://YOUR_MONGODB_URI"
```

### Setting up the webhook

If we want to use our bot we need to set up a webhook, i.e., where we can receive the updates Telegram provides us. To achieve that we can use [ngrok](https://ngrok.io/) to get an HTTP/HTTPS URL or any host like [heroku](https://www.heroku.com).

If we use heroku to host our Flask app it automatically will set up an URL for us, however, if we use ngrok instead to get an URL, we need to make sure that ngrok is running on the same host thar we are running our Flask app.

Once we have our URL and Flask app running, we need to make a request to [setWebhook](https://core.telegram.org/bots/api#setwebhook) Telegram's endpoint.

### Running the bot

You have 3 ways to run the bot:
- Using the flask module
- Running the python file
- Using a WSGI Server (such as Gunicorn)
  
#### Using Flask module

To start the bot using the Flask module you need to set up the "FLASK_APP" environment variable:

##### Linux
```bash
export FLASK_APP="main.py"
```

##### Windows
```bat
set FLASK_APP="main.py"
```

Once you've set your environment variables you can run your bot with:

```bash
python -m flask run
```

#### Running the python file

Starting the bot with this method is the easiest one, simply you need to type:

```bash
python main.py
```

And thats it!

#### Using a WSGI Server

There are multiple WSGI containers to choose from, here we will choose [gunicorn](https://gunicorn.org/) as it is the easiest to set up.

First of all you need to install it via PIP

```bash
pip install gunicorn
```

Once we've done that we can start our Bot by doing
```bash
gunicorn main:app
```

And that's it, we should see our Bot being started :)


### Usage of the bot

The bot is pretty much user-friendly, for now, we only have 2 commands (excluding the /help command):

- /remind - Used to create a reminder in format: /remind in \<number> year(s) \<number> month(s) \<number> day(s) \<number> hour(s) \<number> minute(s). While replying a message. <br><br>Ex: /remind in 3 days<br><br>
- /myreminders - Replies with a list that contains your reminders.

And that's it! you now know how to use the bot:).


### Extra - Setting up bot's language

To set up the bot's language you need to define the environment variable "lang", right now the bot is compatible with english and spanish. To use spanish set the "lang" variable to "es", if this variable isn't provided or any other language is provided the bot will use english on its config.

<!-- CONTRIBUTING -->
## Contributing

Wanna contribute to the project? Great! Please follow the next steps in order to submit any feature or bug-fix :) You can also send me your ideas to my [Telegram](https://t.me/freshSauce), any submit is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the AGPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Telegram: - [@freshSauce](https://t.me/freshSauce)

Project Link: [https://github.com/freshSauce/Basic-Reminder-Bot](https://github.com/freshSauce/Basic-Reminder-Bot)

<!-- CHANGELOG -->

### Changelog

#### 0.1.0
* Code uploaded to Github.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/freshSauce/Basic-Reminder-Bot.svg?style=for-the-badge
[contributors-url]: https://github.com/freshSauce/Basic-Reminder-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/freshSauce/Basic-Reminder-Bot.svg?style=for-the-badge
[forks-url]: https://github.com/freshSauce/Basic-Reminder-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/freshSauce/Basic-Reminder-Bot.svg?style=for-the-badge
[stars-url]: https://github.com/freshSauce/Basic-Reminder-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/freshSauce/Basic-Reminder-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/freshSauce/Basic-Reminder-Bot/issues
[license-shield]: https://img.shields.io/github/license/freshSauce/Basic-Reminder-Bot.svg?style=for-the-badge
[license-url]: https://github.com/freshSauce/Basic-Reminder-Bot/blob/master/LICENSE.txt
[telegram-shield]: https://img.shields.io/badge/-@freshSauce-black?style=for-the-badge&logo=telegram&colorB=0af
[telegram-url]: https://t.me/freshSauce
