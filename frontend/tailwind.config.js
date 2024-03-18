/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'main_red': '#77142B',
                'red_selected': '#9b0014',
                'main_grey': '#666666',
                'grey_selected': '#9b9b9b',
                'main_white': '#FFFFFF',
                'main_black': '#000000'
            },
            fontFamily: {
                oswald: ['Oswald', 'sans-serif'],
                roboto: ['Roboto Condensed', 'sans-serif']
            },
        },
    },
    plugins: [],
}