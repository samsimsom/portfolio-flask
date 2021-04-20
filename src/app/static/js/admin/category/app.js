'use strict'
console.log('--- Category App ---')
/*

        PROTOTYPE - 4-12-2021
        BY - mft

*/


// DOM Elements
let tr
const form = document.getElementById('add-category-form')
const categoryList = document.getElementById('category-list')
const popupAlertDiv = document.getElementById('popup-alert')
const submitBtn = document.getElementById('add-category-btn')
const submitBtnContainer = document.getElementById('btn-container')

// Event Listeners
window.addEventListener('load', WindowLoad)
function WindowLoad(e) {
  // Fetch all categories from db
  getCategory()
    .then((data) => categoriesListUI(data))
    .catch((err) => console.log(err))
}

form.addEventListener('submit', addFormSubmit)
function addFormSubmit(e) {
  e.preventDefault()

  addNewCategory()
    .then((data) => {
      if (data.Err) {
        return popupAlert(data.Err.name, 'danger')
      }
      if (data.Success) {
        clearForm()
        return getCategory(data.Success)
      }
    })
    .then((data) => {
      if (data) {
        addNewCategoryToUI(data)
      }
    })
    .catch((err) => console.error(err))
}

categoryList.addEventListener('click', editDeleteEvent)
function editDeleteEvent(e) {
  // EDIT
  if (e.target.classList.contains('edit')) {
    let id = e.target.id.split('-')[0]
    let trTableId = `${id}-category-table-tr`
    getCategory(id).then((data) => {
      tr = document.getElementById(trTableId)
      tr.innerHTML = ''
      tr.insertAdjacentHTML('afterbegin', editFormGenerator(data))
    })
  }

  // DELETE
  if (e.target.classList.contains('delete')) {
    let id = e.target.id.split('-')[0]
    deleteCategory(id)
      .then((data) => {
        if (data.Err) {
          popupAlert(data.Err, 'danger')
        } else {
          removeCategoryElement(data)
        }
      })
      .catch((err) => console.log(err))
  }

  // CANCEL
  if (e.target.classList.contains('cancel')) {
    let id = e.target.id.split('-')[0]
    let trTableId = `${id}-category-table-tr`
    tr = document.getElementById(trTableId)
    if (id === tr.id.split('-')[0]) {
      getCategory(id).then((data) => {
        tr.innerHTML = ''
        tr.insertAdjacentHTML('afterbegin', categoryHtmlGenerator(data))
      })
    }
  }

  // SUBMIT
  if (e.target.classList.contains('submit')) {
    e.preventDefault()
    let id = e.target.id.split('-')[0]
    let trTableId = `${id}-category-table-tr`
    tr = document.getElementById(trTableId)
    if (id === tr.id.split('-')[0]) {
      editCategory(id).then((data) => {
        if (data.Err) {
          return popupAlert(data.Err, 'danger')
        }
        getCategory(id).then((data) => {
          tr.innerHTML = ''
          tr.insertAdjacentHTML('afterbegin', categoryHtmlGenerator(data))
        })
      })
    }
  }
}

// Backand Communications
async function addNewCategory() {
  let entry = {
    name: form.name.value.trim(),
    description: form.description.value.trim(),
  }

  const url = `${window.origin}/admin/category/add_category`
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': form.csrf_token.value,
    },
    body: JSON.stringify(entry),
  }

  const responce = await fetch(url, options)
  if (!responce.ok) {
    throw new Error('NOT 2XX RESPONSE')
  } else {
    const data = await responce.json()
    return data
  }
}

async function getCategory(id) {
  let url = ``
  if (id) {
    url = `${window.origin}/admin/category/get_category/${id}`
  } else {
    url = `${window.origin}/admin/category/get_category`
  }
  const options = { method: 'GET' }

  const responce = await fetch(url, options)
  if (!responce.ok) {
    throw new Error('NOT 2XX RESPONSE')
  } else {
    const data = await responce.json()
    return data
  }
}

async function deleteCategory(id) {
  const url = `${window.origin}/admin/category/delete_category/${id}`
  const options = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': form.csrf_token.value,
    },
  }

  const responce = await fetch(url, options)
  if (!responce.ok) {
    throw new Error('NOT 2XX RESPONSE')
  } else {
    const data = await responce.json()
    return data
  }
}

