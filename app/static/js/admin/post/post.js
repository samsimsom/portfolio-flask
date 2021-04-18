console.log('--- POST ---')
// console.log(current_user)

const newPostForm = document.getElementById('new-post-form')
const filesFrame = document.getElementById('uploaded-files')
const form = document.getElementById('new-post-form')

// Dropzone Settings
Dropzone.options.postDropzoneContainer = {
  paramName: 'file',
  maxFilesize: 5,
  renameFile: (file) => {
    let splitName = file.name.split(/\.(?=[^\.]+$)/)
    let fileName = splitName[0].replace(/[^a-z0-9]/gi, '_').toLowerCase()
    let extension = splitName[1].toLowerCase()
    let id = Math.random().toString(36).substr(2, 9)
    let date = new Date().getTime()
    let fileId = id + '_' + date
    let newName = fileId + '_' + fileName
    let secureName = newName + '.' + extension
    return secureName
  },

  init: function () {
    this.on('addedfile', (file) => {
      console.log('Added in Dropzone! ->', file.upload.filename)
    })

    this.on('success', (file) => {
      console.log('Success! ->', file.upload.filename)
      addImagesToDOM(file.upload.filename)
      let item = document.getElementById(
        file.upload.filename.split(/\_(?=[^\_]+$)/)[0]
      )
      item.addEventListener('click', (e) => {
        // console.log(e)
        if (e.target.id === 'featuredImageCheck') {
          // console.log('checked')
          let checkBoxes = document.querySelectorAll('.form-check-input')
          checkBoxes.forEach((box) => {
            // console.log(box.disabled)
            if (!box.checked) {
              console.log('Disable')
            }
          })
        }
      })

      // getUploadedFile(file.upload.filename)
      //   .then((data) => addImagesToDOM(data))
      //   .catch((err) => console.log(err))
    })

    this.on('complete', (file) => {
      this.removeFile(file)
    })
  },
}

form.addEventListener('submit', (e) => {
  e.preventDefault()

  newPost()
    .then((data) => console.log(data))
    .catch((err) => console.log(err))
})

function addImagesToDOM(filename) {
  let html = `
      <div class="border rounded p-1" id="${
        filename.split(/\_(?=[^\_]+$)/)[0]
      }">
      <div class="d-flex flex-row">
        <div class="d-flex flex-column">
          <div class="p-1 bd-highlight">
            <img src="${window.origin}/static/upload/samsimsom/${filename}"
                class="uploaded-image rounded">
          </div>
        </div>
        <div class="d-flex flex-column flex-fill">

          <div class="input-group input-group-sm p-1">
            <span class="input-group-text"
                  id="#">Name : &ThinSpace;</span>
            <input type="text" class="form-control" value="${filename}">
          </div>

          <div class="input-group input-group-sm p-1">
            <span class="input-group-text"
                  id="#">Weight :</span>
            <input type="number" min="0" class="form-control" value="0">
          </div>

          <div class="d-flex flex-column">
            <div class="d-flex flex-row">
              <div class="p-1 flex-fill">
                <div class="form-check form-switch">
                  <input class="form-check-input"
                        type="checkbox"
                        id="featuredImageCheck">
                  <label class="form-check-label"
                        for="featuredImageCheck">Featured Image</label>
                </div>
              </div>
              <div class="p-1 flex-fill d-grid gap-2">
                <button type="button" class="btn btn-dark btn-sm">Update</button>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>`

  filesFrame.insertAdjacentHTML('afterbegin', html)
}

// Reload Page Event
window.onbeforeunload = function (e) {
  // document.cookie = 'cookiename=; expires=' + d.toGMTString() + ';'
  console.log(e)
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
  let entry = {
    name: form.title.value,
    description: form.description.value,
    category: form.categorySelect.value,
  }

  const url = `${window.origin}/admin/post/new_post`
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
