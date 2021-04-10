console.log("--- Category App ---");

// UI Elements
const form = document.getElementById("category-form");
const categoryList = document.getElementById("category-list");

const updateUI = (data) => {
  data.forEach((category, index) => {
    const categoryHTML = `
    <tr>
    <th scope="row">${index}</th>
    <td>${category._id.$oid.slice(0, 6)}</td>
    <td>${category.name}</td>
    <td>${category.description}</td>
    <td>${category.slug}</td>
    <td>
    <div class="btn-group" role="group" aria-label="Basic example">
      <button type="button" class="btn btn-success">Edit</button>
      <button type="button" class="btn btn-danger">Delete</button>
    </div>
    </td>
    </tr>
  `;
    categoryList.innerHTML += categoryHTML;
  });
};

const getCategories = async () => {
  const url = `${window.origin}/admin/category/get_category`;
  const options = { method: "GET" };
  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
};

const formSubmit = async (entry, csrf_token) => {
  const url = `${window.origin}/admin/category/add_category`;
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrf_token,
    },
    body: JSON.stringify(entry),
  };
  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
};

const clearFrom = () => {
  form.reset();
};

// Event Listeners
window.addEventListener("load", () => {
  getCategories()
    .then((data) => updateUI(data))
    .catch((err) => console.log(err));
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let entry = {
    name: form.name.value,
    description: form.description.value,
  };
  let csrf_token = form.csrf_token.value;

  formSubmit(entry, csrf_token)
    .then((data) => console.log(data))
    .catch((err) => console.log(err));

  clearFrom();
});
