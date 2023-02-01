const btnAdd = document.querySelector('#btnAdd');

btnAdd.addEventListener('click', async function() {
    const nameValue = document.querySelector('#name');
    const lastNameValue = document.querySelector('#last_name');
    const passportValue = document.querySelector('#passport');
    const phoneValue = document.querySelector('#phone');
    const salaryValue = document.querySelector('#salary');
    const cabinetValue = document.querySelector('#cabinet');

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
    console.log(await response);
})