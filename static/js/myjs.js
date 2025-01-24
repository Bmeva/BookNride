


$(document).ready(function () { //This function is used to close the alert button on the base.html
    $('.alert .close').on('click', function () {
        $(this).closest('.alert').addClass('fade-out');

        setTimeout(function () {
            $(this).closest('.alert').remove();
        }.bind(this), 2000);
    });
});





document.addEventListener("DOMContentLoaded", function () {
    const profileInput = document.querySelector("input[name='profile_picture']"); //profile_picture is gotten from theprofileupdate.profile_picture
    const profilePreview = document.getElementById("profilePreview"); 

    profileInput.addEventListener("change", function (event) {
        const file = event.target.files[0]; // Get the selected file
        if (file) {
            const reader = new FileReader(); // Create a FileReader instance

            // When the file is loaded, update the image src
            reader.onload = function (e) {
                profilePreview.src = e.target.result;
            };

            reader.readAsDataURL(file); // Read the file as a data URL
        }
    });
});

document.addEventListener('DOMContentLoaded', function () { //I used this on the customer registration page to dispaly various forms
    var showForm1Button = document.getElementById('showForm1');
    var showForm2Button = document.getElementById('showForm2');
    var showForm3Button = document.getElementById('showForm3');
    var form1 = document.getElementById('form1');
    var form2 = document.getElementById('form2');
    var form3 = document.getElementById('form3');

    showForm1Button.addEventListener('click', function () {
        form1.style.display = 'block';
        //document.getElementById('contentText').textContent = 'You clicked the Customer button.'; I can also use this to change the Title text but i used the jQuery code below
        form2.style.display = 'none';
        form3.style.display = 'none';
    });

    showForm2Button.addEventListener('click', function () {
        form2.style.display = 'block';
        //document.getElementById('contentText').textContent = 'You clicked the Vendor button.'; I can also use this to change the Title text but i used the jQuery code below
        form1.style.display = 'none';
        form3.style.display = 'none';

    });
    showForm3Button.addEventListener('click', function () {
        form3.style.display = 'block';
        //document.getElementById('contentText').textContent = 'You clicked the Driver button.'; I can also use this to change the Title text but i used the jQuery code below
        form1.style.display = 'none';
        form2.style.display = 'none';

    });


});

//this is jQuery code to change the title on the vendor registration page
$(document).ready(function () {
    $('#showForm1').click(function () {
        $('#contentText').text('You clicked the Customer reg button.');
    });

    $('#showForm2').click(function () {
        $('#contentText').text('You clicked the Vendor reg button.');
    });

    $('#showForm3').click(function () {
        $('#contentText').text('You clicked the Driver reg button.');
    });
});



// Chart 1
var ctx1 = document.getElementById('myChart1').getContext('2d');
new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    }
});

// Chart 2
var ctx2 = document.getElementById('myChart2').getContext('2d');
new Chart(ctx2, {
    type: 'polarArea',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 15, 5, 7, 12, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.3)',
                'rgba(75, 192, 192, 0.3)',
                'rgba(153, 102, 255, 0.3)',
                'rgba(255, 159, 64, 0.3)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    }
});

// Chart 3
var ctx3 = document.getElementById('myChart3').getContext('2d');
new Chart(ctx3, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 15, 5, 7, 12, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.3)',
                'rgba(75, 192, 192, 0.3)',
                'rgba(153, 102, 255, 0.3)',
                'rgba(255, 159, 64, 0.3)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    }
});


