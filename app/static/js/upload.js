function showUploadWidget() {
  cloudinary.openUploadWidget(
    {
      cloudName: "dsbucgfga",
      uploadPreset: "tpkvym31",
      sources: [
        "local",
        "url",
        "camera",
        "dropbox",
        "instagram",
        "google_drive",
      ],
      googleApiKey: "<image_search_google_api_key>",
      showAdvancedOptions: true,
      cropping: false,
      multiple: true,
      defaultSource: "local",
      styles: {
        palette: {
          window: "#F5F5F5",
          sourceBg: "#FFFFFF",
          windowBorder: "#90a0b3",
          tabIcon: "#0094c7",
          inactiveTabIcon: "#69778A",
          menuIcons: "#0094C7",
          link: "#53ad9d",
          action: "#8F5DA5",
          inProgress: "#0194c7",
          complete: "#53ad9d",
          error: "#c43737",
          textDark: "#000000",
          textLight: "#FFFFFF",
        },
        fonts: {
          default: null,
          "'Poppins', sans-serif": {
            url: "https://fonts.googleapis.com/css?family=Poppins",
            active: true,
          },
        },
      },
    },
    (err, info) => {
      if (!err) {
        console.log("Upload Widget event - ", info);
      }
    }
  );
}
