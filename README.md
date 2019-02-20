# EpicSevenDB.com - Game Database [![Build Status](https://travis-ci.com/EpicSevenDB/gamedatabase.svg?branch=master)](https://travis-ci.com/EpicSevenDB/gamedatabase)

License: `Attribution-NonCommercial-ShareAlike 4.0 International`

EpicSevenDB.com community database for game information, such as Heroes, Artifacts, Gear, Skills and anything else necessary to feed the DB

> Feel free to open an Issue if you see something wrong or some data/property is missing. Better yet if you make a Pull Request with the fixes :-)

## READ THIS BEFORE CONTRIBUTING

Please check if the new hero you intend to contribute isn't already being worked (or was already worked) by someone here: https://github.com/EpicSevenDB/gamedatabase/wiki/List-of-Heroes-currently-being-worked-on

Thank you.


## Changelog

Please see [CHANGELOG.md](https://github.com/EpicSevenDB/gamedatabase/blob/master/CHANGELOG.md) for latest merged changes.

## General Contributing Rules

Whenever referring to another hero, another resource, always write them with the following rules:

-   Always lowercase
-   If name contains spaces, replace them for `-` (dash)
    -   E.g.: `Ruele of Light` (5 star Light hero) becomes `ruele-of-light`
-   If name contains `'` (apostrophe) or any other special symbol (that is, not `a-zA-Z0-9`, and not a greek word, see rule below), simply ignore it.
    -   E.g.: `Water's Origin` (4 star artifact) becomes `waters-origin`.
-   If name contains greek special symbol (that is, `β`), write it's greek name ([reference letter->name](https://en.wikipedia.org/wiki/Greek_alphabet#Sound_values)). Some other games have items of same name with different greek letter so let's prepare for that.
    -   E.g.: `Abyss Guide β` (Item that gives entries to Abyss dungeon) becomes `abyss-guide-beta`.

---

## Contributing to Buff & Debuffs

Please read `src/buff-debuff/README.md` before contributing

---

## Contributing to Artifacts

Please read `src/artifact/README.md` before contributing

---

## Contributing to Heroes

Please read `src/hero/README.md` before contributing

---

Thank you for contributing.

# Testing your changes before committing:

1. Run `npm install` to install dependencies
2. Run `npm test` and check if all JSONs are valid:
    - Success: you'll get a `All JSON validated. Congrats!` if everything is fine.
    - Error: You'll get a `JSON {nameofjson} is not valid.` and validation will halt with `One or more JSONs are not valid. Please fix above files and commit the changes.`
