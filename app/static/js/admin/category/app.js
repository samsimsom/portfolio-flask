console.log("--- Category App ---");

const categoryListElement = document.getElementById("category-list");

const getCategories = async () => {
  const url = `${window.origin}/admin/category/get_category`;
  const options = {method: "GET",};
  const responce = await fetch(url, options);
  const data = await responce.json();

  return data;
};

const grabCategoryData = () => {
  getCategories()
    .then((data) => updateUI(data))
    .catch((err) => console.log(err));
};

const updateUI = (data) => {
  data.forEach((category, index) => {
    const categoryHTML = `
    <tr>
    <th scope="row">${index}</th>
    <td>${(category._id.$oid).slice(0, 6)}</td>
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
    categoryListElement.innerHTML += categoryHTML;
  });

  // console.log(data);
};

window.addEventListener("load", grabCategoryData);
