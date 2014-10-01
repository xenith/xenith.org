module.exports = function (grunt) {

  var appConfig = grunt.file.readJSON('package.json');

  // Load grunt tasks automatically
  // see: https://github.com/sindresorhus/load-grunt-tasks
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take. Can help when optimizing build times
  // see: https://npmjs.org/package/time-grunt
  require('time-grunt')(grunt);

  var pathsConfig = function (appName) {
    this.app = appName || appConfig.name;

    return {
      app: this.app,
      templates: this.app + '/templates',
      css: this.app + '/static/css',
      sass: this.app + '/static/sass',
      fonts: this.app + '/static/fonts',
      images: this.app + '/static/images',
      js: this.app + '/static/js',
      manageScript: './manage.py'
    }
  };

  grunt.initConfig({

    paths: pathsConfig(),
    pkg: appConfig,

    // see: https://github.com/gruntjs/grunt-contrib-watch
    watch: {
      gruntfile: {
        files: ['Gruntfile.js']
      },
      compass: {
        files: ['<%= paths.sass %>/**/*.{scss,sass}'],
        tasks: ['compass:server']
      },
      livereload: {
        files: [
          '<%= paths.js %>/**/*.js',
          '<%= paths.sass %>/**/*.{scss,sass}',
          './**/*.html'
          ],
        options: {
          spawn: false,
          livereload: true,
        },
      },
    },

    // see: https://github.com/gruntjs/grunt-contrib-compass
    compass: {
      options: {
          basePath: '<%= paths.app %>',
          sassDir: 'static/sass',
          cssDir: 'static/css',
          fontsDir: 'static/fonts',
          imagesDir: 'static/images',
          relativeAssets: false,
          assetCacheBuster: false,
          outputStyle: 'compressed',
          raw: 'Sass::Script::Number.precision = 10\n',
          require: 'susy'
      },
      dist: {
        options: {
          environment: 'production'
        }
      },
      server: {
        options: {
          // debugInfo: true
        }
      }
    },

    // see: https://npmjs.org/package/grunt-bg-shell
    bgShell: {
      _defaults: {
        bg: true
      },
      runFlask: {
        cmd: 'python <%= paths.manageScript %> server'
      }
    }
  });

  grunt.registerTask('serve', [
    'bgShell:runFlask',
    'watch'
  ]);

  grunt.registerTask('build', [
    'compass:dist'
  ]);

  grunt.registerTask('default', [
    'build'
  ]);
};
