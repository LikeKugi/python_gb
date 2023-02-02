const btnAdd = document.querySelector('#btnAdd');

const nameValue = document.querySelector('#name');
const lastNameValue = document.querySelector('#last_name');
const passportValue = document.querySelector('#passport');
const phoneValue = document.querySelector('#phone');
const salaryValue = document.querySelector('#salary');
const cabinetValue = document.querySelector('#cabinet');

const resultBox = document.querySelector('#result');
const resultTitle = document.querySelector('#resultTitle');
const resultText = document.querySelector('#resultText');
const resultClose = document.querySelector('#close');

btnAdd.addEventListener('click', async function() {

    const response = await fetch("/api/new_worker", {
        method: "POST",
        body: JSON.stringify({
            title: 'new worker',
            name: nameValue.value,
            lastName: lastNameValue.value,
            passport: passportValue.value,
            phone: phoneValue.value,
            salary: salaryValue.value,
            cabinet: cabinetValue.value,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });

    const result = await response;
    if (result['status'] ===200) {
        console.log('done');
        resultTitle.textContent = 'Выполнено';
        resultText.textContent = 'Работник добавлен';
    } else {
        resultTitle.textContent = 'Ошибка';
        resultText.textContent = result['error'];
    }
    clearField();
    resultBox.classList.remove('hidden');
    setTimeout(() => {
        resultBox.classList.add('hidden')
    }, 5000);
})

resultClose.addEventListener('click', function() {
    resultBox.classList.add('hidden');
})

function clearField() {
    nameValue.value = '';
    lastNameValue.value = '';
    passportValue.value = '';
    phoneValue.value = '';
    salaryValue.value = '';
    cabinetValue.value = '';
}