console.log('--- POST ---')
console.log(current_user)

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
    })

    // this.on('complete', (file) => {
    //   this.removeFile(file)
    // })
  },
}
