console.log('--- POST ---')
console.log(current_user)

const newPostForm = document.getElementById('new-post-form')
const filesFrame = document.getElementById('uploaded-files')

// Dropzone Settings
Dropzone.options.newPostDropzone = {
  paramName: 'file',
  maxFilesize: 4,
  addRemoveLinks: true,
  // headers: {
  //   'X-CSRF-Token': newPostForm.csrf_token.value,
  // },
  accept: (file, done) => {
    done()
  },
  renameFile: (file) => {
    console.log(file.name)
  },
}

// Dropzone Events
Dropzone.options.newPostDropzone = {
  init: function () {
    this.on('addedfile', (file) => {
      console.log('Added in Dropzone! ->', file.name)
    })

    this.on('success', (file) => {
      console.log('Success! ->', file.name)
      getUploadedFile(file.name)
        .then((data) => addImagesToDOM(data))
        .catch((err) => console.log(err))
    })

    // this.on('complete', (file) => {
    //   this.removeFile(file)
    // })
  },
}

function addImagesToDOM(data) {
  // data.file_names.forEach((file) => {
  //   let html = `<img src="${window.origin}/static/upload/samsimsom/${file}">`
  //   filesFrame.insertAdjacentHTML('beforebegin', html)
  // })

  console.log(data)

  let html = `<img src="${window.origin}/static/upload/samsimsom/${data.fileName}" class="uploaded-image">`
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
