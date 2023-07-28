import {CG_EP} from "./api_route.js";
// -------------------------------------------------------------------------------

// loader that shows a process is happening
var loader = document.getElementById("faculty-loader");

// alerts
var add_success_alert = document.getElementById("faculty-added-success");
var add_failure_alert = document.getElementById("faculty-added-danger");
var delete_success_alert = document.getElementById("faculty-deleted-success");
var delete_failure_alert = document.getElementById("faculty-deleted-danger");
var edit_success_alert = document.getElementById("faculty-updated-success");
var edit_failure_alert = document.getElementById("faculty-updated-danger");

// modals
var addFacultyModalClose = document.getElementById('addFacultyModalCloseBtn')
var editFacultyModalOpen = document.getElementById('editFacultyModalOpenBtn')
var editFacultyModalClose = document.getElementById('editFacultyModalCloseBtn')

// -------------------------------------------------------------------------------

// Functon to Add new faculty to database
const addFacultyDetail = () => {

    // get values from the field
    const title = document.getElementById('faculty-title').value.trim();
    const fname = document.getElementById('faculty-first-name').value.trim();
    const lname = document.getElementById('faculty-last-name').value.trim();
    const contact = document.getElementById('faculty-contact').value.trim();
    const cabin = document.getElementById('faculty-cabin').value.trim();
    const email = document.getElementById('faculty-email').value.trim();
    const department = document.getElementById('faculty-department').value.trim();
    const designation = document.getElementById('faculty-designation').value.trim();

    if (fname == '' || lname == '' || contact == '' || cabin == '' || email == '') {
        alert("Please submit all the details first before pressing the save button.");

        return;
    }

    // close the model
    addFacultyModalClose.click();

    // make the loader visible
    loader.hidden = false;

    // let's fill those detail into an object
    const faculty = {
        "title": title,
        "first_name": fname,
        "last_name": lname,
        "contact": contact,
        "email": email,
        "cabin": cabin,
        "department": department,
        "designation": designation
    };

    // console.log(faculty);

    // create xhr object and send request
    let xhr = new XMLHttpRequest();
    xhr.open('POST', CG_EP);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.addEventListener('load', () => {
        // hide the loader
        loader.hidden = true;

        // read the response
        let response = JSON.parse(xhr.responseText);

        console.log(response.result)

        if (response.result) {
            add_failure_alert.hidden = true;
            add_success_alert.hidden = false;
            delete_success_alert.hidden = true;
            delete_failure_alert.hidden = true;
            edit_success_alert.hidden = true;
            edit_failure_alert.hidden = true;
        } else {
            add_failure_alert.hidden = false;
            add_success_alert.hidden = true;
            delete_success_alert.hidden = true;
            delete_failure_alert.hidden = true;
            edit_success_alert.hidden = true;
            edit_failure_alert.hidden = true;
        }
    })
    xhr.send(JSON.stringify(faculty));

};

// Function to Delete a faculty from database
const deleteFacultyDetail = (event) => {
    const sure = confirm("Are you sure you want to delete this detail? Remember once deleted, you cannot recover the detail?")

    if (!sure) {
        return;
    } else {

        // make the loader visible
        loader.hidden = false;

        // now fetch the required details
        let target_id = event.target.parentNode.id;

        const fname = document.getElementById("first-name-" + target_id).innerHTML.trim();
        const contact = document.getElementById("contact-" + target_id).innerHTML.trim();

        // fill these details in an object
        const faculty = {
            "title": '',
            "first_name": fname,
            "last_name": '',
            "contact": contact,
            "email": '',
            "cabin": '',
            "department": '',
            "designation": ''
        }

        let xhr = new XMLHttpRequest();
        xhr.open('DELETE', CG_EP);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.addEventListener('load', () => {
            // hide the loader
            loader.hidden = true;

            // read the response
            let response = JSON.parse(xhr.responseText);

            // console.log(response.result)

            if (response.result) {
                add_failure_alert.hidden = true;
                add_success_alert.hidden = true;
                delete_success_alert.hidden = false;
                delete_failure_alert.hidden = true;
                edit_success_alert.hidden = true;
                edit_failure_alert.hidden = true;
            } else {
                add_failure_alert.hidden = true;
                add_success_alert.hidden = true;
                delete_success_alert.hidden = true;
                delete_failure_alert.hidden = false;
                edit_success_alert.hidden = true;
                edit_failure_alert.hidden = true;
            }
        })

        xhr.send(JSON.stringify(faculty));
    }
};

