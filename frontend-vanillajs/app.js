const formulario = document.querySelector("#form");
const id = document.querySelector("#exampleInputId");
const username = document.querySelector("#exampleInputUsername");
const email = document.querySelector("#exampleInputEmail1");
const disabled = document.querySelector("#exampleCheck1");
const alert_container = document.querySelector("#alerts");

// base url of the API server
const URL = "http://127.0.0.1:8000"

// post a new user in the userAPI
async function postNewUser(user) {
  options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(user)
  }

  const response = await fetch(URL + "/user", options)
  const json = await response.json()

  if (!response.ok) {
    throw new Error(json.detail)
  }
  return json;

}


formulario.addEventListener("submit", (e) => {
  e.preventDefault();

  const data = {
    id: id.value,
    username: username.value,
    email: email.value,
    disabled: disabled.checked
  }

  postNewUser(data).then((user) => {
    console.log(user);
    addAlert(alert_container, "New user added successfully", "alert-info")
  }).catch(error => {
    console.error(error.message);
    addAlert(alert_container, error.message, "alert-danger")
  })


})

// add a bootstrap alert-dismissible to the specified container
// type = alert-info, alert-danger, alert-warning, etc...
function addAlert(container, message, type = "alert-info") {
  const alert =
    `<div class="alert ${type} alert-dismissible fade show">
      ${message}
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>`
  container.innerHTML += alert;
}