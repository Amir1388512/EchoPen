// this file is used in all of my js files
const $ = document;

function _class(className) {
    return $.getElementsByClassName(className);
}

function _id(id) {
    return $.getElementById(id);
}

export { $, _class, _id };
