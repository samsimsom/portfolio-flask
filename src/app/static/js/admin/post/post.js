console.log('--- POST ---')

/*----------------------------------------------------------------------------*/
// Global Variables
const newPostForm = document.getElementById('new-post-form')
const publishPostFormButton = document.getElementById('submit')
const savePostFormButton = document.getElementById('save')
const filesFrame = document.getElementById('uploaded-files')

let pageId
let filesData = []
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Dropzone START
Dropzone.options.postDropzoneContainer = {
  paramName: 'file',
  maxFilesize: 5,
  renameFile: (file) => {
    let splitName = file.name.split(/\.(?=[^\.]+$)/)
    let fileName = splitName[0].replace(/[^a-z0-9]/gi, '_').toLowerCase()
    let extension = splitName[1].toLowerCase()
    let fileId = `${Math.random()
      .toString(36)
      .substr(2, 9)}_${new Date().getTime()}`
    let newName = fileId + '_' + fileName
    let secureName = newName + '.' + extension
    return secureName
  },

  init: function () {
    this.on('addedfile', (file) => {
      console.log('Added! ->', file.upload.filename)
    })

    this.on('success', (file) => {
      console.log('Success! ->', file.upload.filename)
      let fileId = { id: file.upload.filename.split(/\_(?=[^\_]+$)/)[0] }
      filesData.push(fileId)
      addImagesToDOM(file.upload.filename)
    })

    // this.on('complete', (file) => {
    //   this.removeFile(file)
    //   console.log('Removed! ->', file.upload.filename)
    // })
  },
}
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Event Listeners START
window.addEventListener('load', (e) => {
  // Generate PageId
  pageId = Math.random().toString(36).substr(2, 9) + '_' + new Date().getTime()
  console.log('Page ID ->', pageId)
})

// newPostForm.addEventListener('submit', (e) => {
//   e.preventDefault()

//   newPost()
//     .then((data) => console.log(data))
//     .catch((err) => console.log(err))
// })

savePostFormButton.addEventListener('click', (e) => {
  e.preventDefault()
  SaveFormInLocalStorage()
  console.log(e.target.id, 'Form Data Saved!')
})

publishPostFormButton.addEventListener('submit', (e) => {
  e.preventDefault()
  console.log(e.target.id, 'Form Data Published!')
})
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Save Form in LocalStorage
function SaveFormInLocalStorage() {
  let fileData = {
    name: 'File Name',
    path: 'File Path',
    weight: 'File Weight',
    is_featured_image: false,
  }

  let formData = {
    title: newPostForm.title.value,
    description: newPostForm.description.value,
    category: newPostForm.categorySelect.value,
    file: [fileData],
  }

  localStorage.setItem(pageId, JSON.stringify(formData))
}
/*----------------------------------------------------------------------------*/

function addImagesToDOM(filename) {
  let id = filename.split(/\_(?=[^\_]+$)/)[0]

  let html = `
    <div class="border rounded p-1" id="${id}_card">
    <div class="d-flex flex-row">
      <div class="d-flex flex-column">
        <div class="p-1 bd-highlight">
          <img src="${window.origin}/static/upload/samsimsom/${filename}"
              class="uploaded-image rounded">
        </div>
      </div>
      <div class="d-flex flex-column flex-fill">

        <div class="input-group input-group-sm p-1">
          <span class="input-group-text" id="#">Name : &ThinSpace;</span>
          <input type="text" class="form-control" id="${id}_name" value="${filename}">
        </div>

        <div class="input-group input-group-sm p-1">
          <span class="input-group-text" id="#">Weight :</span>
          <input type="number" min="0" class="form-control" id="${id}_weight" value="0">
        </div>

        <div class="d-flex flex-column">
          <div class="d-flex flex-row">
            <div class="p-1 flex-fill">
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="${id}_feature">
                <label class="form-check-label" for="featuredImageCheck">Featured Image</label>
              </div>
            </div>
            <div class="p-1 flex-fill d-grid gap-2">
              <button type="button" class="delete btn btn-danger btn-sm">Delete</button>
            </div>
            <div class="p-1 flex-fill d-grid gap-2">
              <button type="button" class="update btn btn-dark btn-sm">Update</button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>`

  filesFrame.insertAdjacentHTML('afterbegin', html)
}

async function getUploadedFiles() {
  const url = `${window.origin}/admin/post/upload/get_files`
  const options = { method: 'GET' }

  const responce = await fetch(url, options)
  const data = await responce.json()

  return data
}

async function getUploadedFile(filename) {
  const url = `${window.origin}/admin/post/upload/get_file/${filename}`
  const options = { method: 'GET' }

  const responce = await fetch(url, options)
  const data = await responce.json()

  return data
}

async function newPost() {
  // gerekli bilgileri localstorage'dan alalir post eder.
  let entry = {
    name: newPostForm.title.value,
    description: newPostForm.description.value,
    category: newPostForm.categorySelect.value,
  }

  const url = `${window.origin}/admin/post/new_post`
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': newPostForm.csrf_token.value,
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
