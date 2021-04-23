# UpVent Web Source

> Notice: The current GitHub action is broken due to upstream issues, your commits might be displayed as "non passing".  All PR's will be reviewed manually until this is solved or until we change our action.yml file.

## :warning: For development purposes, when this project reaches beta we will "redo" the commited migrations. Please backup your database contents if you are using this project and restore it accordingly

This is the source code for the UpVent's website under `upvent.codes`.

Development occurs on the `master` branch and new branches are only opened when adding critical/unstable features. The main site is published by upvent making a fork of this project and adding some post-update commits in order to make deployment more secure.



**PLEASE CONSIDER THESE THINGS FIRST**

1- Some content is in Spanish(MX), translate it at your own will.

2- There might be dummy content in `master` branch, if you cannot afford to have experimental features in production, please use the `stable` branch instead.

## Architecture / Stack

* Django powered backend
* Jinja2 templating
* HTML + CSS + JS
* Shell scripting for deploying

## Project organization

- One issue per thing to do.
- Milestones for major releases
- All PR's will be manually reviewed

## Philosophies

- **KEEP IT SIMPLE**, we are already using two frameworks and five libraries. As much as these technologies are useful, we don't want to contribute to the bloated web, keep things simple, secure and easy to maintain
  - Frameworks: Django, Bootstrap 5
  - Libraries: `django-admin-honeypot`, `pillow`, `django-ckeditor`, `django-admin-interface` and `bootstrap-icons`
- Very tiny CMS. Not full featured. Not complex.
- Keep it as secure as possible. We use `django-honeypot` to protect our admin url from attackers. Change your real admin url and use the honeypot for common attack patterns.
- Don't break `stable`. All changes must undergo testing or find a way to prevent breakage on the `stable` branch, if breakage is unavoidable, create a decent solution to allow existing stable users to migrate easily.



## Security

For any serious security related issues, please **do not open a public GitHub issue**. 

Instead, email them to [our issues email](mailto:upventmx@gmail.com). We provide a quick response of security reports within 24 hours and should apply patches ASAP (also, feel free to contribute a fix for the issue).

## Contributing 

If you wish to continue please look at our [ISSUES](https://github.com/UpVent/upvent.codes/issues) tab, open a new Issue to request a feature or report a bug.

If this work helped you somehow, please leave us a star :cat: it will mean so much to us :heart:



## Running

If you wish to contribute to this project here are the steps you need to follow:

- Clone the project

  ```bash
  git clone https://github.com/UpVent/upvent.codes.git
  ```

- Create a virtualenv and install dependencies using Pipenv

  ```bash
  # If pipenv is not installed
  pip3 install pipenv
  
  # Install dependencies + spawn a shell
  pipenv install && pipenv shell
  ```

- (If needed) Make migrations & migrate the database

  ```bash
  # If needed
  python manage.py makemigrations
  
  # Migrate to db
  python manage.py migrate
  ```

- Run the project server

  ```bash
  python manage.py runserver
  ```


## Deployment

We won't provide  (for now) instructions on how to deploy to a server, the steps should be the same as a simple django app. However here are a few steps you should follow:

- Change the default admin url, we placed `wp-admin` as a meme to troll wappalizer users. Don't use it in production.
- Change the secret key or generate a new one in a separate file.
- **DON'T** use the sqlite database, use the supported mysql or modify the project to connect to psql.
- Protect your media folder against execution

## License + Credits

### Our Code
The source code is free software distributed under the GNU General Public License, version 2, or, at your option, any later version. (See [LICENSE](https://github.com/UpVent/upvent.codes/blob/master/LICENSE).)

The website contents are creative commons released under CC-BY-ND-3.0-International.


### External Code

#### hcaptcha implementation

The hcaptcha impementation on this app is credited to
(AndrejZbin)[https://github.com/AndrejZbin] who made `django-hcaptcha` 
which we integrated directly in our codebase.

- License: [BSD 3-Clause "New" or "Revised" License](https://github.com/AndrejZbin/django-hcaptcha/blob/master/LICENSE)

#### Basecode help

Thanks to [@corahama](https://github.com/corahama) for helping us jumpstart this project..
