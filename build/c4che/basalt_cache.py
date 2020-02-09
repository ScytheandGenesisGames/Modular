AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'basalt'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'basalt'
BUNDLE_NAME = 'Modular.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['basalt']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'gitHead': u'14f03a968987058c9eadcd42122b512f3458725d', u'_location': u'/pebble-generic-weather', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-generic-weather/-/pebble-generic-weather-1.1.6.tgz', u'shasum': u'e6c85b3d19a69578eadeba4d01bea3eaac661ed6'}, u'_spec': u'pebble-generic-weather', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-generic-weather-1.1.6.tgz_1476819802593_0.7969138235785067', u'host': u'packages-16-east.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'pebble-generic-weather@latest', u'pebble': {u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'projectType': u'package', u'messageKeys': [u'GW_APIKEY', u'GW_BADKEY', u'GW_CONDITIONCODE', u'GW_DAY', u'GW_DESCRIPTION', u'GW_FEELS_LIKE', u'GW_LATITUDE', u'GW_LOCATIONUNAVAILABLE', u'GW_LONGITUDE', u'GW_NAME', u'GW_PROVIDER', u'GW_REPLY', u'GW_REQUEST', u'GW_SUNRISE', u'GW_SUNSET', u'GW_TEMPK'], u'sdkVersion': u'3', u'capabilities': [u'location'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-generic-weather', u'/home/thesillybatdoc/Pebble-Projects/Modular']], u'_nodeVersion': u'5.6.0', u'version': u'1.1.6', u'_resolved': u'https://registry.npmjs.org/pebble-generic-weather/-/pebble-generic-weather-1.1.6.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/gregoiresage/pebble-generic-weather#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.5', u'_requested': {u'name': u'pebble-generic-weather', u'rawSpec': u'', u'raw': u'pebble-generic-weather', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Library for easy fetching of weather data from various providers.', u'repository': {u'url': u'git+https://github.com/gregoiresage/pebble-generic-weather.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'gregoire', u'email': u'gregoire.sage@gmail.com'}], u'dependencies': {u'suncalc': u'^1.7.0', u'pebble-events': u'^1.0.0'}, u'scripts': {}, 'path': 'node_modules/pebble-generic-weather/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-generic-weather', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Gr\xe9goire Sage'}, u'bugs': {u'url': u'https://github.com/gregoiresage/pebble-generic-weather/issues'}, u'_npmUser': {u'email': u'gregoire.sage@gmail.com', u'name': u'gregoire'}, 'js_paths': ['node_modules/pebble-generic-weather/dist/js/index.js'], u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular', u'_id': u'pebble-generic-weather@1.1.6', u'_shasum': u'e6c85b3d19a69578eadeba4d01bea3eaac661ed6'}, {u'_location': u'/pebble-simple-health', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-simple-health/-/pebble-simple-health-1.0.6.tgz', u'shasum': u'6589f38778c52ef2b4c313d48154659f1a113b54'}, u'_spec': u'pebble-simple-health', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-simple-health-1.0.6.tgz_1476374436453_0.7390608100686222', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'pebble-simple-health@latest', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-simple-health', u'/home/thesillybatdoc/Pebble-Projects/Modular']], u'_nodeVersion': u'4.2.6', u'version': u'1.0.6', u'_resolved': u'https://registry.npmjs.org/pebble-simple-health/-/pebble-simple-health-1.0.6.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/ygalanter/pebble-simple-health#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.5', u'_requested': {u'name': u'pebble-simple-health', u'rawSpec': u'', u'raw': u'pebble-simple-health', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Simlpe health library for Pebble', u'repository': {u'url': u'git+https://github.com/ygalanter/pebble-simple-health.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'ygalanter', u'email': u'yuri@galanter.net'}], u'dependencies': {u'pebble-events': u'^1.1.0'}, u'scripts': {}, 'path': 'node_modules/pebble-simple-health/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-simple-health', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Yuriy Galanter'}, u'bugs': {u'url': u'https://github.com/ygalanter/pebble-simple-health/issues'}, u'_npmUser': {u'email': u'yuri@galanter.net', u'name': u'ygalanter'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular', u'_id': u'pebble-simple-health@1.0.6', u'_shasum': u'6589f38778c52ef2b4c313d48154659f1a113b54'}, {u'gitHead': u'1bf6db08092ab464974d1762a953ea7cbd24efb8', u'_location': u'/pebble-clay', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}, u'_spec': u'pebble-clay', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-clay-1.0.4.tgz_1479759281024_0.1520081793423742', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'config', u'configuration', u'pebble', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'_from': u'pebble-clay@latest', u'pebble': {u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'sdkVersion': u'3', u'projectType': u'package', u'resources': {u'media': []}, u'capabilities': [u'configurable']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-clay', u'/home/thesillybatdoc/Pebble-Projects/Modular']], u'_nodeVersion': u'6.9.1', u'version': u'1.0.4', u'_resolved': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/clay#readme', u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-clay', u'rawSpec': u'', u'raw': u'pebble-clay', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Pebble Config Framework', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)', u'lint': u'eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean'}, 'path': 'node_modules/pebble-clay/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-clay', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Pebble Technology'}, u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, u'_npmUser': {u'email': u'webteam@getpebble.com', u'name': u'pebble-tech'}, 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular', u'_id': u'pebble-clay@1.0.4', u'_shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}, {u'gitHead': u'46b6272b962b9b6341766448a4e33fc7b7e6d0c1', u'_location': u'/pebble-events', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, u'_spec': u'pebble-events@^1.0.0', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-events-1.2.0.tgz_1476814456282_0.26054703164845705', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'pebble-events@>=1.0.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-events@^1.0.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather']], u'_nodeVersion': u'6.8.1', u'version': u'1.2.0', u'_resolved': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/katharine/pebble-events#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-events', u'rawSpec': u'^1.0.0', u'raw': u'pebble-events@^1.0.0', u'scope': None, u'type': u'range', u'spec': u'>=1.0.0 <2.0.0'}, u'description': u"A library to fix the Pebble SDK's event services.", u'repository': {u'url': u'git+https://github.com/katharine/pebble-events.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-generic-weather'], u'maintainers': [{u'name': u'katharine', u'email': u'katharine@kathar.in'}], u'dependencies': {u'@smallstoneapps/linked-list': u'^1.3.0'}, u'scripts': {}, 'path': 'node_modules/pebble-events/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-events', u'license': u'MIT', u'directories': {}, u'author': {u'email': u'katharine@pebble.com', u'name': u'Katharine Berry'}, u'bugs': {u'url': u'https://github.com/katharine/pebble-events/issues'}, u'_npmUser': {u'email': u'katharine@kathar.in', u'name': u'katharine'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather', u'_id': u'pebble-events@1.2.0', u'_shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, {u'gitHead': u'b08d1f6f8e56a3c0d85469d6cf0ff8675cba40a5', u'_location': u'/suncalc', u'dist': {u'tarball': u'https://registry.npmjs.org/suncalc/-/suncalc-1.8.0.tgz', u'shasum': u'1d9898109563078750f4994a959e654d876acbf5'}, u'_spec': u'suncalc@^1.7.0', u'_npmOperationalInternal': {u'tmp': u'tmp/suncalc-1.8.0.tgz_1482502981360_0.05787906516343355', u'host': u'packages-18-east.internal.npmjs.com'}, u'eslintConfig': {u'rules': {u'strict': 0, u'indent': 0, u'array-bracket-spacing': 0, u'brace-style': 0}, u'extends': u'mourner', u'env': {u'amd': True}}, u'keywords': [u'astronomy', u'calculation', u'illumination', u'math', u'moon', u'sun', u'sunrise', u'sunset', u'twilight'], u'devDependencies': {u'eslint-config-mourner': u'^2.0.1', u'tap': u'^8.0.1', u'eslint': u'^3.12.2'}, u'_from': u'suncalc@>=1.7.0 <2.0.0', u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'suncalc@^1.7.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather']], u'_nodeVersion': u'7.3.0', u'version': u'1.8.0', u'_resolved': u'https://registry.npmjs.org/suncalc/-/suncalc-1.8.0.tgz', u'readme': u'ERROR: No README data found!', u'main': u'suncalc.js', u'homepage': u'https://github.com/mourner/suncalc', u'_npmVersion': u'3.10.10', u'_requested': {u'name': u'suncalc', u'rawSpec': u'^1.7.0', u'raw': u'suncalc@^1.7.0', u'scope': None, u'type': u'range', u'spec': u'>=1.7.0 <2.0.0'}, u'description': u'A tiny JavaScript library for calculating sun/moon positions and phases.', u'repository': {u'url': u'git://github.com/mourner/suncalc.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-generic-weather'], u'maintainers': [{u'name': u'mourner', u'email': u'agafonkin@gmail.com'}], u'dependencies': {}, u'scripts': {u'test': u'tap test.js', u'pretest': u'eslint suncalc.js test.js', u'cov': u'tap test.js --cov'}, u'_installable': True, u'_shrinkwrap': None, u'name': u'suncalc', u'directories': {}, u'author': {u'name': u'Vladimir Agafonkin'}, u'bugs': {u'url': u'https://github.com/mourner/suncalc/issues'}, u'_npmUser': {u'email': u'agafonkin@gmail.com', u'name': u'mourner'}, 'js_paths': ['node_modules/suncalc/package.json', 'node_modules/suncalc/suncalc.js', 'node_modules/suncalc/test.js'], u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather', u'_id': u'suncalc@1.8.0', u'jshintConfig': {u'unused': True, u'trailing': True, u'quotmark': u'single'}, u'_shasum': u'1d9898109563078750f4994a959e654d876acbf5'}, {u'gitHead': u'46b6272b962b9b6341766448a4e33fc7b7e6d0c1', u'_location': u'/pebble-events', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, u'_spec': u'pebble-events@^1.0.0', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-events-1.2.0.tgz_1476814456282_0.26054703164845705', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'pebble-events@>=1.0.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-events@^1.0.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather']], u'_nodeVersion': u'6.8.1', u'version': u'1.2.0', u'_resolved': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/katharine/pebble-events#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-events', u'rawSpec': u'^1.0.0', u'raw': u'pebble-events@^1.0.0', u'scope': None, u'type': u'range', u'spec': u'>=1.0.0 <2.0.0'}, u'description': u"A library to fix the Pebble SDK's event services.", u'repository': {u'url': u'git+https://github.com/katharine/pebble-events.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-generic-weather'], u'maintainers': [{u'name': u'katharine', u'email': u'katharine@kathar.in'}], u'dependencies': {u'@smallstoneapps/linked-list': u'^1.3.0'}, u'scripts': {}, 'path': 'node_modules/pebble-events/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-events', u'license': u'MIT', u'directories': {}, u'author': {u'email': u'katharine@pebble.com', u'name': u'Katharine Berry'}, u'bugs': {u'url': u'https://github.com/katharine/pebble-events/issues'}, u'_npmUser': {u'email': u'katharine@kathar.in', u'name': u'katharine'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather', u'_id': u'pebble-events@1.2.0', u'_shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, {u'gitHead': u'46b6272b962b9b6341766448a4e33fc7b7e6d0c1', u'_location': u'/pebble-events', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, u'_spec': u'pebble-events@^1.0.0', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-events-1.2.0.tgz_1476814456282_0.26054703164845705', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'pebble-events@>=1.0.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-events@^1.0.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather']], u'_nodeVersion': u'6.8.1', u'version': u'1.2.0', u'_resolved': u'https://registry.npmjs.org/pebble-events/-/pebble-events-1.2.0.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/katharine/pebble-events#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-events', u'rawSpec': u'^1.0.0', u'raw': u'pebble-events@^1.0.0', u'scope': None, u'type': u'range', u'spec': u'>=1.0.0 <2.0.0'}, u'description': u"A library to fix the Pebble SDK's event services.", u'repository': {u'url': u'git+https://github.com/katharine/pebble-events.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-generic-weather'], u'maintainers': [{u'name': u'katharine', u'email': u'katharine@kathar.in'}], u'dependencies': {u'@smallstoneapps/linked-list': u'^1.3.0'}, u'scripts': {}, 'path': 'node_modules/pebble-events/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-events', u'license': u'MIT', u'directories': {}, u'author': {u'email': u'katharine@pebble.com', u'name': u'Katharine Berry'}, u'bugs': {u'url': u'https://github.com/katharine/pebble-events/issues'}, u'_npmUser': {u'email': u'katharine@kathar.in', u'name': u'katharine'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-generic-weather', u'_id': u'pebble-events@1.2.0', u'_shasum': u'0b57797ad20bfc02aa7da764e5c47c62aeb3c366'}, {u'gitHead': u'4b575a4fae9f575ec978e0ac66dc84fea3e2e965', u'_location': u'/@smallstoneapps/linked-list', u'dist': {u'tarball': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}, u'_spec': u'@smallstoneapps/linked-list@^1.3.0', u'_npmOperationalInternal': {u'tmp': u'tmp/linked-list-1.4.0.tgz_1476813130672_0.23447094927541912', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'@smallstoneapps/linked-list@>=1.3.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'@smallstoneapps/linked-list@^1.3.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events']], u'_nodeVersion': u'6.8.1', u'version': u'1.4.0', u'_resolved': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'readme': u'ERROR: No README data found!', u'main': u'src/c/linked-list.c', u'homepage': u'https://github.com/smallstoneapps/linked-list#readme', u'files': [u'dist.zip', u'include/', u'src/'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'@smallstoneapps/linked-list', u'rawSpec': u'^1.3.0', u'raw': u'@smallstoneapps/linked-list@^1.3.0', u'scope': u'@smallstoneapps', u'type': u'range', u'spec': u'>=1.3.0 <2.0.0'}, u'description': u'Pebble library for doing linked lists', u'repository': {u'url': u'git+https://github.com/smallstoneapps/linked-list.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-events'], u'maintainers': [{u'name': u'smallstoneapps', u'email': u'pebble@matthewtole.com'}], u'dependencies': {}, u'scripts': {u'test': u'make'}, 'path': 'node_modules/@smallstoneapps/linked-list/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'@smallstoneapps/linked-list', u'license': u'MIT', u'directories': {u'test': u'tests'}, u'author': {u'email': u'pebble@matthewtole.com', u'name': u'Matthew Tole'}, u'bugs': {u'url': u'https://github.com/smallstoneapps/linked-list/issues'}, u'_npmUser': {u'email': u'pebble@matthewtole.com', u'name': u'smallstoneapps'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events', u'_id': u'@smallstoneapps/linked-list@1.4.0', u'_shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}, {u'gitHead': u'4b575a4fae9f575ec978e0ac66dc84fea3e2e965', u'_location': u'/@smallstoneapps/linked-list', u'dist': {u'tarball': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}, u'_spec': u'@smallstoneapps/linked-list@^1.3.0', u'_npmOperationalInternal': {u'tmp': u'tmp/linked-list-1.4.0.tgz_1476813130672_0.23447094927541912', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'@smallstoneapps/linked-list@>=1.3.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'@smallstoneapps/linked-list@^1.3.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events']], u'_nodeVersion': u'6.8.1', u'version': u'1.4.0', u'_resolved': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'readme': u'ERROR: No README data found!', u'main': u'src/c/linked-list.c', u'homepage': u'https://github.com/smallstoneapps/linked-list#readme', u'files': [u'dist.zip', u'include/', u'src/'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'@smallstoneapps/linked-list', u'rawSpec': u'^1.3.0', u'raw': u'@smallstoneapps/linked-list@^1.3.0', u'scope': u'@smallstoneapps', u'type': u'range', u'spec': u'>=1.3.0 <2.0.0'}, u'description': u'Pebble library for doing linked lists', u'repository': {u'url': u'git+https://github.com/smallstoneapps/linked-list.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-events'], u'maintainers': [{u'name': u'smallstoneapps', u'email': u'pebble@matthewtole.com'}], u'dependencies': {}, u'scripts': {u'test': u'make'}, 'path': 'node_modules/@smallstoneapps/linked-list/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'@smallstoneapps/linked-list', u'license': u'MIT', u'directories': {u'test': u'tests'}, u'author': {u'email': u'pebble@matthewtole.com', u'name': u'Matthew Tole'}, u'bugs': {u'url': u'https://github.com/smallstoneapps/linked-list/issues'}, u'_npmUser': {u'email': u'pebble@matthewtole.com', u'name': u'smallstoneapps'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events', u'_id': u'@smallstoneapps/linked-list@1.4.0', u'_shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}, {u'gitHead': u'4b575a4fae9f575ec978e0ac66dc84fea3e2e965', u'_location': u'/@smallstoneapps/linked-list', u'dist': {u'tarball': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}, u'_spec': u'@smallstoneapps/linked-list@^1.3.0', u'_npmOperationalInternal': {u'tmp': u'tmp/linked-list-1.4.0.tgz_1476813130672_0.23447094927541912', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {}, u'_from': u'@smallstoneapps/linked-list@>=1.3.0 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'@smallstoneapps/linked-list@^1.3.0', u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events']], u'_nodeVersion': u'6.8.1', u'version': u'1.4.0', u'_resolved': u'https://registry.npmjs.org/@smallstoneapps/linked-list/-/linked-list-1.4.0.tgz', u'readme': u'ERROR: No README data found!', u'main': u'src/c/linked-list.c', u'homepage': u'https://github.com/smallstoneapps/linked-list#readme', u'files': [u'dist.zip', u'include/', u'src/'], u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'@smallstoneapps/linked-list', u'rawSpec': u'^1.3.0', u'raw': u'@smallstoneapps/linked-list@^1.3.0', u'scope': u'@smallstoneapps', u'type': u'range', u'spec': u'>=1.3.0 <2.0.0'}, u'description': u'Pebble library for doing linked lists', u'repository': {u'url': u'git+https://github.com/smallstoneapps/linked-list.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/pebble-events'], u'maintainers': [{u'name': u'smallstoneapps', u'email': u'pebble@matthewtole.com'}], u'dependencies': {}, u'scripts': {u'test': u'make'}, 'path': 'node_modules/@smallstoneapps/linked-list/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'@smallstoneapps/linked-list', u'license': u'MIT', u'directories': {u'test': u'tests'}, u'author': {u'email': u'pebble@matthewtole.com', u'name': u'Matthew Tole'}, u'bugs': {u'url': u'https://github.com/smallstoneapps/linked-list/issues'}, u'_npmUser': {u'email': u'pebble@matthewtole.com', u'name': u'smallstoneapps'}, u'_where': u'/home/thesillybatdoc/Pebble-Projects/Modular/node_modules/pebble-events', u'_id': u'@smallstoneapps/linked-list@1.4.0', u'_shasum': u'33ab0472202899b07e0ba318d49daf86770319d9'}]
LIB_RESOURCES_JSON = {u'pebble-clay': [], u'pebble-generic-weather': [], u'pebble-simple-health': [], u'suncalc': {}, u'@smallstoneapps/linked-list': {}, u'pebble-events': []}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'GW_LATITUDE': 10007, u'GW_CONDITIONCODE': 10003, u'GW_FEELS_LIKE': 10006, u'GW_LOCATIONUNAVAILABLE': 10008, u'GW_DAY': 10004, u'GW_TEMPK': 10016, u'dummy': 10000, u'GW_REQUEST': 10013, u'GW_NAME': 10010, u'GW_SUNRISE': 10014, u'GW_PROVIDER': 10011, u'GW_REPLY': 10012, u'GW_LONGITUDE': 10009, u'GW_APIKEY': 10001, u'GW_SUNSET': 10015, u'GW_DESCRIPTION': 10005, u'GW_BADKEY': 10002}
MESSAGE_KEYS_DEFINITION = '/home/thesillybatdoc/Pebble-Projects/AppleModular/Modular/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/home/thesillybatdoc/Pebble-Projects/AppleModular/Modular/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/home/thesillybatdoc/Pebble-Projects/AppleModular/Modular/build/js/message_keys.json'
NODE_PATH = '/home/thesillybatdoc/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/thesillybatdoc/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/thesillybatdoc/.pebble-sdk/SDKs/current/sdk-core/pebble/basalt'
PEBBLE_SDK_ROOT = '/home/thesillybatdoc/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['basalt', 'color', 'rect', 'mic', 'strap', 'strappower', 'compass', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'basalt', 'BUNDLE_BIN_DIR': 'basalt', 'BUILD_DIR': 'basalt', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'basalt'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'GW_LATITUDE': 10007, u'GW_CONDITIONCODE': 10003, u'GW_FEELS_LIKE': 10006, u'GW_LOCATIONUNAVAILABLE': 10008, u'GW_DAY': 10004, u'GW_TEMPK': 10016, u'dummy': 10000, u'GW_REQUEST': 10013, u'GW_NAME': 10010, u'GW_SUNRISE': 10014, u'GW_PROVIDER': 10011, u'GW_REPLY': 10012, u'GW_LONGITUDE': 10009, u'GW_APIKEY': 10001, u'GW_SUNSET': 10015, u'GW_DESCRIPTION': 10005, u'GW_BADKEY': 10002}, u'watchapp': {u'watchface': True}, u'displayName': u'Apple Watch Modular', u'uuid': u'808813b8-4316-439d-a70b-ff76c0244ccf', u'messageKeys': {u'GW_LATITUDE': 10007, u'GW_CONDITIONCODE': 10003, u'GW_FEELS_LIKE': 10006, u'GW_LOCATIONUNAVAILABLE': 10008, u'GW_DAY': 10004, u'GW_TEMPK': 10016, u'dummy': 10000, u'GW_REQUEST': 10013, u'GW_NAME': 10010, u'GW_SUNRISE': 10014, u'GW_PROVIDER': 10011, u'GW_REPLY': 10012, u'GW_LONGITUDE': 10009, u'GW_APIKEY': 10001, u'GW_SUNSET': 10015, u'GW_DESCRIPTION': 10005, u'GW_BADKEY': 10002}, 'companyName': u'Dr Alexander the bat', u'enableMultiJS': True, u'sdkVersion': u'3', 'versionLabel': u'1.0', u'targetPlatforms': [u'basalt'], 'longName': u'Apple Watch Modular', 'shortName': u'Apple Watch Modular', u'resources': {u'media': [{u'type': u'font', u'name': u'WatchOSThin_30', u'file': u'fonts/WatchOSThin_30.otf'}, {u'type': u'font', u'name': u'WatchOSThin_22', u'file': u'fonts/WatchOSThin_22.otf'}, {u'type': u'font', u'name': u'WatchOSThin_24', u'file': u'fonts/WatchOSThin_24.otf'}, {u'type': u'font', u'name': u'WatchOSThin_26', u'file': u'fonts/WatchOSThin_26.otf'}, {u'type': u'font', u'name': u'WatchOSThin_15', u'file': u'fonts/WatchOSThin_15.otf'}]}, 'name': u'Apple_Watch_Modular'}
REQUESTED_PLATFORMS = [u'basalt']
RESOURCES_JSON = [{u'type': u'font', u'name': u'WatchOSThin_30', u'file': u'fonts/WatchOSThin_30.otf'}, {u'type': u'font', u'name': u'WatchOSThin_22', u'file': u'fonts/WatchOSThin_22.otf'}, {u'type': u'font', u'name': u'WatchOSThin_24', u'file': u'fonts/WatchOSThin_24.otf'}, {u'type': u'font', u'name': u'WatchOSThin_26', u'file': u'fonts/WatchOSThin_26.otf'}, {u'type': u'font', u'name': u'WatchOSThin_15', u'file': u'fonts/WatchOSThin_15.otf'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['emery', 'diorite', 'chalk', 'basalt', 'aplite']
TARGET_PLATFORMS = ['basalt']
TIMESTAMP = 1581292687
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/thesillybatdoc/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
