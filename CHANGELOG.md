# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased][unreleased]


## [2.0.0] - 2016-04-04
### Added
- added decorators: **frame**, **thin frame**, **double frame**, **paper**
- added renderers: **sharp**, **drawille**

### Changed
- changed signature of tchart!
- refactored ChartRenderer for separate chart renderer and chart decorator
    - name of current renderer is **box**, and current decorator is **axis**


## [1.1.0] - 2016-03-30
### Changed
- supported Python is 2.7, 3.4, 3.5 *(removed 3.2, added 2.7)*
- changed license from GPLv2 to GPLv3
- small deployment & testing related changes
- Pylint ready code


## [1.0.1] - 2015-10-27
### Added
- added example screenshots
- enhanced readme with usage, badges and screenshots
- improved test environment
- wrote unit tests for bad dimension error #3

### Fixed
- horizontal scaling works bad in some cases #1
- fixed building on Python3.2 in Travis #2


## 1.0.0 - 2015-10-20
### Added
- ``tchart`` lib with unit tests
- random chart generator example


[unreleased]: https://github.com/andras-tim/tchart/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/andras-tim/tchart/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/andras-tim/tchart/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/andras-tim/tchart/compare/v1.0.0...v1.0.1
