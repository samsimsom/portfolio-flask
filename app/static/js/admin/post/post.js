console.log('--- POST ---')
// console.log(current_user)

const newPostForm = document.getElementById('new-post-form')
const filesFrame = document.getElementById('uploaded-files')
let fileId

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
    fileId = id + '_' + date
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
      getUploadedFile(file.upload.filename)
        .then((data) => addImagesToDOM(data))
        .catch((err) => console.log(err))
    })

    this.on('complete', (file) => {
      this.removeFile(file)
    })
  },
}

function addImagesToDOM(data) {
  let html = `
      <div class="border rounded p-1" id="${fileId}">
      <div class="d-flex flex-row">
        <div class="d-flex flex-column">
          <div class="p-1 bd-highlight">
            <img src="${window.origin}/static/upload/samsimsom/${data.fileName}"
                class="uploaded-image rounded">
          </div>
        </div>
        <div class="d-flex flex-column flex-fill">

          <div class="input-group input-group-sm p-1">
            <span class="input-group-text"
                  id="#">Name : &ThinSpace;</span>
            <input type="text" class="form-control" value="${data.fileName}">
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
                        id="flexSwitchCheckChecked" checked>
                  <label class="form-check-label"
                        for="flexSwitchCheckChecked">Featured Image</label>
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

  filesFrame.insertAdjacentHTML('beforebegin', html)
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
