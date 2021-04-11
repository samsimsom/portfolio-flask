console.log("--- Category App - 2 ---");

// DOM Elements
const form = document.getElementById("category-form");
const categoryList = document.getElementById("category-list");
const popupAlert = document.getElementById("popup-alert");

// First Load Event
window.addEventListener("load", WindowLoad);
function WindowLoad() {
  getCategory()
    .then((data) => CategoriesListUI(data))
    .catch((err) => console.log(err));
}

form.addEventListener("submit", formSubmit);
function formSubmit(e) {
  e.preventDefault();

  addNewCategory()
    .then((data) => {
      if (data.Err) {
        return PopupAlert(data.Err.name, "danger");
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

categoryList.addEventListener("click", EditDeleteEvent);
function EditDeleteEvent(e) {
  if (e.target.classList.contains("edit")) {
    console.log(e.target.id);
  }

  if (e.target.classList.contains("delete")) {
    deleteCategory(e.target.id)
      .then((data) => {
        if (data.Err) {
          PopupAlert(data.Err, "danger");
        } else {
          RemoveCategoryElement(data);
        }
      })
      .catch((err) => console.log(err));
  }
}

// Backand Communications
async function addNewCategory() {
  let entry = {
    name: form.name.value,
    description: form.description.value,
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

async function editCategory(id) {
  
}

// UI Generators and Update
function CategoryHtmlGenerator(category) {
  const html = `
  <tr id="${category._id.$oid}">
  <td>${category._id.$oid}</td>
  <td>${category.name}</td>
  <td>${category.description.slice(0, 6)}</td>
  <td>${category.slug}</td>
  <td>
  <div class="btn-group" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-success edit" id="${
      category._id.$oid
    }">Edit</button>
    <button type="button" class="btn btn-danger delete" id="${
      category._id.$oid
    }">Delete</button>
  </div>
  </td>
  </tr>
`;
  return html;
}

function addNewCategoryToUI(category) {
  const html = CategoryHtmlGenerator(category);
  categoryList.insertAdjacentHTML("afterbegin", html);
}

function CategoriesListUI(categories) {
  categories.forEach((category) => {
    const html = CategoryHtmlGenerator(category);
    categoryList.insertAdjacentHTML("afterbegin", html);
  });
}

function RemoveCategoryElement(category) {
  let removed = document.getElementById(category.id);
  removed.remove();
}

function PopupAlert(err, style) {
  popupAlert.innerHTML = "";
  const html = `
  <div class="alert alert-${style} alert-dismissible fade show" role="alert">
  ${err}
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  `;
  popupAlert.insertAdjacentHTML("afterbegin", html);

  setTimeout(() => {
    popupAlert.innerHTML = "";
  }, 3000);
}

function clearForm() {
  form.reset();
}
