# NEW! upvent.codes

A website made in laravel used to help upvent in it's goal to spread the word of
free software around the globe. 

## Project organization
* One issue per thing TO-DO
* Add these features in order:
  - Blog
  - E-commerce
  - VPS API
* Milestones for point, minor and major releases
* Reviews of PR's

THERE IS DUMMY CONTENT IN MASTER, IF YOU WISH TO USE THIS AS A FORK FOR
PRODUCTION USE THE `stable` BRANCH INSTEAD.

## Architecture / Stack
* HTML, CSS, JS
* Laravel Based system
* Blade templating system

## Philosophy
* KEEP IT SIMPLE! We are already using two frameworks and one library:
  - Laravel (Framework)
  - TailwindCSS (Framework)
  - Bootstrap Icons (Library)
We do not want this project to contribute to the bloated web. Keep things
simple, secure and easy to maintain.

## Cloning / Contributing

If you wish to contribute to this project here are the steps you need to
follow:

* Clone the project

```sh
git clone https://github.com/UpVent/upvent.codes.git
cd upvent.codes
```

* Install composer + node dependencies

```sh
composer install && npm install && npm run dev
```

* Copy .env file (Make sure to configure it properly yourself, also try to
use one of the supported databases, namely MariaDB, PostgreSQL or SQLite3)

``` sh
cp .env.example .env
```

* Generate app encryption key

```sh
php artisan key:generate
```

* Migrate the database

```sh
php artisan migrate
```

And that's all, enjoy making changes!
