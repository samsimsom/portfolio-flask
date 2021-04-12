console.log("--- Category App - 2 ---");

let editIsActivated
let addIsActivated

// DOM Elements
const form = document.getElementById("add-category-form")
const categoryList = document.getElementById("category-list");
const popupAlertDiv = document.getElementById("popup-alert");
const submitBtn = document.getElementById("add-category-btn");
const submitBtnContainer = document.getElementById("btn-container");

// Event Listeners
window.addEventListener("load", WindowLoad);
function WindowLoad(e) {
  // Fetch all categories from db
  getCategory()
    .then((data) => categoriesListUI(data))
    .catch((err) => console.log(err));
}

form.addEventListener("submit", addFormSubmit)
function addFormSubmit(e) {
  e.preventDefault();

  addNewCategory()
    .then((data) => {
      if (data.Err) {
        return popupAlert(data.Err.name, "danger");
      }
      if (data.Success) {
        clearForm();
        return getCategory(data.Success);
      }
    })
    .then((data) => {
      if (data) {
        addNewCategoryToUI(data);
      }
    })
    .catch((err) => console.error(err));
}


categoryList.addEventListener("click", editDeleteEvent);
function editDeleteEvent(e) {
  // EDIT
  if (e.target.classList.contains("edit")) {
    console.log('EDIT!')
  }

  // DELETE
  if (e.target.classList.contains("delete")) {
    deleteCategory(e.target.id)
      .then((data) => {
        if (data.Err) {
          popupAlert(data.Err, "danger");
        } else {
          removeCategoryElement(data);
        }
      })
      .catch((err) => console.log(err));
  }
}


// Backand Communications
async function addNewCategory() {
  let entry = {
    name: form.name.value.trim(),
    description: form.description.value.trim(),
  };

  const url = `${window.origin}/admin/category/add_category`;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": form.csrf_token.value,
    },
    body: JSON.stringify(entry),
  };

  const responce = await fetch(url, options);
  if (!responce.ok) {
    throw new Error("NOT 2XX RESPONSE");
  } else {
    const data = await responce.json();
    return data;
  }
}

async function getCategory(id) {
  let url = ``;
  if (id) {
    url = `${window.origin}/admin/category/get_category/${id}`;
  } else {
    url = `${window.origin}/admin/category/get_category`;
  }
  const options = { method: "GET" };

  const responce = await fetch(url, options);
  if (!responce.ok) {
    throw new Error("NOT 2XX RESPONSE");
  } else {
    const data = await responce.json();
    return data;
  }
}

async function deleteCategory(id) {
  const url = `${window.origin}/admin/category/delete_category/${id}`;
  const options = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": form.csrf_token.value,
    },
  };

  const responce = await fetch(url, options);
  if (!responce.ok) {
    throw new Error("NOT 2XX RESPONSE");
  } else {
    const data = await responce.json();
    return data;
  }
}

/*
async function editCategory(id) {
  const url = `${window.origin}/admin/category/edit_category/${id}`;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": form.csrf_token.value,
    },
  };

  const responce = await fetch(url, options);
  if (!responce.ok) {
    throw new Error("NOT 2XX RESPONSE");
  } else {
    const data = await responce.json();
    return data;
  }
}
*/

// UI Generators and Update
function categoryHtmlGenerator(category) {
  const html = `
  <tr id="${category._id.$oid}">
  <td>${category._id.$oid}</td>
  <td>${category.name}</td>
  <td>${category.description}</td>
  <td>${category.slug}</td>
  <td>
  <div class="btn-group" role="group">
    <button type="button" class="btn btn-success edit" id="${category._id.$oid}">Edit</button>
    <button type="button" class="btn btn-danger delete" id="${category._id.$oid}">Delete</button>
  </div>
  </td>
  </tr>
`;
  return html;
}

function addNewCategoryToUI(category) {
  const html = categoryHtmlGenerator(category);
  categoryList.insertAdjacentHTML("afterbegin", html);
}

function categoriesListUI(categories) {
  categories.forEach((category) => {
    const html = categoryHtmlGenerator(category);
    categoryList.insertAdjacentHTML("afterbegin", html);
  });
}

function removeCategoryElement(category) {
  let removed = document.getElementById(category.id);
  removed.remove();
}

function popupAlert(err, style) {
  popupAlertDiv.innerHTML = "";
  const html = `
  <div class="alert alert-${style} alert-dismissible fade show" role="alert">
  ${err}
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  `;
  popupAlertDiv.insertAdjacentHTML("afterbegin", html);

  setTimeout(() => {
    popupAlertDiv.innerHTML = "";
  }, 3000);
}

function clearForm() {
  form.reset();
}