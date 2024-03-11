// this file is for my homepage
let DataText = document.getElementsByClassName('data-num');

for (let index = 0; index < DataText.length; index++) {
    const element = DataText[index];
    let targetValue = Number(element.getAttribute('data-num'));
    let currentValue = 0;

    // Define a function to update the value
    function updateValue() {
        element.innerHTML = currentValue;
        currentValue++;
        if (currentValue <= targetValue) {
            setTimeout(updateValue, 5);
        }
    }

    // Start the update process
    updateValue();
}


