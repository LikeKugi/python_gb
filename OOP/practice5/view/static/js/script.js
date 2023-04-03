const outExpression = document.querySelector('#out-expression');
const printExpression = document.querySelector('#expression');
const queryExpression = document.querySelector('#query');

const numbers = document.querySelectorAll('.numbers');
const operators = document.querySelectorAll('.operators');
const submitBtn = document.querySelector('.btn_submit');

numbers.forEach(element => element.addEventListener('click', function () {
    console.log(`text_=_${queryExpression.textContent}`);
    addToQuery(this.value);
}))

operators.forEach(element => element.addEventListener('click', function () {
    if (this.value === 'del') {
        queryExpression.textContent = '0';
    } else {
        operation(this.value);
    }
}))

submitBtn.addEventListener('click',function () {
    document.querySelector('#exp').value = printExpression.textContent + queryExpression.textContent;
    queryExpression.textContent = '0';
    printExpression.textContent = 0;
})

function addToQuery(val) {
    if (val === '.') {
        console.log(queryExpression.textContent)
        if (queryExpression.textContent.includes('.')) {
            return;
        } else {
            queryExpression.textContent += val;
        }
    } else if (queryExpression.textContent === '0') {
        queryExpression.textContent = val;
    } else {
        queryExpression.textContent += val;
    }
}

function operation(val='') {
    printExpression.textContent = queryExpression.textContent + val;
    queryExpression.textContent = 0;
}

const testBtn = document.querySelector('#test');

testBtn.addEventListener('click', async function (){
    const response = await fetch('/test');
    console.log(response);
    const jsoned = await response.json()
    console.log(jsoned)
})
