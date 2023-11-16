// function to make tasks as completed
var markCompletedLinks = document.querySelectorAll('.mark-completed-link');

markCompletedLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(); 
        var taskId = link.getAttribute('data-task-id');
        markCompleted(taskId);
    });
});
function markCompleted(taskId) {
    var statusTask = document.getElementById('status-' + taskId)
    statusTask.textContent = 'COMPLETED';
    statusTask.style.backgroundColor = 'green';
}

function openModal() {
    $('#myModal').modal('show');
}