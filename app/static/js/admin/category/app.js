console.log("--- Category App ---");

const form = document.getElementById("category-form");
const categoryList = document.getElementById("category-list");

async function formPost() {
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

  // console.log(data);

  return data;
}

async function getCategories() {
  const url = `${window.origin}/admin/category/get_category`;
  const options = { method: "GET" };
  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
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
  const data = await responce.json();

  return data;
}

function updateCategoryListUI(data) {
  categoryList.innerHTML = "";
  const reversed = data.reverse();
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
    categoryList.innerHTML += categoryHTML;
  });
}

function clearForm() {
  form.reset();
}

form.addEventListener("submit", (e) => {
  e.preventDefault();

  async function glue() {
    const a = await formPost();
    const b = await getCategories();

    // console.log(a);

    return { a, b };
  }

  glue()
    .then((data) => console.log(data))
    .catch((err) => console.log(err));

  clearForm();
});

categoryList.addEventListener("mouseup", (e) => {
  if (e.target.classList.contains("edit")) {
    console.log(e.target.id);
  }

  if (e.target.classList.contains("delete")) {
    deleteCategory(e.target.id)
      .then((data) => console.log(data))
      .catch((err) => console.log(err));
  }
});

window.addEventListener("load", () => {
  getCategories()
    .then((data) => updateCategoryListUI(data))
    .catch((err) => console.log(err));
});
