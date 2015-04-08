var gulp = require('gulp');
var sourcemaps = require('gulp-sourcemaps');
var wp = require("webpack");
var webpack = require('gulp-webpack');
var uglify = require('gulp-uglify');

const JS_PATH = './web/js/**/*.js';
const JS_DEST = './public/js';
const CSS_PATH = './web/css/**/*.scss';

function processJS(need_watch) {
    if (need_watch == undefined) need_watch = false;
    return gulp.src(JS_PATH)
        .pipe(webpack({
            output: {
                filename: 'bundle.js' //this is the default name, so you can skip it
            },
            //devtool: "eval-source-map",
            module: {
                loaders: [
                    { test: /\.js$/, loader: "jsx-loader?harmony" },
                    { test: /\.json$/, loader: "json-loader" },
                    { test: /masonry-layout/, loader: 'imports?define=>false&this=>window'}
                ]
            },
            plugins: [
                new wp.optimize.UglifyJsPlugin({
                    compress: { warnings: false}
                })
            ],
            watch : need_watch
        }))
        .pipe(gulp.dest(JS_DEST));
}
gulp.task('javascript', processJS);


function processCSS() {
    var sass = require('gulp-sass'),
        minifyCSS = require('gulp-minify-css');
    gulp.src(CSS_PATH)
        .pipe(sourcemaps.init())
        .pipe(sass({
            outpuStyle: 'compressed',
            errLogToConsole: true
        }))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./public/css'))
        .pipe(minifyCSS());
}
gulp.task('sass', processCSS);

gulp.task('watch', function () {
    processJS(true);
    processCSS();
    gulp.watch(CSS_PATH, ['sass']);
});