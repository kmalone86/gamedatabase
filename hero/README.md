# Contributing to Heroes

> Heroes are one of the main focus in this game, therefore they have a lot of information. All the information listed here is a mix of info from `Menu > Journal > Hero` and `Menu > Hero`.

> Therefore if you do not own the hero, you might not have all information.

## Important: Do not be afraid of making PR with missing data!

You might not have memory imprint rank SSS, but someone else might have and make a complementary PR to add it.

---

1. Identify a Hero in-game that the json counterpart is missing
    - Or identify a existing one with typo and/or wrong information
2. Create a new json file with the name of the hero
    - Follow the rules stated on `General Contributing Rules` @ repository's root `README.md`
    - If the artifact name contains spaces, replace them for `-` (dashes).
        - E.g.: `Ruele of Light` (5 star Light hero) becomes `ruele-of-light.json`
3. Follow the standard names for the properties, see `ras.json` for example. The idea is to duplicate `ras.json`, change the name to the hero you want to contribute and write on top
4. Create a PR with your changes
5. Thank you for contributing

### Properties

-   `classType`: A hero class can be of the following type:
    -   `knight`
    -   `thief`
    -   `warrior`
    -   `soul-weaver`
    -   `mage`
    -   `ranger`
    -   `material`
-   `element`: A hero element can be of the following type:
    -   `fire`
    -   `earth`
    -   `ice`
    -   `light`
    -   `dark`
    -   `material`
-   `zodiac`: A hero zodiac can be of the following type:
    -   `aries`
    -   `taurus`
    -   `gemini`
    -   `cancer`
    -   `leo`
    -   `virgo`
    -   `libra`
    -   `scorpio`
    -   `sagittarius`
    -   capricorn
    -   `aquarius`
    -   `pisces`
-   `specialtyChangeName`: Leave empty string if hero does not have a specialty change. Otherwise, add the specialty change hero.
    -   E.g.: Hero Lorina will have `"specialtyChangeName":"commander-lorina"`, while Kluri will have `"specialtyChangeName":"falconer-kluri"`
-   `background`: Some heroes might have multi-paragraph backgrounds, therefore, please keep as an array where each paragraph is an array entry.
-   Specialty's `dispatch` and `enhancement`:
-   `relations`: An array of object with the hero and relationType. A hero relationType can be of the following type:
    -   `trust`
    -   `grudge`
    -   `rival`
    -   `longing`
-   Hero stats will be referenced in `stats`, `memoryImprint` and `awakening.statsIncrease`. A hero have the following stats:
    -   `cp` - CP, Character Power
    -   `atk` - Attack
    -   `hp` - Hit Points, Health
    -   `spd` - Speed
    -   `chc` - Critical Hit Chance
    -   `chd` - Critical Hit Damage
    -   `eff` - Effectiveness
    -   `eff` - Effectiveness
    -   `afr` - Effect Resistance
    -   `dac` - Dual Attack Chance
-   `skills`:
    -   `awakenUpgrade` true when the skill is upgraded on awakening #3
    -   `buffs` and `debuffs`. An array of possible buffs and debuffs applied by each skill. Please refer to `src/buff-debuff` folder to write them.
        -   E.g.: Ras' S3 has `"buffs": ["stic_def_up"]`
-   `specialtySkill`'s `dispatch` and `enhancement`: Currently there are no multi-dispatch or multi-enhancement skills, but supposing it might exist in the future, please keep as an array.
-   `memoryImprint`'s `increase`, as well as : If the increase is a flat number, put as _Integer_. If the increase is percentage, put as _String_.
    -   E.g.: Health+300 = `"type":"hp","increase":300`, Attack+2.4% = `"type":"atk","increase":"2.4%"
-   `awakening`'s `statsIncrease`: Same kind of memoryImpring:
    -   E.g.: `"statsIncrease": [{ "efr": "6%" }, { "atk": 30 }, { "hp": 80 }],`.
