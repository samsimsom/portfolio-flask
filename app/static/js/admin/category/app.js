console.log("--- Category App ---");

const categoryListElement = document.getElementById("category-list");

async function getCategory() {
  const fetchCategory = await fetch(
    `${window.origin}/admin/category/get_category`
  );

  return fetchCategory;
}

window.addEventListener("load", (event) => {
  getCategory()
    .then((response) => response.json())
    .then((data) => console.log(data));
});




function updateList() {

}