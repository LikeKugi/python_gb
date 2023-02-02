window.addEventListener('DOMContentLoaded', async function () {

    const btnAdd = document.querySelector('#btnAdd');
    const btnRes = document.querySelector('#btnRes');
    const btnDel = document.querySelector('#btnDel');

    const empID = document.querySelector('#emp_id');

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

    await defValues();

    async function makeResponse() {
        const response = await fetch(`/api/get_worker/${empID.value}`);
        const jsoned = await response.json();
        return jsoned['data']
    }

    async function defValues() {
        const worker = await makeResponse();
        nameValue.value = worker['name'];
        lastNameValue.value = worker['lastname'];
        passportValue.value = worker['passport'];
        phoneValue.value = worker['phone'];
        salaryValue.value = worker['salary'];
        cabinetValue.value = worker['cabinet'];
    }

    function clearField() {
        empID.value = '';
        nameValue.value = '';
        lastNameValue.value = '';
        passportValue.value = '';
        phoneValue.value = '';
        salaryValue.value = '';
        cabinetValue.value = '';
    }

    function showResult() {
        resultBox.classList.remove('hidden');
        setTimeout(() => {
            resultBox.classList.add('hidden')
        }, 5000);
    }

    btnRes.addEventListener('click', defValues);

    btnAdd.addEventListener('click', async function () {
        console.log('empID = ' + empID.value)
        const putting = await fetch(`/api/update_worker/${empID.value}`, {
            method: "PUT",
            body: JSON.stringify({
                title: 'update worker',
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
        const result = await putting;
        console.log(result)
        if (result['status'] === 200) {
            console.log('done');
            resultTitle.textContent = 'Выполнено';
            resultText.textContent = 'Информация обновлена';
        } else {
            resultTitle.textContent = 'Ошибка';
            resultText.textContent = result['error'];
        }
        await defValues();
        showResult();
    })

    btnDel.addEventListener('click', async function() {
        const response = await fetch(`/api/delete_worker/${empID.value}`, {
            method: "delete"
        });
        const result = await response;
        if (result['status'] === 200) {
            console.log('done');
            resultTitle.textContent = 'Выполнено';
            resultText.textContent = 'Информация обновлена';
            clearField();
        } else {
            resultTitle.textContent = 'Ошибка';
            resultText.textContent = result['error'];
            await defValues();
        }
        showResult();
    });

    resultClose.addEventListener('click', function() {
        resultBox.classList.add('hidden');
    })

})

