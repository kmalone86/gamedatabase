const jsonfile = require('jsonfile');
const glob = require('glob');
const chalk = require('chalk');
const log = console.log;
const error = chalk.bold.red;
const warning = chalk.bold.yellow;
const success = chalk.green;
const finishSuccess = chalk.bgGreen;
const finishError = chalk.bgRed;

const validate = async () => {
    glob('**/*.json', { ignore: ['**/node_modules/**', '**/package.json', '**/package-lock.json'] }, function(
        err,
        fileArray
    ) {
        if (err) {
            log(error(err));
            process.exit(1);
        }
        if (!fileArray || (fileArray && !fileArray.length)) {
            log(warning(`χ No JSON files found.`));
            return process.exit(1);
        }
        log(warning(`VALIDATOR: ${fileArray.length} JSON files were found and will be validated.`));

        // https://stackoverflow.com/questions/31413749/node-js-promise-all-and-foreach
        let actions = fileArray.map(filename => {
            return jsonfile
                .readFile(filename, { throws: false })
                .then(filecontents => {
                    if (filecontents === null) {
                        return Promise.reject(new Error('filecontents null = not valid'));
                    }
                    return log(success(`√ JSON ${filename} is valid.`));
                })
                .catch(err => {
                    throw log(error(`χ JSON ${filename} is not valid.`));
                });
        });

        Promise.all(actions)
            .then(data => {
                log(finishSuccess(`√ All JSON validated. Congrats!`));
                return process.exit(0);
            })
            .catch(e => {
                log(finishError(`χ One or more JSONs are not valid. Please fix above files and commit the changes.`));
                return process.exit(1);
            });
    });
};
validate();
