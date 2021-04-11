console.log("--- Category App - 2 ---");

// DOM Elements
const form = document.getElementById("category-form");
const categoryList = document.getElementById("category-list");

// First Load Event
window.addEventListener("load", WindowLoad);
function WindowLoad() {
  getCategories()
    .then((data) => CategoriesListUI(data))
    .catch((err) => console.error(err));
}

form.addEventListener("submit", formSubmit);
function formSubmit(e) {
  e.preventDefault();

  formFetch()
    .then((data) => getCategory(data.Success))
    .then((data) => addNewCategoryToUI(data))
    .catch((err) => console.error(err));
}

// Backand Communications
async function formFetch() {
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
  const data = await responce.json();

  return data;
}

async function getCategories() {
  const url = `${window.origin}/admin/category/get_categories_`;
  const options = { method: "GET" };

  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
}

async function getCategory(id) {
  const url = `${window.origin}/admin/category/get_category/${id}`;
  const options = { method: "GET" };

  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
}

// UI Generators and Update
function CategoryHtmlGenerator(category) {
  const html = `
  <tr>
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
