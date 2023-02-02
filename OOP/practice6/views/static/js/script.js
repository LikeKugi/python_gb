const newWorker = document.querySelector('#btnForm');

const getWorkers = document.querySelector('#getWorkers');

newWorker.addEventListener('click', async function () {
    const nameValue = document.querySelector("#name")
    val = nameValue.value;
    await fetch("/api/new_worker", {
        method: "POST",
        body: JSON.stringify({
            title: "name",
            value: val,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
})

getWorkers.addEventListener('click', async function () {

    const response = await fetch('/api/workers');
    console.log(response);
    const jsoned = await response.json();

    const workers = jsoned['data']
    const lists = document.querySelector('#workers');

    console.log(typeof workers);
    for (const worker of workers) {
        console.log(worker)
        const elements = []
        for (const key in worker) {
            elements.push(`${key}: ${worker[key]}`)
        }
        lists.innerHTML += `<li>${elements.join(' ')}</li>`
    }

})

const testGetBtn = document.querySelector('#testGet');

testGetBtn.addEventListener('click', async function() {
    const response = await fetch('api/get_worker/2');
    const jsoned = await response.json();
    console.log(jsoned)
    const answer = jsoned['data'];
    for (let key in answer) {
        console.log(`${key}: ${answer[key]}`);
    }
})

const testPutBtn = document.querySelector('#testPut');

testPutBtn.addEventListener('click', async function() {

    const response = await fetch("/api/workers/2", {
        method: "PUT",
        body: JSON.stringify({
            title: "name",
            value: 2,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });

    const jsoned = await response.json();
    console.log(jsoned)
    const answer = jsoned['data'];
    for (let key in answer) {
        console.log(`${key}: ${answer[key]}`);
    }
})

const testDelBtn = document.querySelector('#testDelete');

testDelBtn.addEventListener('click', async function() {

    const response = await fetch("/api/workers/2", {
        method: "DELETE",
        body: JSON.stringify({
            title: "name",
            value: 2,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });

    const jsoned = await response.json();
    console.log(jsoned)
    const answer = jsoned['data'];
    for (let key in answer) {
        console.log(`${key}: ${answer[key]}`);
    }
})