console.log('--- POST ---')
console.log(current_user)

const filesFrame = document.getElementById('uploaded-files')

// Dropzone Settings
Dropzone.options.newPostDropzone = {
  paramName: 'file',
  maxFilesize: 4,
  addRemoveLinks: true,
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
      getUploadedFiles()
        .then((data) => addImagesToDOM(data))
        .catch((err) => console.log(err))
    })

    // this.on('complete', (file) => {
    //   this.removeFile(file)
    // })
  },
}

function addImagesToDOM(data) {
  console.log(data)
}

async function getUploadedFiles() {
  const url = `${window.origin}/admin/post/upload/get_files`
  const options = { method: 'GET' }

  const responce = await fetch(url, options)
  const data = await responce.json()

  return data
}