// Function to feed the details in the edit modal and display the modal

const showEditFacultyDetailModal = (event) => {
    // locate the tagert and fetch old details
    let target_id = event.target.parentNode.id;

    const title = document.getElementById("title-" + target_id).innerHTML.trim();
    const fname = document.getElementById("first-name-" + target_id).innerHTML.trim();
    const lname = document.getElementById("last-name-" + target_id).innerHTML.trim();
    const contact = document.getElementById("contact-" + target_id).innerHTML.trim();
    const email = document.getElementById("email-" + target_id).innerHTML.trim();
    const department = document.getElementById("department-" + target_id).innerHTML.trim();
    const designation = document.getElementById("designation-" + target_id).innerHTML.trim();
    const cabin = document.getElementById("cabin-" + target_id).innerHTML.trim();

    // fill these details in an object that represents initial values
    const oldFaculty = {
        "title": title,
        "first_name": fname,
        "last_name": lname,
        "contact": contact,
        "email": email,
        "cabin": cabin,
        "department": department,
        "designation": designation
    }

    // fill these details in the modal
    document.getElementById('faculty-title-edit').value = title;
    document.getElementById('faculty-first-name-edit').value = fname;
    document.getElementById('faculty-last-name-edit').value = lname;
    document.getElementById('faculty-contact-edit').value = contact;
    document.getElementById('faculty-cabin-edit').value = cabin;
    document.getElementById('faculty-email-edit').value = email;
    document.getElementById('faculty-department-edit').value = department;
    document.getElementById('faculty-designation-edit').value = designation;

    // make the modal visible
    editFacultyModalOpen.click();

    // map the submit btn with the edit function
    document.getElementById('edit-faculty-btn').addEventListener('click', editFacultyDetail(oldFaculty));
}

// Function to update details to the data base
var editFacultyDetail = (oldFaculty) => {

    // now using the `closure` feature to utilise the old object value
    return () => {
        // fetch the new details
        const title = document.getElementById("faculty-title-edit").value.trim();
        const fname = document.getElementById("faculty-first-name-edit").value.trim();
        const lname = document.getElementById("faculty-last-name-edit").value.trim();
        const contact = document.getElementById("faculty-contact-edit").value.trim();
        const email = document.getElementById("faculty-email-edit").value.trim();
        const department = document.getElementById("faculty-department-edit").value.trim();
        const designation = document.getElementById("faculty-designation-edit").value.trim();
        const cabin = document.getElementById("faculty-cabin-edit").value.trim();

        // store the new details in objects

        const newFaculty = {
            "title": title,
            "first_name": fname,
            "last_name": lname,
            "contact": contact,
            "email": email,
            "cabin": cabin,
            "department": department,
            "designation": designation
        }
        // fill these details in an object according to the API documentation

        const faculty = {
            "old_faculty_detail": oldFaculty,
            "new_faculty_detail": newFaculty
        }

        console.log(faculty);

        // hide the modal and clear all the content in it
        editFacultyModalClose.click();

        // make the loader visible
        loader.hidden = false;

        // make xhr object and send request

        let xhr = new XMLHttpRequest();
        xhr.open('PUT', CG_EP);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.addEventListener('load', () => {
            // hide the loader
            loader.hidden = true;

            // read the response
            let response = JSON.parse(xhr.responseText);

            console.log(response.result)

            if (response.result) {
                add_failure_alert.hidden = true;
                add_success_alert.hidden = true;
                delete_success_alert.hidden = false;
                delete_failure_alert.hidden = true;
                edit_success_alert.hidden = true;
                edit_failure_alert.hidden = true;
            } else {
                add_failure_alert.hidden = true;
                add_success_alert.hidden = true;
                delete_success_alert.hidden = true;
                delete_failure_alert.hidden = false;
                edit_success_alert.hidden = true;
                edit_failure_alert.hidden = true;
            }
        })

        xhr.send(JSON.stringify(faculty));
    }
}

// -------------------------------------------------------------------------------

// mapping functions with buttons
document.getElementById('add-faculty-btn').addEventListener('click', addFacultyDetail);

let deleteBtns = document.getElementsByClassName("delete-faculty-button");
for (let i = 0; i < deleteBtns.length; i++)
    deleteBtns[i].addEventListener("click", deleteFacultyDetail);

let editBtns = document.getElementsByClassName("edit-faculty-button");
for (let i = 0; i < editBtns.length; i++)
    editBtns[i].addEventListener("click", showEditFacultyDetailModal);

// -------------------------------------------------------------------------------

