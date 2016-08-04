import path from 'path';

const config = {
  entry: path.join(__dirname, '..', 'src', 'index.js'),

  output: {
    path: path.join(__dirname, '..', 'build'),
    filename: 'bundle.js',
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: path.join(__dirname, '..', 'src'),
        presets: [
          'node5',
          'stage-0',
        ],
      },
      {
        test: /\.json$/,
        loader: 'json-loader',
      },
    ],
    noParse: /node_modules\/json-schema\/lib\/validate\.js/, // https://github.com/request/request/issues/1920
  },

  target: 'node',
};

export default config;
