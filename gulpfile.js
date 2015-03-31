var gulp = require('gulp');
var sourcemaps = require('gulp-sourcemaps');

const JS_PATH = './web/js/**/*.js';
const CSS_PATH = './web/css/**/*.scss';

function processJS() {
    var browserify = require('browserify');
    var gutil = require('gulp-util');
    var source = require('vinyl-source-stream');
    var buffer = require('vinyl-buffer');
    var uglify = require('gulp-uglify');
    require('glob')(JS_PATH, {}, function (err, files) {
        var b = browserify();
        files.forEach(function (file) {
            b.add(file);
        });
        b.bundle()
            .on('log', gutil.log) // output build logs to terminal
            .on('error', gutil.log.bind(gutil, 'Browserify Error'))
            .pipe(source('bundle.js'))
            .pipe(buffer())
            .pipe(uglify())
            .pipe(sourcemaps.init({loadMaps: true})) // loads map from browserify file
            .pipe(sourcemaps.write('.')) // writes .map file
            .pipe(gulp.dest('./public/js'));
    });
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
    processJS();
    processCSS();
    gulp.watch(CSS_PATH, ['sass']);
    gulp.watch(JS_PATH, ['javascript']);
});