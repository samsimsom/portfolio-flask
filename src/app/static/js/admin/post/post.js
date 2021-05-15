/*----------------------------------------------------------------------------*/
// Global Variables
const newPostForm = document.getElementById('new-post-form')
const uploadedFilesFrame = document.getElementById('uploaded-files')

/*----------------------------------------------------------------------------*/
// Dropzone
Dropzone.options.postDropzoneContainer = {
  paramName: 'file',
  maxFilesize: 5,
  renameFile: (file) => {
    return renameUploadingFile(file)
  },

  init: function () {
    this.on('addedfile', (file) => {
      console.log('Added! ->', file.upload.filename)
    })

    this.on('success', (file) => {
      console.log('Success! ->', file.upload.filename)
      generateUploadedCard(file.upload.filename)

      // Uploaded card added event listener
      let id = getIdFromFileName(file.upload.filename)
      let card = document.getElementById(`${id}_card`)
      card.addEventListener('click', (e) => {
        cardEvent(e)
      })
    })

    this.on('complete', (file) => {
      console.log('Removed! ->', file.upload.filename)
      this.removeFile(file)
    })
  },
}

// Rename Uploading File with secure file name
function renameUploadingFile(file) {
  let splitName = file.name.split(/\.(?=[^\.]+$)/)
  let fileName = splitName[0].replace(/[^a-z0-9]/gi, '_').toLowerCase()
  let extension = splitName[1].toLowerCase()
  let newName = `${generateRandomId()}-${fileName}`
  return `${newName}.${extension}`
}

// Return File ID Extracted in File Name
function getIdFromFileName(filename) {
  let id = filename.split(/\-(?=[^\-]+$)/)[0]
  return id
}

// File Id Generator
function generateRandomId() {
  let randomString = Math.random().toString(36).substr(2, 9).toLowerCase()
  let date = new Date().getTime()
  return `${randomString}-${date}`
}

/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Uploaded card HTML
function generateUploadedCard(filename) {
  let id = getIdFromFileName(filename)
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
              <button type="button" class="btn btn-danger btn-sm" id="${id}_delete">Delete</button>
            </div>
            <div class="p-1 flex-fill d-grid gap-2">
              <button type="button" class="btn btn-dark btn-sm" id="${id}_update">Update</button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>`

  uploadedFilesFrame.insertAdjacentHTML('afterbegin', html)
}
/*----------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------*/
// Uploaded Card Event
function cardEvent(e) {
  let id = e.target.id
  if (id.includes('name')) {
    console.log(e.target.value)
  }

  if (id.includes('weight')) {
    console.log(e.target.value)
  }

  if (id.includes('feature')) {
    console.log(document.getElementById(id).checked)
    console.log(e.target.value)
  }

  if (id.includes('delete')) {
    console.log(`${id} -> DELETED!`)
  }

  if (id.includes('update')) {
    console.log(`${id} -> UPDATE!`)
  }
}
/*----------------------------------------------------------------------------*/
