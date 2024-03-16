/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        colors: {
            'main_red': '#77142B',
            'main_grey': '#666666',
            'bg_white': '#FFFFFF',
            'main_black': '#000000'
        },
        extend: {
            fontFamily: {
                oswald: ['Oswald', 'sans-serif'],
            },
        },
    },
    plugins: [],
}