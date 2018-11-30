const path = require('path');
const jsonfile = require('jsonfile');
const glob = require('glob');
const chalk = require('chalk');
const validationRules = require('./_validator/validationRules');

const log = console.log;
const error = chalk.bold.red;
const warning = chalk.bold.yellow;
const success = chalk.green;
const finishSuccess = chalk.bold.bgGreen;
const finishError = chalk.bold.bgRed;

const validateFolder = async (folderToMatch) => {
    return await new Promise((resolve, reject) => {
        const requiredProperties = validationRules[folderToMatch];
        const fileArray = glob.sync(`${folderToMatch}/*.json`, {
            ignore: ['**/node_modules/**', '**/package.json', '**/package-lock.json'],
        });

        if (!fileArray || (fileArray && !fileArray.length)) {
            log(warning(`χ No JSON files found.`));
            return reject();
        }
        log(
            warning(
                `VALIDATOR: ${
                    fileArray.length
                } JSON files were found in "${folderToMatch}" folder and will be validated.`
            )
        );

        // https://stackoverflow.com/questions/31413749/node-js-promise-all-and-foreach
        let actions = fileArray.map((filename) => {
            return jsonfile
                .readFile(filename, { throws: false })
                .then((filecontents = null) => {
                    if (filecontents === null) {
                        return Promise.reject(new Error('filecontents null'));
                    }

                    // TODO: WRITE TEST FOR INNER PROPS, NOT ONLY ROOT ONES
                    if (
                        requiredProperties.every((prop) => {
                            let propTest = prop in filecontents;

                            if (!propTest) {
                                log(error(`χ JSON "${filename}" does not containt required property "${prop}"!!`));
                            }
                            return propTest;
                        })
                    ) {
                        return log(success(`√ JSON "${filename}" is valid.`));
                    }
                    return Promise.reject(new Error('missing props'));
                })
                .catch((err = {}) => {
                    switch (err.message) {
                        case 'filecontents null':
                            log(error(`χ JSON "${filename}" is not valid`));
                            break;
                        case 'missing props':
                            log(
                                error(
                                    `χ JSON ${filename} is missing one or more of the required properties.\nConfirm that the file contains all the following properties:\n    - ${requiredProperties.join(
                                        `\n    - `
                                    )}`
                                )
                            );
                            break;

                        default:
                            log(error(`χ An error happened. Please see the following error stack:\,${e.message}`));
                            break;
                    }
                    reject();
                });
        });

        return Promise.all(actions)
            .then(() => {
                log(finishSuccess(`\n√ All JSON files on "${folderToMatch}" folder were validated.\n`));
                return resolve();
            })
            .catch((e) => {
                log(
                    finishError(
                        `\nχ One or more JSONs on "${folderToMatch}" folder are not valid. Please fix above file errors and commit the changes.\n`
                    )
                );
                return reject();
            });
    });
};

const validate = async () => {
    return Promise.all([
        validateFolder('artifact'),
        validateFolder('buff-debuff'),
        validateFolder('hero'),
        validateFolder('resource'),
    ])
        .then(() => {
            log(
                finishSuccess(
                    `\n√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√\n√ All JSON files of all folders were validated. Congrats! √\n√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√\n`
                )
            );
            return process.exit(0);
        })
        .catch((e = {}) => {
            log(
                finishError(
                    `\nχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχ\nχ One or more JSONs are not valid.               χ\nχ Please fix above files and commit the changes. χ\nχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχ\n`
                )
            );
            return process.exit(1);
        });
};

validate();
