const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require('copy-webpack-plugin');
const path = require("path");

module.exports = {
    entry: [
        "./assets/index.js",
        "./assets/index.scss",
    ],
    output: {
        filename: "index.js",
        path: path.resolve(__dirname, "static/example"),
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "index.css"
        }),
        new CopyWebpackPlugin([
            {from: 'assets/images/', to: 'images'},
            {from: './node_modules/jquery', to: 'jquery'},
            {from: './node_modules/jquery-ui-dist', to: 'jquery-ui'},
            {from: './node_modules/@fortawesome/fontawesome-free', to: 'fontawesome'},
            {from: './node_modules/sweetalert2/dist', to: 'sweetalert2'},
            {from: './node_modules/smartwizard/dist', to: 'smartwizard'},
            {from: './node_modules/bootstrap/dist', to: 'bootstrap'},
            {from: './node_modules/popper.js/dist', to: 'popper'},
        ]),
    ],
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    "css-loader",
                    "sass-loader"
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    'file-loader',
                ],
            },
        ]
    }
};