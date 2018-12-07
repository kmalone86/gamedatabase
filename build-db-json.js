const fs = require('fs');
const path = require('path');
const jsonfile = require('jsonfile');
const glob = require('glob');
const chalk = require('chalk');

const log = console.log;
const error = chalk.bold.red;
const warning = chalk.bold.yellow;
const success = chalk.green;
const finishSuccess = chalk.bold.bgGreen;
const finishError = chalk.bold.bgRed;

const mkdirSync = function(dirPath) {
    try {
        fs.mkdirSync(dirPath);
    } catch (err) {
        if (err.code !== 'EEXIST') {
            throw err;
        }
    }
};

const buildFolder = async (folderToMatch) => {
    let baseJsonObject = {};

    return await new Promise((resolve, reject) => {
        const fileArray = glob.sync(`${folderToMatch}/*.json`, {
            ignore: ['**/node_modules/**', '**/package.json', '**/package-lock.json'],
        });

        if (!fileArray || (fileArray && !fileArray.length)) {
            log(warning(`χ No JSON files found.`));
            return reject();
        }
        log(
            warning(
                `BUILD: ${
                    fileArray.length
                } JSON files were found in "${folderToMatch}" folder and will be built into a single file "dist/${folderToMatch}.json".`
            )
        );

        baseJsonObject[folderToMatch] = [];

        // https://stackoverflow.com/questions/31413749/node-js-promise-all-and-foreach
        let actions = fileArray.map((filename) => {
            return jsonfile
                .readFile(filename, { throws: false })
                .then((filecontents = null) => {
                    if (filecontents === null) {
                        return Promise.reject(new Error('filecontents null'));
                    }
                    filecontents.fileId = filename.replace(/(.*\/)(.*)(\.json)/i, '$2');
                    baseJsonObject[folderToMatch].push(filecontents);

                    return log(success(`√ JSON "${filename}" processed.`));
                })
                .catch((err = {}) => {
                    switch (err.message) {
                        case 'filecontents null':
                            log(error(`χ JSON "${filename}" is not valid`));
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
                log(
                    finishSuccess(
                        `\n√ All JSON files on "${folderToMatch}" folder were processed. See file at "dist/${folderToMatch}.json"\n`
                    )
                );

                return fs.writeFile(
                    path.resolve('./dist') + `/${folderToMatch}.json`,
                    JSON.stringify(baseJsonObject),
                    (err) => {
                        if (err) {
                            log(error(`χ Error writing to dist/"${filename}".json`, err));
                            return reject();
                        }
                        return resolve();
                    }
                );
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

const buildDb = async () => {
    //make `dist` folder
    mkdirSync(path.resolve('./dist'));

    return Promise.all([
        buildFolder('artifact'),
        buildFolder('buff-debuff'),
        buildFolder('hero'),
        buildFolder('resource'),
    ])
        .then(() => {
            log(
                finishSuccess(
                    `\n√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√\n√ All JSON files of all folders were Built. Congrats!     √\n√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√\n`
                )
            );
            return process.exit(0);
        })
        .catch((e = {}) => {
            console.log(e);
            console.log(e.message);

            log(
                finishError(
                    `\nχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχ\nχ One or more JSONs are not valid.               χ\nχ Please run "npm test" to discover which        χ\nχ JSON file is the culprit, fix and commit it.   χ\nχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχχ\n`
                )
            );
            return process.exit(1);
        });
};

buildDb();
