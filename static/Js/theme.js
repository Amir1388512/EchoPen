import { $, _class, _id } from './base.js';

// variables
let btn = _id('change-theme-btn');
let icon = btn.firstChild;

window.addEventListener('load', function () {
    let local = localStorage.getItem('Theme');
    if (local === 'light') {
        $.body.classList.replace('dark', 'light');
        $.documentElement.style.setProperty('--txt-color', '#373737');
        icon.classList.replace('bi-brightness-high', 'bi-moon');
    } else {
        $.body.classList.replace('light', 'dark');
        $.documentElement.style.setProperty('--txt-color', '#c0c0c0');
        icon.classList.replace('bi-moon', 'bi-brightness-high');
    }
});

btn.addEventListener('click', function () {
    let local = localStorage.getItem('Theme');
    if (local === 'light') {
        $.body.classList.replace('light', 'dark');
        $.documentElement.style.setProperty('--txt-color', '#c0c0c0');
        localStorage.setItem('Theme', 'dark');
        icon.classList.replace('bi-moon', 'bi-brightness-high');
    } else {
        $.body.classList.replace('dark', 'light');
        localStorage.setItem('Theme', 'light');
        $.documentElement.style.setProperty('--txt-color', '#373737');
        icon.classList.replace('bi-brightness-high', 'bi-moon');
    }
});
