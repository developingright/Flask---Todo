function deleteTask(taskId){
    fetch('/delete-task',{
        method: 'POST',
        body: JSON.stringify({taskId: taskId})
    }).then((_res) => {
        window.location.href = "/"
    });
}
// var modalbtn = document.querySelector('.modal-btn');
var buttons = document.getElementsByClassName('modal-btn');
var bg = document.querySelector('.modal-bg');
var modalclose = document.querySelector('.modal-close');
modalclose.addEventListener('click',function(){
    bg.classList.remove('bg-active');
});
// console.log(modalbtn);
function val(title,id){
    document.getElementById("name").value = title;
    document.getElementById("myform").action = `/update/${id}`;;
}

for(var i=0; i< buttons.length; i++){
    buttons[i].addEventListener('click',function(){
        bg.classList.add('bg-active');
        // document.getElementById("name").value = `${k}`;
       
    });
}

console.log("asdasd");
