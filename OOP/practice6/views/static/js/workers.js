window.addEventListener('DOMContentLoaded', async function() {
    const response = await fetch('/api/workers');
    const jsoned = await response.json();
    const workers = jsoned['data'];
    const template = document.querySelector('#employeeCard');
    const employeesList = document.querySelector('.employee');

    for (const worker of workers) {
        const clone = template.content.cloneNode(true);
        let emp_name = clone.querySelector('.name');
        emp_name.textContent = worker['name'];
        let emp_lastname = clone.querySelector('.lastname');
        emp_lastname.textContent = worker['lastname'];
        let emp_passport = clone.querySelector('.passport');
        emp_passport.textContent = worker['passport'];
        let emp_phone = clone.querySelector('.phone');
        emp_phone.textContent = worker['phone'];
        let emp_salary = clone.querySelector('.salary');
        emp_salary.textContent = worker['salary'];
        let emp_cabinet = clone.querySelector('.cabinet');
        emp_cabinet.textContent = worker['cabinet'];
        let emp_id = clone.querySelector('.hiddenID');
        emp_id.value = worker['id'];
        let emp_edit = clone.querySelector('.edit');
        emp_edit.setAttribute('href', `/edit.html/${worker['id']}`);

        employeesList.append(clone);
    }
})