/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}", "./public/index.html"],
  theme: {
    extend: {
      colors: {
        customBlue: "#343C6A",
        customGreen: "#4CAF50",
      },
    },
  },
  plugins: [],
};
