const loginBtn = document.querySelector("#login");
const saveBtn = document.querySelectorAll('.save-btn');

const gradesInp = document.querySelectorAll('.grade');
const namesInp = document.querySelectorAll('.sname');
const tested = document.querySelector('#test-info')

loginBtn.addEventListener("click", changeStateNext);

const users = {
    current: 3,
    0:'Student',
    1:'Teacher',
    2:'Admin',
    3:'Login',
    currentNext() {
        this.current = (this.current + 1) % 4;
        return this.current;
    },
    currentPrev() {
        this.current = Math.abs(this.current - 1) % 4;
        return this.current;
    },
};

function changeStateNext(e) {
    if (e.ctrlKey) {
        loginBtn.textContent = users[users.currentPrev()];
        permissions();
    } else {
        loginBtn.textContent = users[users.currentNext()];
        permissions();
    }
}

function permissions() {
    switch (users.current) {
        case 0:
        case 3:
            namesInp.forEach( element => element.disabled = true);
            gradesInp.forEach( element => element.disabled = true);
            saveBtn.forEach( element => element.disabled = true);
            console.log(users.current)
            break;
        case 1:
            namesInp.forEach( element => element.disabled = true);
            gradesInp.forEach( element => element.disabled = false);
            saveBtn.forEach( element => element.disabled = false);
            console.log(users.current)
            break
        case 2:
            namesInp.forEach( element => element.disabled = false);
            gradesInp.forEach( element => element.disabled = false);
            saveBtn.forEach( element => element.disabled = false);
            console.log(users.current)
            break
    }
}