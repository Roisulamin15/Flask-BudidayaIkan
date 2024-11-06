module.exports = {
  content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
  ],
  theme: {
    extend: {
      backgroundImage : {
        'bg' : "url('https://sito.libero.it/livedrawhongkongpools/wp-content/uploads/sites/9457/2022/05/cara-bermain-gates-of-olympus-1-1.jpg')"
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}