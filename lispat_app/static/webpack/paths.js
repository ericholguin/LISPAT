const path = require('path');

module.exports = {
  root: path.resolve(__dirname, '../'),
  outputPath: path.resolve(__dirname, '../', 'build'),
  entryPath: path.resolve(__dirname, '../', 'src/index.jsx'),
  templatePath: path.resolve(__dirname, '../', 'src/template.html'),
  imagePath: path.resolve(__dirname, '../', 'images'),
  imagesFolder: 'images',
  fontsFolder: 'fonts',
  cssFolder: 'bundle',
  jsFolder: 'bundle',
};
