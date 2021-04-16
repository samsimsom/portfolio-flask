console.log('--- POST ---')
// console.log(current_user)

// Dropzone Settings
Dropzone.options.newPostDropzone = {
  paramName: 'file',
  maxFilesize: 4, // MB
  addRemoveLinks: true,
  accept: function (file, done) {
    if (file.name == 'justinbieber.jpg') {
      done("Naha, you don't.")
    } else {
      done()
    }
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

    // this.on('complete', (file) => {
    //   this.removeFile(file)
    // })
  },
}
