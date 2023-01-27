const logBtn = document.querySelector("#login");

const toExport = document.querySelector('#export');
const toAdd = document.querySelector('#add_student');
const toAddTeacher = document.querySelector('#add_teacher');
const lessonName = document.querySelector('#lesson_name')
const toDel = document.querySelector('#del_student');
const targetDel = document.querySelector('#delete');

logBtn.addEventListener('click', permission);
toDel.addEventListener('click', function () {
    targetDel.disabled = !toDel.checked;
})
toAdd.addEventListener('click', disableDeleter);
toAdd.addEventListener('click', disableLesson);
toExport.addEventListener('click', disableDeleter);
toExport.addEventListener('click', disableLesson);

function permission(e) {
    switch (+logBtn.value) {
        case 0:
        case 1:
        case 3:
            toAdd.disabled = true;
            toDel.disabled = true;
            disableDeleter();
            disableTeacher();
            break;
        case 2:
            toAdd.disabled = false;
            toDel.disabled = false;
            enableTeacher();
    }
}

function disableDeleter() {
    targetDel.disabled = true;
    targetDel.value = -1;
}

function disableTeacher() {
    toAddTeacher.disabled = true;
    disableLesson();
}
function enableTeacher() {
    toAddTeacher.disabled = false;
    lessonName.disabled = false;
}
function disableLesson() {
    lessonName.value = '';
    lessonName.disabled = true;
}