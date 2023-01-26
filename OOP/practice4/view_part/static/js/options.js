const logBtn = document.querySelector("#login");

const toExport = document.querySelector('#export');
const toAdd = document.querySelector('#add_student');
const toDel = document.querySelector('#del_student');
const targetDel = document.querySelector('#delete');

logBtn.addEventListener('click', permission);
toDel.addEventListener('click', function () {
    targetDel.disabled = !toDel.checked;
})
toAdd.addEventListener('click', disableDeleter);
toExport.addEventListener('click', disableDeleter);

function permission(e) {
    switch (+logBtn.value) {
        case 0:
        case 1:
        case 3:
            toAdd.disabled = true;
            toDel.disabled = true;
            disableDeleter();
            break;
        case 2:
            toAdd.disabled = false;
            toDel.disabled = false;
    }
}

function disableDeleter() {
    targetDel.disabled = true;
    targetDel.value = -1;
}