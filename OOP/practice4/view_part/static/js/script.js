const loginBtn = document.querySelector("#login");
const contentList = document.querySelector("#content")

loginBtn.addEventListener("click", fname);

loginBtn.addEventListener("click", changeStateNext);

const users = {
    current: 0,
    0:'Admin',
    1:'Teacher',
    2:'Student',
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

function fname() {
    console.log('works');
    contentList.innerHTML += '<li>works</li>';
}

function changeStateNext(e) {
    if (e.ctrlKey) {
        loginBtn.textContent = users[users.currentPrev()];
    } else {

        loginBtn.textContent = users[users.currentNext()];
    }

}