async function editCategory(id) {
  let entry = {
    name: document.getElementById(`${id}-name-input`).value.trim(),
    slug: document.getElementById(`${id}-slug-input`).value.trim(),
    description: document.getElementById(`${id}-description-input`)
      .value.trim(),
  }

  const url = `${window.origin}/admin/category/edit_category/${id}`
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': form.csrf_token.value,
    },
    body: JSON.stringify(entry),
  }

  const responce = await fetch(url, options)
  if (!responce.ok) {
    throw new Error('NOT 2XX RESPONSE')
  } else {
    const data = await responce.json()
    return data
  }
}

// UI Generators and Update
function editFormGenerator(category) {
  const html = `
    <td colspan="5">
    <div class="shadow p-3 bg-body rounded">
    <form id="${category._id.$oid}-edit-form">
    <!-- Flex Row -->
    <div class="d-flex flex-row align-items-center">
      <div class="p-1 h6">Edit Category</div>
    </div>
    <!-- Flex Row -->
    <div class="d-flex flex-row align-items-center">
      <div class="p-1 w-25">Name : </div>
      <div class="p-1 flex-fill">
        <input type="text" class="form-control form-control-sm" value="${category.name}" id="${category._id.$oid}-name-input" required>
      </div>
    </div>
    <!-- Flex Row -->
    <div class="d-flex flex-row align-items-center">
      <div class="p-1 w-25">Slug : </div>
      <div class="p-1 flex-fill">
        <input type="text" class="form-control form-control-sm" value="${category.slug}" id="${category._id.$oid}-slug-input" required>
      </div>
    </div>
    <!-- Flex Row -->
    <div class="bd-highlight">
      <div class="d-flex flex-row align-items-center">
        <div class="p-1 w-25">Description : </div>
        <div class="p-1 flex-fill">
          <input type="text" class="form-control form-control-sm" value="${category.description}" id="${category._id.$oid}-description-input">
        </div>
      </div>
    </div>
    <!-- Flex Row -->
    <div class="d-flex flex-row align-items-center">
      <div class="p-1">
      <button type="button" id="${category._id.$oid}-edit-form-cancel-btn" class="btn btn-info btn-sm cancel">Cancel</button>
      </div>
      <div class="p-1">
      <button type="submit" id="${category._id.$oid}-edit-submit-btn" class="btn btn-primary btn-sm submit">Submit</button>
      </div>
    </div>
    <!-- Flex Row -->
    </form>
    </div>
    </td>
  `
  return html
}

function categoryHtmlGenerator(category) {
  const html = `
  <tr id="${category._id.$oid}-category-table-tr">
  <td>${category.name}</td>
  <td>${category.description}</td>
  <td>${category.slug}</td>
  <td>
  <div class="btn-group" role="group">
    <button type="button" class="btn btn-success edit" id="${category._id.$oid}-category-edit-btn">Edit</button>
    <button type="button" class="btn btn-danger delete" id="${category._id.$oid}-category-delete-btn">Delete</button>
  </div>
  </td>
  </tr>
`
  return html
}

function addNewCategoryToUI(category) {
  const html = categoryHtmlGenerator(category)
  categoryList.insertAdjacentHTML('afterbegin', html)
}

function categoriesListUI(categories) {
  categories.forEach((category) => {
    const html = categoryHtmlGenerator(category)
    categoryList.insertAdjacentHTML('afterbegin', html)
  })
}

function removeCategoryElement(category) {
  let id = `${category.id.split('-')[0]}-category-table-tr`
  let removed = document.getElementById(id)
  removed.remove()
}

function popupAlert(err, style) {
  popupAlertDiv.innerHTML = ''
  const html = `
  <div class="alert alert-${style} alert-dismissible fade show" role="alert">
  ${err}
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  `
  popupAlertDiv.insertAdjacentHTML('afterbegin', html)

  setTimeout(() => {
    popupAlertDiv.innerHTML = ''
  }, 3000)
}

function clearForm() {
  form.reset()
}
