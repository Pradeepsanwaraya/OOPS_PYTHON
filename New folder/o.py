/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let result = [];
        let count = 0;

        if (functions.length === 0) {
            resolve(result);
            return;
        }

        functions.forEach((fn, i) => {
            fn().then(value => {
                result[i] = value;
                count++;

                if (count === functions.length) {
                    resolve(result);
                }
            }).catch(error => {
                reject(error);
            });
        });
    });
};